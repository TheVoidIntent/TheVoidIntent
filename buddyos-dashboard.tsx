import { useState, useEffect, useRef } from 'react';

const BuddyOSDashboard = () => {
  // State for metrics
  const [fci] = useState(0.83);
  const [dissonance] = useState(0.19);
  const [recovery] = useState(0.71);
  const [activeTab] = useState('dissonance');
  const [simulationRunning, setSimulationRunning] = useState(true);
  const [liveMode] = useState(true);
  
  // Agent responses
  const [intentResponse] = useState('Field integrity at acceptable levels. Minor dissonance detected in sector 7.');
  const [resonatorResponse] = useState('Applying harmonic correction. Recovery rate: 71%');
  
  // Canvas ref
  const canvasRef = useRef(null);
  
  // Format percentage from decimal
  const formatPercent = (value) => {
    return `${Math.round(value * 100)}%`;
  };
  
  // Toggle simulation running state
  const toggleSimulation = () => {
    setSimulationRunning(!simulationRunning);
  };
  
  // Trigger dissonance spike (just a UI function, not actually used in this simplified version)
  const triggerDissonance = () => {
    // This would normally update metrics and add an event
    console.log("Dissonance triggered");
  };
  
  // Export data (just a UI function, not actually used in this simplified version)
  const exportData = () => {
    alert('Data export initiated. File: BuddyOS_Analytics_Export.json');
  };
  
  // Sample data for the events table
  const dataEntries = [
    { id: 1, timestamp: '08:24:12', fci: 0.82, dissonance: 0.17, recovery: 0.74, eventType: 'Standard' },
    { id: 2, timestamp: '08:23:55', fci: 0.79, dissonance: 0.22, recovery: 0.68, eventType: 'Dissonance Spike' },
    { id: 3, timestamp: '08:23:38', fci: 0.85, dissonance: 0.14, recovery: 0.78, eventType: 'Standard' },
    { id: 4, timestamp: '08:23:21', fci: 0.84, dissonance: 0.15, recovery: 0.76, eventType: 'Standard' },
    { id: 5, timestamp: '08:23:03', fci: 0.88, dissonance: 0.11, recovery: 0.81, eventType: 'Harmonic Peak' }
  ];
  
  // Initialize the canvas for drawing
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    
    // Get drawing context
    const ctx = canvas.getContext('2d');
    
    // Set canvas dimensions
    const width = canvas.width;
    const height = canvas.height;
    
    let animationId = null;
    let lastTime = 0;
    let particles = [];
    let nodes = [];
    
    // Setup initial nodes
    nodes = [
      { type: 'intentSire', x: 200, y: 150, radius: 15, pulse: 0 },
      { type: 'resonator', x: 400, y: 250, radius: 15, pulse: 0 },
      { type: 'field', x: 300, y: 200, radius: 12, pulse: 0 },
      { type: 'field', x: 150, y: 300, radius: 10, pulse: 0 },
      { type: 'field', x: 450, y: 150, radius: 8, pulse: 0 }
    ];
    
    // Create particles
    for (let i = 0; i < 80; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 2,
        vy: (Math.random() - 0.5) * 2,
        radius: Math.random() * 3 + 2,
        fci: Math.random() * 0.3 + 0.7,
        dissonance: Math.random() * 0.2 + 0.1
      });
    }
    
    // Animation function
    const animate = (time) => {
      // Don't update if simulation is paused
      if (!simulationRunning) {
        animationId = requestAnimationFrame(animate);
        return;
      }
      
      // Calculate time delta
      const delta = time - lastTime;
      lastTime = time;
      
      // Clear canvas
      ctx.clearRect(0, 0, width, height);
      
      // Draw dark blue background
      ctx.fillStyle = 'rgba(15, 23, 42, 1)';
      ctx.fillRect(0, 0, width, height);
      
      // Draw grid lines
      ctx.strokeStyle = 'rgba(55, 65, 81, 0.2)';
      ctx.lineWidth = 1;
      
      // Horizontal grid lines
      for (let y = 0; y < height; y += 40) {
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(width, y);
        ctx.stroke();
      }
      
      // Vertical grid lines
      for (let x = 0; x < width; x += 40) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, height);
        ctx.stroke();
      }
      
      // Draw nodes
      for (let i = 0; i < nodes.length; i++) {
        const node = nodes[i];
        
        // Update pulse
        node.pulse = (node.pulse + 0.02) % 1;
        
        // Draw pulse wave
        const maxRadius = node.radius * 6;
        const pulseRadius = node.radius + node.pulse * maxRadius;
        
        ctx.beginPath();
        ctx.arc(node.x, node.y, pulseRadius, 0, Math.PI * 2);
        
        // Different colors for different node types with glow effect
        if (node.type === 'intentSire') {
          ctx.fillStyle = `rgba(244, 63, 94, ${0.8 * (1 - node.pulse)})`;
        } else if (node.type === 'resonator') {
          ctx.fillStyle = `rgba(16, 185, 129, ${0.8 * (1 - node.pulse)})`;
        } else {
          ctx.fillStyle = `rgba(59, 130, 246, ${0.8 * (1 - node.pulse)})`;
        }
        
        ctx.fill();
        
        // Draw node with glow effect
        ctx.beginPath();
        ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
        
        // Different colors for different node types
        if (node.type === 'intentSire') {
          ctx.fillStyle = '#f43f5e'; // Pink/red
          ctx.shadowColor = '#f43f5e';
          ctx.shadowBlur = 15;
        } else if (node.type === 'resonator') {
          ctx.fillStyle = '#10b981'; // Green
          ctx.shadowColor = '#10b981';
          ctx.shadowBlur = 15;
        } else {
          ctx.fillStyle = '#3b82f6'; // Blue
          ctx.shadowColor = '#3b82f6';
          ctx.shadowBlur = 15;
        }
        
        ctx.fill();
        ctx.shadowBlur = 0; // Reset shadow
      }
      
      // Draw connections between particles and nearby nodes
      for (let i = 0; i < particles.length; i++) {
        const particle = particles[i];
        
        for (let j = 0; j < nodes.length; j++) {
          const node = nodes[j];
          const dx = particle.x - node.x;
          const dy = particle.y - node.y;
          const distance = Math.sqrt(dx * dx + dy * dy);
          
          if (distance < 80) {
            // Draw connection
            ctx.beginPath();
            ctx.moveTo(particle.x, particle.y);
            ctx.lineTo(node.x, node.y);
            
            let alpha = 1 - distance / 80;
            
            // Different colors for different node types
            if (node.type === 'intentSire') {
              ctx.strokeStyle = `rgba(244, 63, 94, ${alpha * 0.6})`;
            } else if (node.type === 'resonator') {
              ctx.strokeStyle = `rgba(16, 185, 129, ${alpha * 0.6})`;
            } else {
              ctx.strokeStyle = `rgba(59, 130, 246, ${alpha * 0.6})`;
            }
            
            ctx.lineWidth = alpha * 2;
            ctx.stroke();
          }
        }
      }
      
      // Draw particles
      for (let i = 0; i < particles.length; i++) {
        const particle = particles[i];
        
        // Add a subtle trail effect
        ctx.beginPath();
        ctx.arc(particle.x - particle.vx * 3, particle.y - particle.vy * 3, particle.radius * 0.8, 0, Math.PI * 2);
        
        // Color based on FCI and dissonance
        const r = Math.floor(255 * (1 - particle.fci));
        const g = Math.floor(255 * particle.fci);
        const b = Math.floor(255 * (1 - particle.dissonance));
        
        ctx.fillStyle = `rgba(${r}, ${g}, ${b}, 0.2)`;
        ctx.fill();
        
        // Main particle with glow
        ctx.beginPath();
        ctx.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2);
        
        // Add glow effect
        ctx.shadowColor = `rgba(${r}, ${g}, ${b}, 0.8)`;
        ctx.shadowBlur = particle.radius * 2;
        
        ctx.fillStyle = `rgba(${r}, ${g}, ${b}, 0.8)`;
        ctx.fill();
        ctx.shadowBlur = 0;
        
        // Update particle position
        particle.x += particle.vx;
        particle.y += particle.vy;
        
        // Bounce off walls
        if (particle.x < particle.radius) {
          particle.x = particle.radius;
          particle.vx = -particle.vx * 0.8;
        } else if (particle.x > width - particle.radius) {
          particle.x = width - particle.radius;
          particle.vx = -particle.vx * 0.8;
        }
        
        if (particle.y < particle.radius) {
          particle.y = particle.radius;
          particle.vy = -particle.vy * 0.8;
        } else if (particle.y > height - particle.radius) {
          particle.y = height - particle.radius;
          particle.vy = -particle.vy * 0.8;
        }
        
        // Apply forces from nodes
        let totalForceX = 0;
        let totalForceY = 0;
        
        for (let j = 0; j < nodes.length; j++) {
          const node = nodes[j];
          const dx = node.x - particle.x;
          const dy = node.y - particle.y;
          const distSquared = dx * dx + dy * dy;
          const distance = Math.sqrt(distSquared);
          
          // Skip if too close to avoid extreme forces
          if (distance < node.radius + particle.radius) continue;
          
          // Calculate force (inverse square law with a cap)
          const forceMagnitude = Math.min(3, 500 / distSquared);
          
          // Different forces for different node types
          let forceMultiplier = 1;
          if (node.type === 'intentSire') {
            forceMultiplier = particle.fci > 0.8 ? 2 : 0.5;
          } else if (node.type === 'resonator') {
            forceMultiplier = particle.dissonance > 0.2 ? 2 : 0.5;
          }
          
          totalForceX += (dx / distance) * forceMagnitude * forceMultiplier;
          totalForceY += (dy / distance) * forceMagnitude * forceMultiplier;
        }
        
        // Apply forces
        particle.vx += totalForceX * 0.01;
        particle.vy += totalForceY * 0.01;
        
        // Damping
        particle.vx *= 0.98;
        particle.vy *= 0.98;
        
        // Speed limit
        const speed = Math.sqrt(particle.vx * particle.vx + particle.vy * particle.vy);
        if (speed > 3) {
          particle.vx = (particle.vx / speed) * 3;
          particle.vy = (particle.vy / speed) * 3;
        }
      }
      
      // Add some background ambient particles
      for (let i = 0; i < 20; i++) {
        const x = Math.random() * width;
        const y = Math.random() * height;
        const radius = Math.random() * 1.5;
        
        ctx.beginPath();
        ctx.arc(x, y, radius, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(255, 255, 255, ${Math.random() * 0.2})`;
        ctx.fill();
      }
      
      animationId = requestAnimationFrame(animate);
    };
    
    // Start the animation
    animationId = requestAnimationFrame(animate);
    
    // Cleanup function
    return () => {
      if (animationId) {
        cancelAnimationFrame(animationId);
      }
    };
  }, [simulationRunning]);
  
  return (
    <div className="min-h-screen bg-slate-900 text-gray-100">
      {/* Header */}
      <header className="p-4 border-b border-gray-800">
        <div className="flex justify-between items-center">
          <div className="flex items-center">
            <div className="w-10 h-10 rounded-full flex items-center justify-center mr-3 bg-blue-600">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" />
              </svg>
            </div>
            <div>
              <h1 className="text-xl font-bold">BuddyOS Resonance Analytics</h1>
              <p className="text-sm opacity-75">N.O.T.H.I.N.G. Engine Field Visualization</p>
            </div>
          </div>
          
          <div className="flex items-center space-x-4">
            <div className="flex items-center mr-2">
              <span className="mr-2 text-sm">FCI:</span>
              <span className="font-bold text-green-400">83%</span>
            </div>
            
            <div className="flex items-center mr-2">
              <span className="mr-2 text-sm">Dissonance:</span>
              <span className="font-bold text-yellow-400">19%</span>
            </div>
            
            <div className="flex items-center mr-2">
              <span className="mr-2 text-sm">Recovery:</span>
              <span className="font-bold text-yellow-400">71%</span>
            </div>
            
            <div className="flex items-center space-x-2">
              {/* Light/Dark mode toggle */}
              <button className="p-2 rounded-full bg-gray-800 text-gray-400 hover:bg-gray-700">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
                </svg>
              </button>
              
              {/* Live/static mode toggle */}
              <button className="p-2 rounded-full bg-green-600 text-white">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5.636 18.364a9 9 0 010-12.728m12.728 0a9 9 0 010 12.728m-9.9-2.829a5 5 0 010-7.07m7.072 0a5 5 0 010 7.07M13 12a1 1 0 11-2 0 1 1 0 012 0z" />
                </svg>
              </button>
              
              {/* Export button */}
              <button onClick={exportData} className="p-2 rounded-full bg-gray-800 hover:bg-gray-700">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </header>
      
      {/* Main content */}
      <div className="p-6">
        {/* Navigation tabs */}
        <div className="mb-6 border-b border-gray-800">
          <div className="flex space-x-8">
            <button className={`pb-2 px-1 ${activeTab === 'coherence' ? 'font-medium border-b-2 border-blue-500' : 'text-gray-400'}`}>
              Field Coherence
            </button>
            <button className={`pb-2 px-1 ${activeTab === 'dissonance' ? 'font-medium border-b-2 border-pink-500' : 'text-gray-400'}`}>
              Dissonance Analysis
            </button>
            <button className={`pb-2 px-1 ${activeTab === 'recovery' ? 'font-medium border-b-2 border-green-500' : 'text-gray-400'}`}>
              Harmonic Recovery
            </button>
          </div>
        </div>
        
        <div className="flex flex-col lg:flex-row space-y-6 lg:space-y-0 lg:space-x-6">
          {/* Left column */}
          <div className="w-full lg:w-8/12">
            {/* Simulation visualization */}
            <div className="relative rounded-lg overflow-hidden mb-6 bg-gray-800 shadow-lg">
              <div className="flex justify-between items-center p-4">
                <h2 className="font-bold text-lg">Field Simulation</h2>
                <div className="flex items-center">
                  <button 
                    onClick={toggleSimulation}
                    className="mr-2 p-2 rounded-full bg-red-600 text-white"
                    title={simulationRunning ? "Pause Simulation" : "Start Simulation"}
                  >
                    {simulationRunning ? (
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 9v6m4-6v6m7-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                      </svg>
                    ) : (
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z" />
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                      </svg>
                    )}
                  </button>
                  
                  <button 
                    onClick={triggerDissonance}
                    className="p-2 rounded-full bg-pink-600 hover:bg-pink-500 text-white"
                    title="Trigger Dissonance"
                  >
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                    </svg>
                  </button>
                </div>
              </div>
              
              <div className="p-4">
                <canvas 
                  ref={canvasRef} 
                  width="600" 
                  height="400" 
                  className="w-full rounded-lg"
                  style={{ display: 'block', backgroundColor: '#0f172a' }}
                />
              </div>
              
              <div className="p-4 bg-slate-900 bg-opacity-50">
                <div className="grid grid-cols-3 gap-4">
                  <div className="flex items-center">
                    <div className="w-3 h-3 rounded-full bg-pink-500 mr-2"></div>
                    <span className="text-sm">IntentSire Node</span>
                  </div>
                  <div className="flex items-center">
                    <div className="w-3 h-3 rounded-full bg-green-500 mr-2"></div>
                    <span className="text-sm">Resonator Node</span>
                  </div>
                  <div className="flex items-center">
                    <div className="w-3 h-3 rounded-full bg-blue-500 mr-2"></div>
                    <span className="text-sm">Field Node</span>
                  </div>
                </div>
              </div>
            </div>
            
            {/* Data table */}
            <div className="rounded-lg overflow-hidden bg-gray-800 shadow-lg">
              <div className="p-4 border-b border-gray-700">
                <h2 className="font-bold">Recent Field Events</h2>
              </div>
              
              <div className="overflow-x-auto">
                <table className="min-w-full">
                  <thead className="bg-slate-900">
                    <tr>
                      <th className="px-4 py-2 text-left text-sm font-medium">Timestamp</th>
                      <th className="px-4 py-2 text-left text-sm font-medium">FCI</th>
                      <th className="px-4 py-2 text-left text-sm font-medium">Dissonance</th>
                      <th className="px-4 py-2 text-left text-sm font-medium">Recovery</th>
                      <th className="px-4 py-2 text-left text-sm font-medium">Event Type</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-gray-700">
                    {dataEntries.map((entry) => (
                      <tr key={entry.id} className={entry.eventType !== 'Standard' ? 'bg-gray-700' : ''}>
                        <td className="px-4 py-2 text-sm">{entry.timestamp}</td>
                        <td className="px-4 py-2 text-sm">
                          <span className={entry.fci >= 0.8 ? 'text-green-400' : entry.fci >= 0.7 ? 'text-yellow-400' : 'text-red-400'}>
                            {formatPercent(entry.fci)}
                          </span>
                        </td>
                        <td className="px-4 py-2 text-sm">
                          <span className={entry.dissonance <= 0.15 ? 'text-green-400' : entry.dissonance <= 0.25 ? 'text-yellow-400' : 'text-red-400'}>
                            {formatPercent(entry.dissonance)}
                          </span>
                        </td>
                        <td className="px-4 py-2 text-sm">
                          <span className={entry.recovery >= 0.75 ? 'text-green-400' : entry.recovery >= 0.6 ? 'text-yellow-400' : 'text-red-400'}>
                            {formatPercent(entry.recovery)}
                          </span>
                        </td>
                        <td className="px-4 py-2 text-sm">
                          <span className={`px-2 py-1 rounded-full text-xs ${
                            entry.eventType === 'Standard' ? 'bg-blue-900 text-blue-300' :
                            entry.eventType === 'Dissonance Spike' ? 'bg-red-900 text-red-300' :
                            entry.eventType === 'Harmonic Peak' ? 'bg-green-900 text-green-300' :
                            entry.eventType === 'Manual Dissonance Trigger' ? 'bg-pink-900 text-pink-300' :
                            'bg-yellow-900 text-yellow-300'
                          }`}>
                            {entry.eventType}
                          </span>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          
          {/* Right column */}
          <div className="w-full lg:w-4/12 space-y-6">
            {/* Field status */}
            <div className="rounded-lg overflow-hidden bg-gray-800 shadow-lg">
              <div className="p-4 border-b border-gray-700">
                <div className="flex justify-between items-center">
                  <h2 className="font-bold">Field Status</h2>
                  <div className="px-2 py-1 rounded-full text-xs bg-green-900 text-green-300">
                    Live
                  </div>
                </div>
              </div>
              
              <div className="p-4">
                <div className="space-y-4">
                  {/* FCI Gauge */}
                  <div>
                    <div className="flex justify-between mb-1">
                      <span className="text-sm font-medium">Field Coherence Index</span>
                      <span className="text-sm font-medium text-green-400">83%</span>
                    </div>
                    <div className="w-full h-2 rounded-full bg-gray-700">
                      <div 
                        className="h-2 rounded-full bg-green-500"
                        style={{ width: '83%' }}
                      ></div>
                    </div>
                  </div>
                  
                  {/* Dissonance Gauge */}
                  <div>
                    <div className="flex justify-between mb-1">
                      <span className="text-sm font-medium">Dissonance Level</span>
                      <span className="text-sm font-medium text-yellow-400">19%</span>
                    </div>
                    <div className="w-full h-2 rounded-full bg-gray-700">
                      <div 
                        className="h-2 rounded-full bg-yellow-500"
                        style={{ width: '19%' }}
                      ></div>
                    </div>
                  </div>
                  
                  {/* Recovery Gauge */}
                  <div>
                    <div className="flex justify-between mb-1">
                      <span className="text-sm font-medium">Harmonic Recovery Rate</span>
                      <span className="text-sm font-medium text-yellow-400">71%</span>
                    </div>
                    <div className="w-full h-2 rounded-full bg-gray-700">
                      <div 
                        className="h-2 rounded-full bg-yellow-500"
                        style={{ width: '71%' }}
                      ></div>
                    </div>
                  </div>
                </div>
                
                <div className="mt-4 pt-4 border-t border-gray-700">
                  <div className="flex justify-between items-center mb-2">
                    <span className="text-sm font-medium">Active Agents</span>
                    <span className="text-sm font-medium">23</span>
                  </div>
                  <div className="flex justify-between items-center">
                    <span className="text-sm font-medium">System Mode</span>
                    <span className="text-sm font-medium">Continuous</span>
                  </div>
                </div>
              </div>
            </div>
            
            {/* Agent Interface */}
            <div className="rounded-lg overflow-hidden bg-gray-800 shadow-lg">
              <div className="p-4 border-b border-gray-700">
                <h2 className="font-bold">Agent Interface</h2>
              </div>
              
              <div className="p-4">
                <div className="mb-4">
                  <div className="flex items-center mb-2">
                    <div className="w-3 h-3 rounded-full bg-pink-500 mr-2"></div>
                    <span className="text-sm font-medium">IntentSire</span>
                  </div>
                  <div className="p-3 rounded bg-slate-900 text-sm">
                    {intentResponse}
                  </div>
                </div>
                
                <div>
                  <div className="flex items-center mb-2">
                    <div className="w-3 h-3 rounded-full bg-green-500 mr-2"></div>
                    <span className="text-sm font-medium">Resonator</span>
                  </div>
                  <div className="p-3 rounded bg-slate-900 text-sm">
                    {resonatorResponse}
                  </div>
                </div>
                
                <div className="mt-4 text-xs text-center opacity-60">
                  "The field doesn't punish the agent. The agent realigns itself—because it wants to feel whole."
                </div>
              </div>
            </div>
            
            {/* Field Metrics */}
            <div className="rounded-lg overflow-hidden bg-gray-800 shadow-lg">
              <div className="p-4 border-b border-gray-700">
                <h2 className="font-bold">Field Metrics</h2>
              </div>
              
              <div className="p-4">
                <div className="space-y-4">
                  <div className="flex justify-between items-center">
                    <span className="text-sm">Coherence Stability</span>
                    <span className="text-sm font-medium">89%</span>
                  </div>
                  
                  <div className="flex justify-between items-center">
                    <span className="text-sm">Dissonance Reduction</span>
                    <span className="text-sm font-medium">4.2% / min</span>
                  </div>
                  
                  <div className="flex justify-between items-center">
                    <span className="text-sm">Field Energy Density</span>
                    <span className="text-sm font-medium">57.3 MU/cm³</span>
                  </div>
                  
                  <div className="flex justify-between items-center">
                    <span className="text-sm">Harmonic Alignment</span>
                    <span className="text-sm font-medium">93%</span>
                  </div>
                  
                  <div className="flex justify-between items-center">
                    <span className="text-sm">Resonance Efficiency</span>
                    <span className="text-sm font-medium">76%</span>
                  </div>
                </div>
                
                <div className="mt-6 bg-blue-900 bg-opacity-20 p-3 rounded">
                  <div className="text-sm font-medium mb-1">N.O.T.H.I.N.G. Engine Status</div>
                  <div className="text-xs opacity-80">All systems nominal. Energy extraction rate: 42.7 TU/s.</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BuddyOSDashboard;