'use client';

import { Claim, Verdict } from '../../lib/types';

export default function ClaimTable({ claims, verdicts }: { claims: Claim[]; verdicts: Verdict[] }) {
  const getVerdictForClaim = (claimId: number) => {
    return verdicts.find(v => v.claim_id === claimId);
  };

  return (
    <div className="bg-slate-900/60 border border-slate-800 rounded-lg p-6">
      <h2 className="text-xl font-semibold mb-4">Claims & Verdicts</h2>
      <div className="space-y-4">
        {claims.map((claim) => {
          const verdict = getVerdictForClaim(claim.id);
          return (
            <div key={claim.id} className="border border-slate-800 rounded-lg p-4">
              <p className="text-slate-200 mb-2">{claim.text}</p>
              {verdict && (
                <div className="flex items-center justify-between">
                  <span className={`px-2 py-1 rounded text-sm font-semibold ${
                    verdict.label === 'True' ? 'bg-green-900 text-green-200' :
                    verdict.label === 'False' ? 'bg-red-900 text-red-200' :
                    verdict.label === 'Misleading' ? 'bg-yellow-900 text-yellow-200' :
                    'bg-slate-800 text-slate-300'
                  }`}>
                    {verdict.label}
                  </span>
                  <span className="text-sm text-slate-400">Confidence: {(verdict.confidence * 100).toFixed(1)}%</span>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}

