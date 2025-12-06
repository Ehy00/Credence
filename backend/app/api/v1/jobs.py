from fastapi import APIRouter, HTTPException
from app.schemas.job import VerificationJob
from app.api.v1.verify import jobs

router = APIRouter()

@router.get("/jobs/{job_id}", response_model=VerificationJob)
async def get_job(job_id: str):
    job = jobs.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

