'use client';

import { Evidence } from '../../lib/types';

export default function SourceCredibilityCard({ sources }: { sources: Evidence[] }) {
  const uniqueDomains = Array.from(new Set(sources.map(s => s.source_domain).filter(Boolean)));
  const avgCredibility = sources.length > 0
    ? sources.reduce((sum, s) => sum + (s.credibility || 0), 0) / sources.length
    : 0;

  return (
    <div className="bg-slate-900/60 border border-slate-800 rounded-lg p-4">
      <h3 className="text-lg font-semibold mb-3">Source Credibility</h3>
      <div className="space-y-2">
        <div>
          <p className="text-sm text-slate-400">Average Credibility</p>
          <p className="text-2xl font-semibold">{(avgCredibility * 100).toFixed(1)}%</p>
        </div>
        <div>
          <p className="text-sm text-slate-400">Unique Sources</p>
          <p className="text-xl font-semibold">{uniqueDomains.length}</p>
        </div>
        <div>
          <p className="text-sm text-slate-400">Total Evidence</p>
          <p className="text-xl font-semibold">{sources.length}</p>
        </div>
      </div>
    </div>
  );
}

