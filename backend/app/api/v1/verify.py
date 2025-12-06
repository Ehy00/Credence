import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.job import VerificationJob
from app.services import ingestion, claim_extraction, evidence_retrieval, fact_checking, aggregation
from app.integrations.openai_client import OpenAIClient
from app.integrations.gdelt_client import GDELTClient
from app.integrations.google_factcheck_client import GoogleFactCheckClient
from app.integrations.mbfc_client import MBFCClient
from app.models import document as document_model, claim as claim_model, evidence as evidence_model, verdict as verdict_model

router = APIRouter()

# naive in-memory job store
jobs: dict[str, VerificationJob] = {}

@router.post("/verify", response_model=VerificationJob)
async def verify(payload: dict, db: Session = Depends(get_db)):
    mode = payload.get("mode")
    text = payload.get("text")
    url = payload.get("url")
    claim = payload.get("claim")

    if mode not in {"claim", "url", "text"}:
        raise HTTPException(status_code=400, detail="mode must be claim|url|text")

    if mode == "claim" and not claim:
        raise HTTPException(status_code=400, detail="Missing claim text")

    raw_text = ""
    source_domain = None
    title = None

    if mode == "url":
        html = await ingestion.fetch_url(url)
        raw_text = ingestion.normalize_text(ingestion.html_to_text(html or ""))
        source_domain = url.split("//")[-1].split("/")[0] if url else None
    elif mode == "text":
        raw_text = ingestion.normalize_text(text or "")
    else:
        raw_text = claim

    doc = document_model.Document(
        url=url,
        source_domain=source_domain,
        title=title,
        raw_text=raw_text,
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)

    oa_client = OpenAIClient()
    gdelt_client = GDELTClient()
    google_factcheck_client = GoogleFactCheckClient()
    mbfc_client = MBFCClient()

    claims_data = (
        [{"text": raw_text, "topic": None, "confidence": 1.0}] if mode == "claim" else await claim_extraction.extract_claims(raw_text, oa_client)
    )

    claims_models = []
    verdicts = []
    evidences = []

    for c in claims_data:
        claim_obj = claim_model.Claim(document_id=doc.id, text=c.get("text"), topic=c.get("topic"), confidence=c.get("confidence"))
        db.add(claim_obj)
        db.commit()
        db.refresh(claim_obj)
        claims_models.append(claim_obj)

        ev = evidence_retrieval.retrieve_evidence(claim_obj.text, gdelt_client, google_factcheck_client, mbfc_client)
        for e in ev:
            ev_model = evidence_model.Evidence(
                claim_id=claim_obj.id,
                source_domain=e.get("domain"),
                url=e.get("url"),
                snippet=e.get("snippet"),
                credibility=e.get("credibility"),
                relevance=e.get("relevance"),
            )
            db.add(ev_model)
            db.commit()
            db.refresh(ev_model)
            evidences.append(ev_model)

        verdict_data = await fact_checking.generate_verdict(claim_obj.text, ev, oa_client)
        verdict_model_obj = verdict_model.Verdict(
            claim_id=claim_obj.id,
            label=verdict_data.get("label", "Unverified"),
            confidence=verdict_data.get("confidence", 0.0),
            rationale=verdict_data.get("rationale"),
            model_version="gpt-4o-mini",
        )
        db.add(verdict_model_obj)
        db.commit()
        db.refresh(verdict_model_obj)
        verdicts.append(verdict_model_obj)

    agg = aggregation.aggregate_article_verdict([{"label": v.label, "confidence": v.confidence} for v in verdicts])

    job_id = str(uuid.uuid4())
    job = VerificationJob(
        job_id=job_id,
        status="completed",
        document=doc,
        claims=claims_models,
        verdicts=verdicts,
        evidences=evidences,
        article_verdict=agg["article_verdict"],
        article_confidence=agg["article_confidence"],
    )
    jobs[job_id] = job

    return job

