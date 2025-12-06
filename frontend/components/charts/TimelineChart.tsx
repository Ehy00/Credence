'use client';

import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

type Point = { name: string; value: number };

export default function TimelineChart({ data }: { data: Point[] }) {
  return (
    <div style={{ width: '100%', height: 240 }}>
      <ResponsiveContainer>
        <LineChart data={data}>
          <XAxis dataKey="name" stroke="#94a3b8" />
          <YAxis stroke="#94a3b8" />
          <Tooltip />
          <Line type="monotone" dataKey="value" stroke="#22d3ee" strokeWidth={2} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

