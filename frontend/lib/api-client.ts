import axios from 'axios';
import { VerificationJob } from './types';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000';

const client = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export async function submitVerification(payload: {
  mode: 'claim' | 'url' | 'text';
  claim?: string;
  url?: string;
  text?: string;
}): Promise<VerificationJob> {
  const response = await client.post('/api/v1/verify', payload);
  return response.data;
}

export async function fetchJob(jobId: string): Promise<VerificationJob> {
  const response = await client.get(`/api/v1/jobs/${jobId}`);
  return response.data;
}

