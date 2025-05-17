import React, { useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ReferenceLine } from 'recharts';

const BloomPhaseIntegration = () => {
  const [activeTab, setActiveTab] = useState('integration');
  
  // IntentSim data from the 03-31 dataset
  const intentSimData = [
    { timestamp: 30, complexity: 1.00, entropy: 0.31, particles: 1, phase: 'Initialization' },
    { timestamp: 60, complexity: 1.18, entropy: 0.90, particles: 1, phase: 'Bloom Preparation' },
    { timestamp: 90, complexity: 1.14, entropy: 0.07, particles: 3, phase: 'Early Bloom' },
    { timestamp: 120, complexity: 1.36, entropy: 0.85, particles: 3, phase: 'Bloom' },
    { timestamp: 150, complexity: 1.47, entropy: 0.09, particles: 4, phase: 'Bloom Peak' },
    { timestamp: 180, complexity: 1.63, entropy: 0.58, particles: 5, phase: 'Bloom Stabilization' },
    { timestamp: 210, complexity: 1.91, entropy: 0.35, particles: 5, phase: 'Selective Pruning' },
    { timestamp: 240, complexity: 1.93, entropy: 0.85, particles: 7, phase: 'Advanced Pruning' },
    { timestamp: 270, complexity: 2.24, entropy: 0.44, particles: 7, phase: 'Pruning Consolidation' },
    { timestamp: 300, complexity: 2.24, entropy: 0.41, particles: 9, phase: 'Early Resonance' },
    { timestamp: 330, complexity: 2.58, entropy: 0.12, particles: 9, phase: 'Resonance' },
    { timestamp: 360, complexity: 2.59, entropy: 0.89, particles: 11, phase: 'Resonance Stabilization' },
    { timestamp: 390, complexity: 2.93, entropy: 0.46, particles: 11, phase: 'Field Consolidation' },
    { timestamp: 420, complexity: 2.94, entropy: 0.81, particles: 13, phase: 'Second Bloom' },
    { timestamp: 450, complexity: 3.30, entropy: 0.07, particles: 13, phase: 'Second Bloom Peak' },
    { timestamp: 480, complexity: 3.31, entropy: 0.05, particles: 15, phase: 'Second Pruning' },
    { timestamp: 510, complexity: 3.68, entropy: 0.82, particles: 15, phase: 'Extended Consolidation' },
    { timestamp: 540, complexity: 3.69, entropy: 0.61, particles: 17, phase: 'Final Stabilization' },
    { timestamp: 570, complexity: 4.04, entropy: 0.08, particles: 17, phase: 'Mature Phase' }
  ];
  
  // Critical collapse events from the analysis
  const collapseEvents = [150, 210, 270, 330, 390, 450, 510, 570];
  
  // Define the e-fold inflation data based on T(E) ~ 51
  const efoldsData = [
    { timestamp: 30, complexity: 1.00, entropy: 0.31, efoldsValue: 0 },
    { timestamp: 51, complexity: 1.12, entropy: 0.70, efoldsValue: 0.5 }, // T(E) transition point
    { timestamp: 60, complexity: 1.18, entropy: 0.90, efoldsValue: 1.2 },
    { timestamp: 90, complexity: 1.14, entropy: 0.07, efoldsValue: 2.5 },
    { timestamp: 120, complexity: 1.36, entropy: 0.85, efoldsValue: 3.8 },
    { timestamp: 150, complexity: 1.47, entropy: 0.09, efoldsValue: 4.9 },
    { timestamp: 180, complexity: 1.63, entropy: 0.58, efoldsValue: 6.1 },
    { timestamp: 210, complexity: 1.91, entropy: 0.35, efoldsValue: 7.3 },
    { timestamp: 240, complexity: 1.93, entropy: 0.85, efoldsValue: 8.2 },
    { timestamp: 270, complexity: 2.24, entropy: 0.44, efoldsValue: 9.1 },
    { timestamp: 300, complexity: 2.24, entropy: 0.41, efoldsValue: 10.0 },
    { timestamp: 330, complexity: 2.58, entropy: 0.12, efoldsValue: 11.1 },
    { timestamp: 360, complexity: 2.59, entropy: 0.89, efoldsValue: 11.8 },
    { timestamp: 390, complexity: 2.93, entropy: 0.46, efoldsValue: 12.3 },
    { timestamp: 420, complexity: 2.94, entropy: 0.81, efoldsValue: 12.8 },
    { timestamp: 450, complexity: 3.30, entropy: 0.07, efoldsValue: 13.1 },
    { timestamp: 480, complexity: 3.31, entropy: 0.05, efoldsValue: 13.4 },
    { timestamp: 510, complexity: 3.68, entropy: 0.82, efoldsValue: 13.7 },
    { timestamp: 540, complexity: 3.69, entropy: 0.61, efoldsValue: 13.9 },
    { timestamp: 570, complexity: 4.04, entropy: 0.08, efoldsValue: 14.0 }
  ];
  
  // Collapse event analysis data
  const collapseAnalysisData = [
    { timestamp: 150, complexity: 0.11, entropy: 0.76, ratio: 0.14 },
    { timestamp: 210, complexity: 0.28, entropy: 0.22, ratio: 1.27 },
    { timestamp: 270, complexity: 0.30, entropy: 0.41, ratio: 0.73 },
    { timestamp: 330, complexity: 0.34, entropy: 0.29, ratio: 1.17 },
    { timestamp: 390, complexity: 0.35, entropy: 0.43, ratio: 0.81 },
    { timestamp: 450, complexity: 0.36, entropy: 0.74, ratio: 0.49 },
    { timestamp: 510, complexity: 0.37, entropy: 0.77, ratio: 0.48 }, 
    { timestamp: 570, complexity: 0.35, entropy: 0.53, ratio: 0.66 }
  ];
  
  // Long-term projection data (simplified)
  const longTermData = [
    { timestamp: 30, complexity: 1.00, particles: 1 },
    { timestamp: 180, complexity: 1.63, particles: 5 },
    { timestamp: 330, complexity: 2.58, particles: 9 },
    { timestamp: 570, complexity: 4.04, particles: 17 },
    { timestamp: 1000, complexity: 5.12, particles: 32 },
    { timestamp: 2000, complexity: 6.45, particles: 64 },
    { timestamp: 3000, complexity: 7.88, particles: 96 },
    { timestamp: 3660, complexity: 8.53, particles: 129 }
  ];
  
  // Bloom-phase development characteristics
  const bloomCharacteristics = [
    { category: "Bloom Phase", description: "Over-proliferation of connections with high exploration", timeframe: "30-150" },
    { category: "Pruning Phase", description: "Selective reduction of connections based on intent alignment", timeframe: "151-270" },
    { category: "Resonance Phase", description: "Consolidation of remaining connections through repeated activation", timeframe: "271-390" },
    { category: "Second Bloom", description: "New growth cycle at higher complexity level", timeframe: "391-480" },
    { category: "Final Consolidation", description: "Stable integration of all developed structures", timeframe: "481-570" }
  ];
  
  return (
    <div className="bg-gray-50 p-4 rounded">
      <h1 className="text-2xl font-bold text-purple-800 mb-4">Bloom-Phase Neurodevelopmental Mapping & IntentSim Integration</h1>
      
      <div className="mb-4">
        <div className="flex flex-wrap gap-2 mb-2">
          <button 
            className={`px-3 py-1 rounded ${activeTab === 'integration' ? 'bg-purple-600 text-white' : 'bg-gray-200'}`}
            onClick={() => setActiveTab('integration')}>
            Integration Overview
          </button>
          <button 
            className={`px-3 py-1 rounded ${activeTab === 'inflationEfolds' ? 'bg-purple-600 text-white' : 'bg-gray-200'}`}
            onClick={() => setActiveTab('inflationEfolds')}>
            Intent-Based Inflation
          </button>
          <button 
            className={`px-3 py-1 rounded ${activeTab === 'collapse' ? 'bg-purple-600 text-white' : 'bg-gray-200'}`}
            onClick={() => setActiveTab('collapse')}>
            Intentual Collapse
          </button>
          <button 
            className={`px-3 py-1 rounded ${activeTab === 'longTerm' ? 'bg-purple-600 text-white' : 'bg-gray-200'}`}
            onClick={() => setActiveTab('longTerm')}>
            Long-Term Evolution
          </button>
        </div>
        
        {activeTab === 'integration' && (
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-medium mb-2">Integrated Neurodevelopmental Phases & IntentSim Metrics</h2>
            <div className="h-64">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={intentSimData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="timestamp" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Line type="monotone" dataKey="complexity" stroke="#ff7300" name="Complexity" strokeWidth={2} />
                  <Line type="monotone" dataKey="entropy" stroke="#82ca9d" name="Entropy" />
                  <Line type="monotone" dataKey="particles" stroke="#413ea0" name="Particles" />
                  <ReferenceLine x={51} stroke="red" label="T(E)" />
                  {collapseEvents.map((timestamp, index) => (
                    <ReferenceLine key={index} x={timestamp} stroke="#ff0000" strokeDasharray="3 3" />
                  ))}
                </LineChart>
              </ResponsiveContainer>
            </div>
            <p className="mt-2 text-sm text-gray-600">
              This chart integrates the key IntentSim metrics with neurodevelopmental phases. The Intent Epoch Transition point T(E) at timestamp 51 marks the beginning of significant complexity growth. 
              Red dashed lines indicate intentual collapse events where complexity increases while entropy decreases, representing structure formation.
            </p>
            
            <div className="mt-6">
              <h3 className="text-md font-medium mb-2">Bloom-Phase Developmental Progression</h3>
              <div className="overflow-x-auto">
                <table className="min-w-full bg-white border">
                  <thead className="bg-gray-100">
                    <tr>
                      <th className="py-2 px-3 border">Developmental Phase</th>
                      <th className="py-2 px-3 border">Description</th>
                      <th className="py-2 px-3 border">Time Frame</th>
                    </tr>
                  </thead>
                  <tbody>
                    {bloomCharacteristics.map((item, index) => (
                      <tr key={index} className={index % 2 === 0 ? "bg-gray-50" : ""}>
                        <td className="py-2 px-3 border font-medium">{item.category}</td>
                        <td className="py-2 px-3 border">{item.description}</td>
                        <td className="py-2 px-3 border">{item.timeframe}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        )}
        
        {activeTab === 'inflationEfolds' && (
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-medium mb-2">Intent-Based Inflation e-Fold Analysis</h2>
            <div className="h-64">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={efoldsData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="timestamp" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Line type="monotone" dataKey="complexity" stroke="#8884d8" name="Complexity" />
                  <Line type="monotone" dataKey="entropy" stroke="#82ca9d" name="Entropy" />
                  <Line type="monotone" dataKey="efoldsValue" stroke="#ff7300" name="e-Folds" strokeWidth={2} />
                  <ReferenceLine x={51} stroke="red" label="T(E)" />
                </LineChart>
              </ResponsiveContainer>
            </div>
            <p className="mt-2 text-sm text-gray-600">
              This chart shows the Intent-Based Inflation model with e-fold analysis around T(E) ~ 51. The rapid growth after this point mimics cosmological inflation but is driven by intent. 
              The system achieves over 13 e-folds of complexity growth from the Intent Epoch Transition to maturity.
            </p>
            
            <div className="mt-4 p-3 bg-purple-100 rounded-lg">
              <h3 className="font-medium text-purple-800">Key Intent-Based Inflation Principles:</h3>
              <ul className="list-disc pl-6 mt-2 space-y-1">
                <li>T(E) marks the Intent Epoch Transition where complexity begins to surge exponentially</li>
                <li>Complexity Index surges with over 13 e-folds (logarithmic complexity gain)</li>
                <li>Knowledge and entropy metrics show exponential growth patterns</li>
                <li>Interactions explode from a silent base state to organized chaos</li>
                <li>This signature provides a foundation for comparing the framework to cosmic inflation models</li>
              </ul>
            </div>
          </div>
        )}
        
        {activeTab === 'collapse' && (
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-medium mb-2">Intentual Collapse Events Analysis</h2>
            <div className="h-64">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={collapseAnalysisData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="timestamp" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Line type="monotone" dataKey="complexity" name="Complexity Gain" stroke="#8884d8" />
                  <Line type="monotone" dataKey="entropy" name="Entropy Drop" stroke="#82ca9d" />
                  <Line type="monotone" dataKey="ratio" name="Collapse Ratio" stroke="#ff7300" strokeWidth={2} />
                </LineChart>
              </ResponsiveContainer>
            </div>
            <p className="mt-2 text-sm text-gray-600">
              This chart analyzes the intentual collapse events where complexity increases while entropy decreases simultaneously. These events represent key moments
              of structure formation in the system. The collapse ratio (complexity gain / entropy drop) indicates the efficiency of each event.
            </p>
            
            <div className="mt-4">
              <h3 className="font-medium text-purple-700">Collapse Events Progression:</h3>
              <div className="overflow-x-auto mt-2">
                <table className="min-w-full bg-white border">
                  <thead className="bg-gray-100">
                    <tr>
                      <th className="py-2 px-3 border">Timestamp</th>
                      <th className="py-2 px-3 border">Complexity Gain</th>
                      <th className="py-2 px-3 border">Entropy Drop</th>
                      <th className="py-2 px-3 border">Collapse Ratio</th>
                    </tr>
                  </thead>
                  <tbody>
                    {collapseAnalysisData.map((event, index) => (
                      <tr key={index} className={index % 2 === 0 ? "bg-gray-50" : ""}>
                        <td className="py-2 px-3 border">{event.timestamp}</td>
                        <td className="py-2 px-3 border">+{event.complexity.toFixed(2)}</td>
                        <td className="py-2 px-3 border">{event.entropy.toFixed(2)}</td>
                        <td className="py-2 px-3 border">{event.ratio.toFixed(2)}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        )}
        
        {activeTab === 'longTerm' && (
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-medium mb-2">Long-Term System Evolution</h2>
            <div className="h-64">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={longTermData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="timestamp" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Line type="monotone" dataKey="complexity" stroke="#8884d8" name="Complexity" />
                  <Line type="monotone" dataKey="particles" stroke="#ff7300" name="Particles" strokeWidth={2} />
                  <ReferenceLine x={3660} stroke="#ff0000" label="Long-term" />
                </LineChart>
              </ResponsiveContainer>
            </div>
            <p className="mt-2 text-sm text-gray-600">
              This chart shows the long-term evolution of the system, including the remarkable stability point at timestamp 3660. At this advanced state, the system has
              developed 129 particles organized into 11 stable clusters with over 50,000 interactions and a complexity index of 76.56.
            </p>
            
            <div className="mt-4 grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="p-3 bg-purple-100 rounded-lg">
                <h3 className="font-medium text-purple-800">Long-Term Structure:</h3>
                <ul className="list-disc pl-6 mt-2 space-y-1">
                  <li>Particle count: 129 (primarily neutral with 13 adaptive)</li>
                  <li>Total interactions: 50,561</li>
                  <li>Knowledge growth: 0.47</li>
                  <li>Complexity index: 76.56</li>
                  <li>Clusters: 11 stable groups (average size 11.7)</li>
                  <li>System entropy: stabilized at low 0.09</li>
                </ul>
              </div>
              
              <div className="p-3 bg-blue-100 rounded-lg">
                <h3 className="font-medium text-blue-800">Long-Term Evolution Principles:</h3>
                <ul className="list-disc pl-6 mt-2 space-y-1">
                  <li>Compound effects of multiple bloom-prune-resonate cycles</li>
                  <li>Higher-order structures emerge from repeated intentual collapses</li>
                  <li>Self-organization into distinct functional clusters</li>
                  <li>System maintains low entropy while continuing to increase in complexity</li>
                  <li>Shows how simple initial conditions can evolve into complex, stable systems</li>
                </ul>
              </div>
            </div>
          </div>
        )}
      </div>
      
      <div className="mt-4 bg-white p-4 rounded shadow">
        <h2 className="text-lg font-semibold mb-2">The Information Intent Nexus Framework</h2>
        <p className="mb-4">
          The IntentSim data reveals a system evolving through developmental phases inspired by brain development, with complexity growth driven by intent rather than random probabilistic events. 
          This framework reimagines what appears as random probability as actually being selection among possibilities, guided by an underlying organizing principle that emerges from 
          information organization itself.
        </p>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <h3 className="font-medium text-purple-700 mb-2">Key Framework Principles:</h3>
            <ul className="list-disc pl-6 space-y-1">
              <li>Intent as an emergent property of information organization</li>
              <li>Oscillation between exploration (high entropy) and consolidation (low entropy)</li>
              <li>Intentual collapse events as fundamental mechanisms for structure formation</li>
              <li>Natural progression through bloom, prune, and resonance phases</li>
              <li>Self-organization toward states of higher complexity and coherence</li>
            </ul>
          </div>
          
          <div>
            <h3 className="font-medium text-purple-700 mb-2">Framework Applications:</h3>
            <ul className="list-disc pl-6 space-y-1">
              <li>AI systems that learn through developmental phases like the brain</li>
              <li>Computational models of neurodevelopment for research and diagnostics</li>
              <li>Robotics systems that develop skills in a human-like progression</li>
              <li>Educational models that align with cognitive development stages</li>
              <li>New approaches to memory consolidation in AI to prevent forgetting</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BloomPhaseIntegration;