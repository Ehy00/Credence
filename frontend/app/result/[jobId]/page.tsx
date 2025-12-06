'use client';

import { useEffect, useState } from 'react';
import { useParams } from 'next/navigation';
import Shell from '../../../components/layout/Shell';
import ArticleViewer from '../../../components/results/ArticleViewer';
import ClaimTable from '../../../components/results/ClaimTable';
import EvidenceList from '../../../components/results/EvidenceList';
import SourceCredibilityCard from '../../../components/results/SourceCredibilityCard';
import VerdictPieChart from '../../../components/charts/VerdictPieChart';
import { fetchJob } from '../../../lib/api-client';
import { VerificationJob } from '../../../lib/types';

export default function ResultPage() {
  const params = useParams();
  const jobId = params?.jobId as string;
  const [job, setJob] = useState<VerificationJob | null>(null);

  useEffect(() => {
    if (jobId) {
      fetchJob(jobId).then(setJob);
    }
  }, [jobId]);

  if (!job) return <Shell>Loading...</Shell>;

  return (
    <Shell>
      <div className="grid lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 space-y-4">
          <ArticleViewer article={job.document} claims={job.claims} />
          <ClaimTable claims={job.claims} verdicts={job.verdicts} />
          <EvidenceList evidences={job.evidences} />
        </div>
        <div className="space-y-4">
          <SourceCredibilityCard sources={job.evidences} />
          <VerdictPieChart data={job.verdicts.map((v) => ({ label: v.label, value: v.confidence * 100 }))} />
          <div className="bg-slate-900/60 border border-slate-800 rounded-lg p-4">
            <p className="text-sm text-slate-300">Article verdict</p>
            <p className="text-2xl font-semibold">{job.article_verdict}</p>
            <p className="text-slate-400">Confidence: {job.article_confidence}</p>
          </div>
        </div>
      </div>
    </Shell>
  );
}

