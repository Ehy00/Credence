import Shell from '../../components/layout/Shell';

export default function AdminPage() {
  return (
    <Shell>
      <div className="space-y-4">
        <h1 className="text-2xl font-semibold">Admin</h1>
        <p className="text-slate-300">Manage overrides, monitor model performance, and trigger retraining.</p>
        <div className="bg-slate-900/60 border border-slate-800 rounded-lg p-4">
          <p className="text-sm text-slate-400">Stub view. Connect to admin APIs to manage labels.</p>
        </div>
      </div>
    </Shell>
  );
}

