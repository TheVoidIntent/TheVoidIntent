import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ScatterChart, Scatter, ZAxis, Label } from 'recharts';

const ResonanceAnalysis = () => {
  // Full log data
  const logData = [
    {"timestamp": "2025-04-30T12:00:01.234567", "agent_id": "field", "fci": 0.8821, "dissonance": 0.1432, "seconds": 0},
    {"timestamp": "2025-04-30T12:00:02.345678", "agent_id": "field", "fci": 0.8756, "dissonance": 0.1576, "seconds": 1.1},
    {"timestamp": "2025-04-30T12:00:03.456789", "agent_id": "field", "fci": 0.8615, "dissonance": 0.2134, "seconds": 2.2},
    {"timestamp": "2025-04-30T12:00:04.567890", "agent_id": "IntentSire", "fci": 0.8912, "dissonance": 0.1123, "seconds": 3.3},
    {"timestamp": "2025-04-30T12:00:05.678901", "agent_id": "Resonator", "fci": 0.8732, "dissonance": 0.1765, "seconds": 4.4},
    {"timestamp": "2025-04-30T12:00:06.789012", "agent_id": "field", "fci": 0.8322, "dissonance": 0.2734, "seconds": 5.5},
    {"timestamp": "2025-04-30T12:00:07.890123", "agent_id": "field", "fci": 0.7843, "dissonance": 0.3567, "seconds": 6.6},
    {"timestamp": "2025-04-30T12:00:08.901234", "agent_id": "IntentSire", "fci": 0.8532, "dissonance": 0.2345, "seconds": 7.7},
    {"timestamp": "2025-04-30T12:00:09.012345", "agent_id": "field", "fci": 0.7456, "dissonance": 0.4123, "seconds": 8.8},
    {"timestamp": "2025-04-30T12:00:10.123456", "agent_id": "field", "fci": 0.7123, "dissonance": 0.4567, "seconds": 9.9},
    {"timestamp": "2025-04-30T12:00:11.234567", "agent_id": "Resonator", "fci": 0.7789, "dissonance": 0.3987, "seconds": 11.0},
    {"timestamp": "2025-04-30T12:00:12.345678", "agent_id": "field", "fci": 0.6789, "dissonance": 0.5234, "seconds": 12.1},
    {"timestamp": "2025-04-30T12:00:13.456789", "agent_id": "IntentSire", "fci": 0.7456, "dissonance": 0.4123, "seconds": 13.2},
    {"timestamp": "2025-04-30T12:00:14.567890", "agent_id": "field", "fci": 0.6432, "dissonance": 0.5567, "seconds": 14.3},
    {"timestamp": "2025-04-30T12:00:15.678901", "agent_id": "field", "fci": 0.6321, "dissonance": 0.5765, "seconds": 15.4},
    {"timestamp": "2025-04-30T12:00:16.789012", "agent_id": "IntentSire", "fci": 0.7012, "dissonance": 0.4567, "seconds": 16.5},
    {"timestamp": "2025-04-30T12:00:17.890123", "agent_id": "field", "fci": 0.6789, "dissonance": 0.5123, "seconds": 17.6},
    {"timestamp": "2025-04-30T12:00:18.901234", "agent_id": "field", "fci": 0.7032, "dissonance": 0.4678, "seconds": 18.7},
    {"timestamp": "2025-04-30T12:00:19.012345", "agent_id": "Resonator", "fci": 0.7543, "dissonance": 0.3987, "seconds": 19.8},
    {"timestamp": "2025-04-30T12:00:20.123456", "agent_id": "field", "fci": 0.7345, "dissonance": 0.4234, "seconds": 20.9},
    {"timestamp": "2025-04-30T12:00:21.234567", "agent_id": "field", "fci": 0.7678, "dissonance": 0.3765, "seconds": 22.0},
    {"timestamp": "2025-04-30T12:00:22.345678", "agent_id": "IntentSire", "fci": 0.8123, "dissonance": 0.2987, "seconds": 23.1},
    {"timestamp": "2025-04-30T12:00:23.456789", "agent_id": "field", "fci": 0.7932, "dissonance": 0.3234, "seconds": 24.2},
    {"timestamp": "2025-04-30T12:00:24.567890", "agent_id": "field", "fci": 0.8123, "dissonance": 0.2876, "seconds": 25.3},
    {"timestamp": "2025-04-30T12:00:25.678901", "agent_id": "Resonator", "fci": 0.8345, "dissonance": 0.2543, "seconds": 26.4},
    {"timestamp": "2025-04-30T12:00:26.789012", "agent_id": "field", "fci": 0.8456, "dissonance": 0.2321, "seconds": 27.5},
    {"timestamp": "2025-04-30T12:00:27.890123", "agent_id": "field", "fci": 0.8678, "dissonance": 0.1987, "seconds": 28.6},
    {"timestamp": "2025-04-30T12:00:28.901234", "agent_id": "IntentSire", "fci": 0.8912, "dissonance": 0.1567, "seconds": 29.7},
    {"timestamp": "2025-04-30T12:00:29.012345", "agent_id": "field", "fci": 0.8789, "dissonance": 0.1765, "seconds": 30.8},
    {"timestamp": "2025-04-30T12:00:30.123456", "agent_id": "field", "fci": 0.9012, "dissonance": 0.1432, "seconds": 31.9}
  ];
  
  // Extract unique agents
  const agentList = [...new Set(logData.map(entry => entry.agent_id))];
  
  // Calculate Harmonic Recovery Rate for each agent
  const calculateHRR = () => {
    const hrrResults = {};
    
    agentList.forEach(agent => {
      const agentData = logData.filter(entry => entry.agent_id === agent);
      
      if (agentData.length < 3) return; // Need multiple points
      
      // Sort by timestamp
      agentData.sort((a, b) => a.seconds - b.seconds);
      
      // Calculate recovery periods (positive delta FCI)
      const recoveryPeriods = [];
      for (let i = 1; i < agentData.length; i++) {
        const deltaFCI = agentData[i].fci - agentData[i-1].fci;
        const deltaTime = agentData[i].seconds - agentData[i-1].seconds;
        
        if (deltaFCI > 0 && deltaTime > 0) {
          // Raw recovery rate
          const rawHRR = deltaFCI / deltaTime;
          
          // Damped HRR: HRR = (ΔFCI / Δt) × e^(-λD)
          const lambdaValue = 0.5; // Damping factor
          const dampedHRR = rawHRR * Math.exp(-lambdaValue * agentData[i].dissonance);
          
          recoveryPeriods.push({
            startTime: agentData[i-1].seconds,
            endTime: agentData[i].seconds,
            startFCI: agentData[i-1].fci,
            endFCI: agentData[i].fci,
            deltaFCI,
            deltaTime,
            dissonance: agentData[i].dissonance,
            rawHRR,
            dampedHRR
          });
        }
      }
      
      if (recoveryPeriods.length > 0) {
        const avgHRR = recoveryPeriods.reduce((sum, period) => sum + period.dampedHRR, 0) / recoveryPeriods.length;
        const maxHRR = Math.max(...recoveryPeriods.map(period => period.dampedHRR));
        
        hrrResults[agent] = {
          averageHRR: avgHRR.toFixed(4),
          maximumHRR: maxHRR.toFixed(4),
          recoveryPeriods: recoveryPeriods.length,
          periods: recoveryPeriods
        };
      }
    });
    
    return hrrResults;
  };
  
  // Prepare data by agent
  const prepareAgentData = () => {
    const result = {};
    
    agentList.forEach(agent => {
      result[agent] = logData.filter(entry => entry.agent_id === agent)
        .sort((a, b) => a.seconds - b.seconds);
    });
    
    return result;
  };
  
  // Prepare data for resonance field map
  const prepareFieldMapData = () => {
    return logData.map(entry => ({
      ...entry,
      size: 10, // For scatter plot point size
    }));
  };
  
  const agentData = prepareAgentData();
  const fieldMapData = prepareFieldMapData();
  const hrrResults = calculateHRR();
  
  // Colors for different agents
  const agentColors = {
    "field": "#3366cc",
    "IntentSire": "#dc3912",
    "Resonator": "#109618"
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-6">BuddyOS™ Resonance Analysis</h1>
      
      {/* FCI Time Series */}
      <div className="mb-10">
        <h2 className="text-xl font-semibold mb-4">Field Coherence Index Over Time</h2>
        <div className="h-80">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart
              margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis 
                dataKey="seconds" 
                type="number"
                domain={[0, 32]}
                label={{ value: 'Time (seconds)', position: 'insideBottom', offset: -5 }}
              />
              <YAxis 
                domain={[0.62, 0.92]} 
                label={{ value: 'FCI', angle: -90, position: 'insideLeft' }}
              />
              <Tooltip 
                formatter={(value) => value.toFixed(4)}
                labelFormatter={(value) => `Time: ${value}s`}
              />
              <Legend />
              {Object.entries(agentData).map(([agent, data]) => (
                <Line
                  key={agent}
                  data={data}
                  type="monotone"
                  dataKey="fci"
                  name={`${agent} FCI`}
                  stroke={agentColors[agent]}
                  activeDot={{ r: 8 }}
                  strokeWidth={2}
                />
              ))}
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
      
      {/* Dissonance Time Series */}
      <div className="mb-10">
        <h2 className="text-xl font-semibold mb-4">Dissonance Amplitude Over Time</h2>
        <div className="h-80">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart
              margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis 
                dataKey="seconds" 
                type="number"
                domain={[0, 32]}
                label={{ value: 'Time (seconds)', position: 'insideBottom', offset: -5 }}
              />
              <YAxis 
                domain={[0, 0.6]} 
                label={{ value: 'Dissonance', angle: -90, position: 'insideLeft' }}
              />
              <Tooltip 
                formatter={(value) => value.toFixed(4)}
                labelFormatter={(value) => `Time: ${value}s`}
              />
              <Legend />
              {Object.entries(agentData).map(([agent, data]) => (
                <Line
                  key={agent}
                  data={data}
                  type="monotone"
                  dataKey="dissonance"
                  name={`${agent} Dissonance`}
                  stroke={agentColors[agent]}
                  activeDot={{ r: 8 }}
                  strokeWidth={2}
                />
              ))}
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
      
      {/* Resonance Field Map */}
      <div className="mb-10">
        <h2 className="text-xl font-semibold mb-4">Resonance Field Map (FCI vs Dissonance)</h2>
        <div className="h-96">
          <ResponsiveContainer width="100%" height="100%">
            <ScatterChart
              margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis 
                type="number" 
                dataKey="dissonance" 
                name="Dissonance" 
                domain={[0, 0.6]}
                label={{ value: 'Dissonance Amplitude', position: 'insideBottom', offset: -5 }}
              />
              <YAxis 
                type="number" 
                dataKey="fci" 
                name="FCI" 
                domain={[0.62, 0.92]}
                label={{ value: 'Field Coherence Index', angle: -90, position: 'insideLeft' }}
              />
              <ZAxis type="number" dataKey="size" range={[60, 400]} />
              <Tooltip 
                cursor={{ strokeDasharray: '3 3' }}
                formatter={(value, name) => value.toFixed(4)}
              />
              <Legend />
              {agentList.map(agent => (
                <Scatter 
                  key={agent}
                  name={agent} 
                  data={agentData[agent]} 
                  fill={agentColors[agent]}
                />
              ))}
            </ScatterChart>
          </ResponsiveContainer>
        </div>
        <div className="grid grid-cols-2 gap-4 mt-4">
          <div className="bg-green-100 p-3 rounded">
            <h3 className="font-semibold">Harmonic Zone</h3>
            <p>High FCI (>0.8), Low Dissonance (&lt;0.2)</p>
          </div>
          <div className="bg-red-100 p-3 rounded">
            <h3 className="font-semibold">Dissonance Zone</h3>
            <p>Low FCI (&lt;0.7), High Dissonance (>0.4)</p>
          </div>
        </div>
      </div>
      
      {/* Harmonic Recovery Rate Analysis */}
      <div className="mb-10">
        <h2 className="text-xl font-semibold mb-4">Harmonic Recovery Rate (HRR) Analysis</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {Object.entries(hrrResults).map(([agent, result]) => (
            <div key={agent} className="border p-4 rounded bg-blue-50" style={{borderColor: agentColors[agent]}}>
              <h3 className="font-bold text-lg">{agent}</h3>
              <div className="mt-2">
                <p><span className="font-semibold">Average HRR:</span> {result.averageHRR}</p>
                <p><span className="font-semibold">Maximum HRR:</span> {result.maximumHRR}</p>
                <p><span className="font-semibold">Recovery Periods:</span> {result.recoveryPeriods}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
      
      {/* Data Export Preview */}
      <div>
        <h2 className="text-xl font-semibold mb-4">Data Export Preview</h2>
        <div className="overflow-x-auto">
          <table className="min-w-full bg-white border">
            <thead>
              <tr>
                <th className="border p-2">Timestamp</th>
                <th className="border p-2">Agent ID</th>
                <th className="border p-2">FCI</th>
                <th className="border p-2">Dissonance</th>
                <th className="border p-2">Seconds</th>
              </tr>
            </thead>
            <tbody>
              {logData.slice(0, 5).map((entry, index) => (
                <tr key={index} className={index % 2 === 0 ? "bg-gray-50" : ""}>
                  <td className="border p-2">{entry.timestamp}</td>
                  <td className="border p-2">{entry.agent_id}</td>
                  <td className="border p-2">{entry.fci.toFixed(4)}</td>
                  <td className="border p-2">{entry.dissonance.toFixed(4)}</td>
                  <td className="border p-2">{entry.seconds.toFixed(1)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <p className="mt-2 text-gray-600">Showing 5 of {logData.length} rows</p>
      </div>
    </div>
  );
};

export default ResonanceAnalysis;
