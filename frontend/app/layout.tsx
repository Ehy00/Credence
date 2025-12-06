import './globals.css';
import './theme.css';
import { ReactNode } from 'react';

export const metadata = {
  title: 'Credence Lite',
  description: 'AI News Verification Dashboard',
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-slate-950 text-slate-100 min-h-screen">
        {children}
      </body>
    </html>
  );
}

