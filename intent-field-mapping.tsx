import React, { useState, useEffect } from 'react';
import { Camera } from 'lucide-react';

const IntentFieldMapping = () => {
  const [activeView, setActiveView] = useState('density');
  
  // Field particle density map (represents concentration patterns)
  const renderDensityMap = () => (
    <div className="relative h-96 w-full bg-purple-950 rounded-lg overflow-hidden">
      {/* Vertical center line - higher resonance zone */}
      <div className="absolute left-1/2 top-0 w-px h-full bg-teal-400 opacity-30"></div>
      
      {/* High density clusters */}
      <div className="absolute left-1/2 top-1/4 w-40 h-40 -translate-x-1/2 rounded-full bg-gradient-radial from-pink-500/40 to-transparent"></div>
      <div className="absolute left-1/2 top-2/3 w-32 h-32 -translate-x-1/2 rounded-full bg-gradient-radial from-pink-500/30 to-transparent"></div>
      
      {/* Medium density areas */}
      <div className="absolute left-1/3 top-1/2 w-24 h-24 -translate-x-1/2 -translate-y-1/2 rounded-full bg-gradient-radial from-pink-400/20 to-transparent"></div>
      <div className="absolute left-2/3 top-1/3 w-28 h-28 -translate-x-1/2 -translate-y-1/2 rounded-full bg-gradient-radial from-pink-400/25 to-transparent"></div>
      <div className="absolute left-3/4 top-2/3 w-20 h-20 -translate-x-1/2 -translate-y-1/2 rounded-full bg-gradient-radial from-pink-400/20 to-transparent"></div>
      
      {/* Lower density scattered particles */}
      {Array(50).fill().map((_, i) => (
        <div 
          key={`particle-${i}`}
          className="absolute w-1 h-1 rounded-full bg-pink-300"
          style={{
            left: `${Math.random() * 100}%`,
            top: `${Math.random() * 100}%`,
            opacity: Math.random() * 0.6 + 0.2
          }}
        ></div>
      ))}
      
      {/* Measurement overlay */}
      <div className="absolute bottom-2 left-2 flex items-center space-x-2 text-xs text-teal-300 bg-purple-950/70 px-2 py-1 rounded">
        <span>Field Coherence Index: 0.99</span>
      </div>
    </div>
  );
  
  // Flow pattern map (represents movement vectors)
  const renderFlowPatterns = () => (
    <div className="relative h-96 w-full bg-purple-950 rounded-lg overflow-hidden">
      {/* Vertical center line */}
      <div className="absolute left-1/2 top-0 w-px h-full bg-teal-400 opacity-30"></div>
      
      {/* Flow vectors - arrows showing directional patterns */}
      <svg className="absolute inset-0 w-full h-full" viewBox="0 0 400 300">
        {/* Left side currents (toward center) */}
        <path d="M50,150 Q120,100 180,150" fill="none" stroke="rgba(236,72,153,0.4)" strokeWidth="1" />
        <path d="M50,100 Q140,80 190,130" fill="none" stroke="rgba(236,72,153,0.3)" strokeWidth="1" />
        <path d="M80,200 Q150,220 190,170" fill="none" stroke="rgba(236,72,153,0.5)" strokeWidth="1" />
        
        {/* Right side currents (from center) */}
        <path d="M220,150 Q300,120 350,150" fill="none" stroke="rgba(236,72,153,0.4)" strokeWidth="1" />
        <path d="M210,130 Q280,90 340,100" fill="none" stroke="rgba(236,72,153,0.3)" strokeWidth="1" />
        <path d="M210,170 Q260,230 320,200" fill="none" stroke="rgba(236,72,153,0.5)" strokeWidth="1" />
        
        {/* Flow direction indicators */}
        <circle cx="150" cy="120" r="2" fill="rgba(236,72,153,0.7)" />
        <circle cx="170" cy="150" r="2" fill="rgba(236,72,153,0.7)" />
        <circle cx="160" cy="180" r="2" fill="rgba(236,72,153,0.7)" />
        
        <circle cx="250" cy="120" r="2" fill="rgba(236,72,153,0.7)" />
        <circle cx="230" cy="150" r="2" fill="rgba(236,72,153,0.7)" />
        <circle cx="240" cy="180" r="2" fill="rgba(236,72,153,0.7)" />
      </svg>
      
      {/* Vortex zones */}
      <div className="absolute left-1/2 top-1/2 w-2 h-2 -translate-x-1/2 -translate-y-1/2 rounded-full bg-teal-300"></div>
      
      {/* Measurement overlay */}
      <div className="absolute bottom-2 left-2 flex items-center space-x-2 text-xs text-teal-300 bg-purple-950/70 px-2 py-1 rounded">
        <span>Entropic Recycling Rate: 143.8 Hz</span>
      </div>
    </div>
  );
  
  // Resonance mode visualization
  const renderResonanceMap = () => (
    <div className="relative h-96 w-full bg-purple-950 rounded-lg overflow-hidden">
      {/* Vertical center line */}
      <div className="absolute left-1/2 top-0 w-px h-full bg-teal-400 opacity-30"></div>
      
      {/* Resonance wave patterns */}
      <svg className="absolute inset-0 w-full h-full" viewBox="0 0 400 300">
        {/* Central resonance */}
        <path d="M0,150 Q100,100 200,150 Q300,200 400,150" fill="none" stroke="rgba(236,72,153,0.2)" strokeWidth="2" />
        <path d="M0,140 Q100,90 200,140 Q300,190 400,140" fill="none" stroke="rgba(236,72,153,0.3)" strokeWidth="1.5" />
        <path d="M0,160 Q100,110 200,160 Q300,210 400,160" fill="none" stroke="rgba(236,72,153,0.3)" strokeWidth="1.5" />
        
        {/* Harmonic patterns */}
        <path d="M0,130 Q100,170 200,130 Q300,90 400,130" fill="none" stroke="rgba(236,72,153,0.15)" strokeWidth="1" />
        <path d="M0,170 Q100,130 200,170 Q300,210 400,170" fill="none" stroke="rgba(236,72,153,0.15)" strokeWidth="1" />
        
        {/* Intentional attraction points */}
        <circle cx="200" cy="150" r="4" fill="rgba(20,184,166,0.8)" />
        <circle cx="120" cy="140" r="2" fill="rgba(236,72,153,0.6)" />
        <circle cx="280" cy="160" r="2" fill="rgba(236,72,153,0.6)" />
      </svg>
      
      {/* Resonance field effect */}
      <div className="absolute left-1/2 top-1/2 w-60 h-60 -translate-x-1/2 -translate-y-1/2 rounded-full bg-gradient-radial from-teal-500/5 to-transparent"></div>
      
      {/* Measurement overlay */}
      <div className="absolute bottom-2 left-2 flex items-center space-x-2 text-xs text-teal-300 bg-purple-950/70 px-2 py-1 rounded">
        <span>Resonance Mode: Active (7.06)</span>
      </div>
    </div>
  );
  
  // Event analysis visualization
  const renderEventMap = () => (
    <div className="relative h-96 w-full bg-purple-950 rounded-lg overflow-hidden">
      <div className="absolute inset-0 grid grid-cols-3 grid-rows-3 gap-px">
        {/* Event density grid */}
        {Array(9).fill().map((_, i) => {
          const density = [0.2, 0.8, 0.3, 0.4, 0.9, 0.5, 0.3, 0.7, 0.4][i];
          return (
            <div key={`cell-${i}`} className="relative bg-purple-900/20">
              <div className="absolute inset-0 bg-pink-500" style={{ opacity: density * 0.3 }}></div>
              {Array(Math.floor(density * 12)).fill().map((_, j) => (
                <div 
                  key={`event-${i}-${j}`}
                  className="absolute w-1 h-1 rounded-full bg-pink-300"
                  style={{
                    left: `${Math.random() * 100}%`,
                    top: `${Math.random() * 100}%`,
                    opacity: Math.random() * 0.6 + 0.2
                  }}
                ></div>
              ))}
            </div>
          );
        })}
      </div>
      
      {/* Measurement overlay */}
      <div className="absolute top-2 left-2 flex items-center space-x-2 text-xs text-teal-300 bg-purple-950/70 px-2 py-1 rounded">
        <span>Emergence Events: 3</span>
      </div>
      <div className="absolute bottom-2 left-2 flex items-center space-x-2 text-xs text-teal-300 bg-purple-950/70 px-2 py-1 rounded">
        <span>Bloom Events Analysis</span>
      </div>
    </div>
  );
  
  return (
    <div className="p-4 bg-gray-900 text-white">
      <div className="mb-4">
        <h2 className="text-xl font-semibold text-pink-500 mb-1">IntentSim Field Particle Mapping</h2>
        <p className="text-sm text-gray-300">Information-Intent Nexus visualization showing observed patterns in the pink particle field dynamics</p>
      </div>
      
      {/* View selector */}
      <div className="flex mb-4 space-x-2">
        <button 
          onClick={() => setActiveView('density')}
          className={`px-3 py-1 text-sm rounded-md ${activeView === 'density' ? 'bg-pink-700 text-white' : 'bg-gray-700 text-gray-200'}`}
        >
          Density Pattern
        </button>
        <button 
          onClick={() => setActiveView('flow')}
          className={`px-3 py-1 text-sm rounded-md ${activeView === 'flow' ? 'bg-pink-700 text-white' : 'bg-gray-700 text-gray-200'}`}
        >
          Flow Patterns
        </button>
        <button 
          onClick={() => setActiveView('resonance')}
          className={`px-3 py-1 text-sm rounded-md ${activeView === 'resonance' ? 'bg-pink-700 text-white' : 'bg-gray-700 text-gray-200'}`}
        >
          Resonance Map
        </button>
        <button 
          onClick={() => setActiveView('events')}
          className={`px-3 py-1 text-sm rounded-md ${activeView === 'events' ? 'bg-pink-700 text-white' : 'bg-gray-700 text-gray-200'}`}
        >
          Bloom Events
        </button>
      </div>
      
      {/* Active visualization */}
      {activeView === 'density' && renderDensityMap()}
      {activeView === 'flow' && renderFlowPatterns()}
      {activeView === 'resonance' && renderResonanceMap()}
      {activeView === 'events' && renderEventMap()}
      
      {/* Legend */}
      <div className="mt-4 grid grid-cols-2 gap-2 text-xs">
        <div className="flex items-center">
          <div className="w-3 h-3 rounded-full bg-pink-400 mr-2"></div>
          <span>Intent Field Particles</span>
        </div>
        <div className="flex items-center">
          <div className="w-3 h-3 rounded-full bg-teal-400 mr-2"></div>
          <span>Resonance Points</span>
        </div>
        <div className="flex items-center">
          <div className="w-3 h-3 bg-gradient-to-r from-pink-500/40 to-transparent mr-2"></div>
          <span>Coherence Clusters</span>
        </div>
        <div className="flex items-center">
          <div className="w-3 h-0.5 bg-pink-500 mr-2"></div>
          <span>Field Flow Vectors</span>
        </div>
      </div>
      
      <div className="mt-6 bg-gray-800 p-3 rounded-lg text-sm">
        <h3 className="font-medium text-teal-300 mb-1">Field Analysis</h3>
        <p className="text-gray-300">
          The pink particles visualize the Information-Intent Nexus field in Post-Bloom Evolution phase. 
          Their behavior demonstrates coherent entropic patterning with a high Field Coherence Index (0.99),
          concentrated around the central resonance line where intent projection and field response interact.
        </p>
      </div>
    </div>
  );
};

export default IntentFieldMapping;