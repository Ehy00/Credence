'use client';

import { Document, Claim } from '../../lib/types';

export default function ArticleViewer({ article, claims }: { article?: Document; claims: Claim[] }) {
  if (!article) return null;

  return (
    <div className="bg-slate-900/60 border border-slate-800 rounded-lg p-6">
      <h2 className="text-xl font-semibold mb-4">Article</h2>
      {article.url && (
        <a href={article.url} target="_blank" rel="noopener noreferrer" className="text-cyan-300 hover:underline mb-2 block">
          {article.url}
        </a>
      )}
      <div className="prose prose-invert max-w-none">
        <p className="text-slate-300 whitespace-pre-wrap">{article.raw_text}</p>
      </div>
      {claims.length > 0 && (
        <div className="mt-4 pt-4 border-t border-slate-800">
          <p className="text-sm text-slate-400">Extracted {claims.length} claim(s)</p>
        </div>
      )}
    </div>
  );
}

