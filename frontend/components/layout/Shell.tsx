import Link from 'next/link';
import { ReactNode } from 'react';

export default function Shell({ children }: { children: ReactNode }) {
  return (
    <div className="min-h-screen">
      <nav className="bg-slate-900 border-b border-slate-800">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex items-center">
              <Link href="/" className="text-xl font-semibold text-cyan-300">
                Credence
              </Link>
            </div>
            <div className="flex items-center space-x-4">
              <Link href="/" className="text-slate-300 hover:text-cyan-300">Home</Link>
              <Link href="/verify" className="text-slate-300 hover:text-cyan-300">Verify</Link>
              <Link href="/admin" className="text-slate-300 hover:text-cyan-300">Admin</Link>
            </div>
          </div>
        </div>
      </nav>
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {children}
      </main>
    </div>
  );
}

