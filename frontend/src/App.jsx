import React, { useState } from 'react';
import { CanvasVectorStream } from './engine/CanvasVectorStream';

// Sample taxonomy data (could be fetched from backend)
const TAXONOMIES = {
  tech: {
    prompt: "Debug async worker pool deadlock in Python FastAPI service payload.",
    constraint: "MUST_USE_BITWISE_MASK_NO_ASYNCIO_SLEEP",
  },
  finance: {
    prompt: "Reconcile Q3 EBITDA liabilities against unearned revenue entries.",
    constraint: "APPLY_2026_LOCALIZED_TAX_BRACKET_RULES",
  },
};

export default function App() {
  const [selected, setSelected] = useState('tech');

  const { prompt, constraint } = TAXONOMIES[selected];

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6 font-mono">
      <h1 className="text-2xl mb-4 text-cyan-400">VeriSkill AI Challenge Dashboard</h1>
      <div className="flex items-center space-x-4 mb-6">
        <label className="mr-2">Discipline:</label>
        <select
          className="bg-gray-800 text-white p-2 rounded"
          value={selected}
          onChange={(e) => setSelected(e.target.value)}
        >
          <option value="tech">Software Engineering</option>
          <option value="finance">Financial Accounting</option>
        </select>
      </div>
      <CanvasVectorStream promptText={prompt} liveConstraint={constraint} />
    </div>
  );
}
