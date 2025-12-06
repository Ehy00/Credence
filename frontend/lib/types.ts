export interface Document {
  id: number;
  url?: string;
  title?: string;
  source_domain?: string;
  raw_text: string;
}

export interface Claim {
  id: number;
  text: string;
  topic?: string;
  confidence?: number;
  evidences?: Evidence[];
  verdicts?: Verdict[];
}

export interface Evidence {
  id: number;
  claim_id: number;
  source_domain?: string;
  url?: string;
  snippet?: string;
  credibility?: number;
  relevance?: number;
}

export interface Verdict {
  id: number;
  claim_id: number;
  label: string;
  confidence: number;
  rationale?: string;
  model_version?: string;
}

export interface VerificationJob {
  job_id: string;
  status: string;
  document?: Document;
  claims: Claim[];
  verdicts: Verdict[];
  evidences: Evidence[];
  article_verdict?: string;
  article_confidence?: number;
}

