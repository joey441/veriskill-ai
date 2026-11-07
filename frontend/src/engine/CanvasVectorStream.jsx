import React, { useRef, useEffect } from 'react';

export const CanvasVectorStream = ({ promptText, liveConstraint }) => {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    
    canvas.width = 700;
    canvas.height = 180;

    // Background Cyber Dark Theme
    ctx.fillStyle = '#090D16';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Cyber Grid lines
    ctx.strokeStyle = 'rgba(0, 243, 255, 0.05)';
    ctx.lineWidth = 1;
    for (let x = 0; x < canvas.width; x += 20) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, canvas.height);
      ctx.stroke();
    }

    // Adversarial OCR Noise Injection (Anti-Extension protection)
    for (let i = 0; i < 150; i++) {
      ctx.fillStyle = `rgba(0, 243, 255, ${Math.random() * 0.08})`;
      ctx.fillRect(Math.random() * canvas.width, Math.random() * canvas.height, 2, 2);
    }

    // Vector Header Stream
    ctx.font = '600 12px monospace';
    ctx.fillStyle = '#00F3FF';
    ctx.fillText('DYNAMIC CHALLENGE PAYLOAD [ENCRYPTED VECTOR STREAM]', 20, 30);

    // Main Prompt
    ctx.font = '500 13px sans-serif';
    ctx.fillStyle = '#E2E8F0';
    ctx.fillText(promptText, 20, 75);

    // Live Variable Constraint
    ctx.font = '700 12px monospace';
    ctx.fillStyle = '#FF0055';
    ctx.fillText(`LIVE CONSTRAINT: ${liveConstraint}`, 20, 125);

    // Cyber Framing Border
    ctx.strokeStyle = '#00F3FF';
    ctx.lineWidth = 1.5;
    ctx.strokeRect(10, 10, canvas.width - 20, canvas.height - 20);
    
  }, [promptText, liveConstraint]);

  return (
    <div className="relative rounded-xl overflow-hidden border border-cyan-500/30 bg-slate-950 p-2 shadow-[0_0_25px_rgba(0,243,255,0.15)]">
      <canvas ref={canvasRef} className="w-full rounded-lg block" />
      <div className="absolute top-3 right-4 flex items-center gap-2">
        <span className="w-2 h-2 rounded-full bg-cyan-400 animate-ping" />
        <span className="text-[10px] font-mono text-cyan-400 uppercase tracking-widest">DOM Scraping Blocked</span>
      </div>
    </div>
  );
};