'use client';

import { Evidence } from '../../lib/types';

export default function EvidenceList({ evidences }: { evidences: Evidence[] }) {
  return (
    <div className="bg-slate-900/60 border border-slate-800 rounded-lg p-6">
      <h2 className="text-xl font-semibold mb-4">Evidence</h2>
      <div className="space-y-3">
        {evidences.map((evidence) => (
          <div key={evidence.id} className="border border-slate-800 rounded-lg p-3">
            {evidence.url && (
              <a href={evidence.url} target="_blank" rel="noopener noreferrer" className="text-cyan-300 hover:underline text-sm mb-1 block">
                {evidence.source_domain || evidence.url}
              </a>
            )}
            <p className="text-slate-300 text-sm">{evidence.snippet}</p>
            <div className="flex items-center gap-4 mt-2 text-xs text-slate-400">
              {evidence.credibility !== null && (
                <span>Credibility: {(evidence.credibility * 100).toFixed(0)}%</span>
              )}
              {evidence.relevance !== null && (
                <span>Relevance: {(evidence.relevance * 100).toFixed(0)}%</span>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

