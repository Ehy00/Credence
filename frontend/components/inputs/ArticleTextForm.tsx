'use client';

import { useState } from 'react';
import { submitVerification } from '../../lib/api-client';
import { useRouter } from 'next/navigation';

export default function ArticleTextForm() {
  const [text, setText] = useState('');
  const router = useRouter();

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const job = await submitVerification({ mode: 'text', text });
    router.push(`/result/${job.job_id}`);
  };

  return (
    <form onSubmit={onSubmit} className="bg-slate-900/60 border border-slate-800 rounded-lg p-4 space-y-3">
      <div className="flex items-center justify-between">
        <h2 className="text-lg font-semibold">Paste article text</h2>
        <span className="text-xs text-slate-400">Mode: Text</span>
      </div>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Paste the full article text for analysis"
        className="w-full bg-slate-950 border border-slate-800 rounded-md p-2 text-sm"
        rows={5}
        required
      />
      <button type="submit" className="w-full bg-cyan-500 hover:bg-cyan-400 text-slate-900 font-semibold py-2 rounded-md">
        Verify text
      </button>
    </form>
  );
}

