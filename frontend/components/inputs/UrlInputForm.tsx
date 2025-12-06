'use client';

import { useState } from 'react';
import { submitVerification } from '../../lib/api-client';
import { useRouter } from 'next/navigation';

export default function UrlInputForm() {
  const [url, setUrl] = useState('');
  const router = useRouter();

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const job = await submitVerification({ mode: 'url', url });
    router.push(`/result/${job.job_id}`);
  };

  return (
    <form onSubmit={onSubmit} className="bg-slate-900/60 border border-slate-800 rounded-lg p-4 space-y-3">
      <div className="flex items-center justify-between">
        <h2 className="text-lg font-semibold">Verify article URL</h2>
        <span className="text-xs text-slate-400">Mode: URL</span>
      </div>
      <input
        type="url"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="https://example.com/article"
        className="w-full bg-slate-950 border border-slate-800 rounded-md p-2 text-sm"
        required
      />
      <button type="submit" className="w-full bg-cyan-500 hover:bg-cyan-400 text-slate-900 font-semibold py-2 rounded-md">
        Verify URL
      </button>
    </form>
  );
}

