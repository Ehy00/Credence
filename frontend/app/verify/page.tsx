import Shell from '../../components/layout/Shell';
import ClaimInputForm from '../../components/inputs/ClaimInputForm';
import UrlInputForm from '../../components/inputs/UrlInputForm';
import ArticleTextForm from '../../components/inputs/ArticleTextForm';
import VerdictPieChart from '../../components/charts/VerdictPieChart';

export default function VerifyPage() {
  return (
    <Shell>
      <div className="grid lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2 space-y-6">
          <ClaimInputForm />
          <UrlInputForm />
          <ArticleTextForm />
        </div>
        <div className="bg-slate-900/60 border border-slate-800 rounded-lg p-4">
          <h2 className="text-lg font-semibold mb-2">Verdict Snapshot</h2>
          <VerdictPieChart data={[{ label: 'True', value: 40 }, { label: 'False', value: 20 }, { label: 'Misleading', value: 25 }, { label: 'Unverified', value: 15 }]} />
        </div>
      </div>
    </Shell>
  );
}

