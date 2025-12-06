import Link from 'next/link';
import Shell from '../components/layout/Shell';
import ClaimInputForm from '../components/inputs/ClaimInputForm';
import UrlInputForm from '../components/inputs/UrlInputForm';
import ArticleTextForm from '../components/inputs/ArticleTextForm';

export default function HomePage() {
  return (
    <Shell>
      <div className="space-y-8">
        <div>
          <h1 className="text-3xl font-semibold">Credence Lite</h1>
          <p className="text-slate-300 mt-2">Enter a claim or article to start verification.</p>
        </div>
        <div className="grid md:grid-cols-3 gap-6">
          <ClaimInputForm />
          <UrlInputForm />
          <ArticleTextForm />
        </div>
        <div>
          <Link href="/verify" className="text-cyan-300 hover:underline">Go to verification workspace →</Link>
        </div>
      </div>
    </Shell>
  );
}

