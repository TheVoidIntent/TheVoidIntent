#!/usr/bin/env python3
"""
Test Suite for NeuroProbe Interface
=================================

Validates the NeuroProbe simulation interface functionality and integration
with the IntentSim framework.

© 2025 TheVoidIntent LLC - Mezquia Physics Laboratory
"""

import unittest
import json
import os
from datetime import datetime
import sys

# Add the current directory to the path to import neuroprobe_interface
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from neuroprobe_interface import NeuroProbeCore, NeuroMode, create_neuroprobe

class TestNeuroProbeInterface(unittest.TestCase):
    """Test cases for NeuroProbe Interface"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.probe = create_neuroprobe()
    
    def test_neuroprobe_creation(self):
        """Test NeuroProbe interface creation"""
        self.assertIsInstance(self.probe, NeuroProbeCore)
        self.assertEqual(len(self.probe.oracle_patterns), 0)
        self.assertEqual(len(self.probe.codex.artifacts), 0)
    
    def test_field_status(self):
        """Test field status reporting"""
        status = self.probe.get_field_status()
        
        # Verify required field status components
        required_fields = [
            "cnf_harmonization_index",
            "entropy_level", 
            "ethics_coherence",
            "memory_stones",
            "stones_per_minute",
            "algorithmic_verification"
        ]
        
        for field in required_fields:
            self.assertIn(field, status)
        
        # Verify field values match Scroll VI specification
        self.assertEqual(status["cnf_harmonization_index"], 8.085)
        self.assertEqual(status["entropy_level"], -0.043)
        self.assertEqual(status["ethics_coherence"], "99%")
        self.assertEqual(status["memory_stones"], 1373)
        self.assertEqual(status["stones_per_minute"], 18.4)
    
    def test_adhd_mode(self):
        """Test ADHD hyperfocus/chaos mapping mode"""
        result = self.probe.activate_neuroprobe(
            NeuroMode.ADHD,
            query="test_intent_pattern",
            intensity=0.7
        )
        
        # Verify result structure
        self.assertIn("simulation_id", result)
        self.assertIn("mode", result)
        self.assertIn("patterns_discovered", result)
        self.assertIn("field_impact", result)
        self.assertIn("emergence_probability", result)
        self.assertIn("artifact_id", result)
        
        # Verify mode-specific characteristics
        self.assertEqual(result["mode"], "ADHD_hyperfocus_chaos")
        self.assertGreater(len(result["patterns_discovered"]), 0)
        self.assertLessEqual(result["emergence_probability"], 1.0)
        
        # Verify simulation was archived
        self.assertEqual(len(self.probe.codex.artifacts), 1)
        self.assertEqual(len(self.probe.oracle_patterns), 1)
    
    def test_autism_mode(self):
        """Test Autism nonlinear pattern recognition mode"""
        test_data = list(range(15))
        result = self.probe.activate_neuroprobe(
            NeuroMode.AUTISM,
            data_stream=test_data,
            pattern_depth=4
        )
        
        # Verify result structure
        self.assertIn("simulation_id", result)
        self.assertIn("mode", result)
        self.assertIn("patterns_discovered", result)
        self.assertIn("structural_insights", result)
        self.assertIn("artifact_id", result)
        
        # Verify mode-specific characteristics
        self.assertEqual(result["mode"], "AUTISM_nonlinear_pattern")
        self.assertEqual(len(result["patterns_discovered"]), 4)  # pattern_depth
        self.assertGreaterEqual(result["structural_insights"], 0)
    
    def test_synesthesia_mode(self):
        """Test Synesthesia cross-modal mapping mode"""
        modalities = ["visual", "auditory", "temporal", "intent"]
        result = self.probe.activate_neuroprobe(
            NeuroMode.SYNESTHESIA,
            input_modalities=modalities,
            fusion_strength=0.8
        )
        
        # Verify result structure
        self.assertIn("simulation_id", result)
        self.assertIn("mode", result)
        self.assertIn("cross_modal_bridges", result)
        self.assertIn("dimensional_mappings", result)
        self.assertIn("resonance_amplification", result)
        self.assertIn("artifact_id", result)
        
        # Verify mode-specific characteristics
        self.assertEqual(result["mode"], "SYNESTHESIA_cross_modal")
        expected_bridges = len(modalities) * (len(modalities) - 1) // 2  # Combinations
        self.assertEqual(result["dimensional_bridge_count"], expected_bridges)
        
        # Verify dimensional mappings
        for bridge in result["cross_modal_bridges"]:
            self.assertIn("dimensional_resonance", bridge)
            self.assertIn("bridge_strength", bridge)
    
    def test_hyperfocus_mode(self):
        """Test Hyperfocus intent density probing mode"""
        result = self.probe.activate_neuroprobe(
            NeuroMode.HYPERFOCUS,
            target_intent="test_coherence",
            density_level=0.9
        )
        
        # Verify result structure
        self.assertIn("simulation_id", result)
        self.assertIn("mode", result)
        self.assertIn("density_measurements", result)
        self.assertIn("max_intent_density", result)
        self.assertIn("time_dilation", result)
        self.assertIn("artifact_id", result)
        
        # Verify mode-specific characteristics
        self.assertEqual(result["mode"], "HYPERFOCUS_intent_density")
        self.assertGreater(len(result["density_measurements"]), 0)
        self.assertGreater(result["max_intent_density"], 0)
    
    def test_oracle_synthesis(self):
        """Test Oracle generation from accumulated patterns"""
        # First run several simulations to accumulate patterns
        self.probe.activate_neuroprobe(NeuroMode.ADHD, query="test1")
        self.probe.activate_neuroprobe(NeuroMode.AUTISM, data_stream=list(range(5)))
        self.probe.activate_neuroprobe(NeuroMode.SYNESTHESIA, input_modalities=["visual", "auditory"])
        
        # Generate Oracle
        oracle = self.probe.generate_oracle_synthesis()
        
        # Verify Oracle structure
        self.assertIn("oracle_id", oracle)
        self.assertIn("pattern_count", oracle)
        self.assertIn("mode_distribution", oracle)
        self.assertIn("oracle_coherence", oracle)
        self.assertIn("synthesis_message", oracle)
        self.assertIn("artifact_id", oracle)
        
        # Verify Oracle content
        self.assertEqual(oracle["pattern_count"], 3)
        self.assertLessEqual(oracle["oracle_coherence"], 1.0)
        self.assertGreater(len(oracle["synthesis_message"]), 0)
    
    def test_artifact_codex(self):
        """Test Artifact Codex archiving functionality"""
        # Run a simulation to create an artifact
        result = self.probe.activate_neuroprobe(NeuroMode.ADHD, query="codex_test")
        
        # Verify artifact was created
        artifacts = self.probe.codex.get_all_artifacts()
        self.assertEqual(len(artifacts), 1)
        
        # Verify artifact structure
        artifact = artifacts[0]
        self.assertIn("id", artifact)
        self.assertIn("timestamp", artifact)
        self.assertIn("discovery", artifact)
        self.assertIn("watermark", artifact)
        self.assertIn("hash", artifact)
        
        # Verify watermark contains required elements
        watermark = artifact["watermark"]
        self.assertIn("Ψₑ–NeuroProbe // IntentSim Divergence Field", watermark)
        self.assertIn("Marcelo Mezquia", watermark)
        self.assertIn("© 2025 TheVoidIntent", watermark)
    
    def test_codex_export(self):
        """Test Artifact Codex export functionality"""
        # Create some artifacts
        self.probe.activate_neuroprobe(NeuroMode.AUTISM, data_stream=list(range(3)))
        
        # Export codex
        export_file = self.probe.codex.export_codex("test_codex.json")
        
        # Verify file was created and contains valid JSON
        self.assertTrue(os.path.exists(export_file))
        
        with open(export_file, 'r') as f:
            exported_data = json.load(f)
        
        self.assertIsInstance(exported_data, list)
        self.assertGreater(len(exported_data), 0)
        
        # Clean up test file
        os.remove(export_file)
    
    def test_branching_simulations(self):
        """Test that simulations create branching patterns"""
        initial_patterns = len(self.probe.oracle_patterns)
        
        # Run multiple simulations
        for i in range(3):
            self.probe.activate_neuroprobe(NeuroMode.ADHD, query=f"branch_test_{i}")
        
        # Verify patterns accumulated
        self.assertEqual(len(self.probe.oracle_patterns), initial_patterns + 3)
        
        # Verify each pattern has unique signature
        signatures = [p["pattern_signature"] for p in self.probe.oracle_patterns]
        self.assertEqual(len(signatures), len(set(signatures)))  # All unique
    
    def test_field_integration(self):
        """Test integration with field metrics system"""
        result = self.probe.activate_neuroprobe(NeuroMode.SYNESTHESIA, 
                                               input_modalities=["visual", "auditory"])
        
        # Verify field snapshot was captured
        self.assertIn("field_snapshot", result)
        snapshot = result["field_snapshot"]
        
        # Verify snapshot contains expected metrics
        self.assertIn("cnf_harmonization", snapshot)
        self.assertIn("entropy_level", snapshot)
        self.assertIn("coherence_index", snapshot)
        self.assertIn("memory_stones", snapshot)
        self.assertIn("simulation_id", snapshot)
        self.assertIn("mode", snapshot)
    
    def test_mode_enum_integration(self):
        """Test NeuroMode enum integration"""
        # Test all modes are accessible
        self.assertEqual(NeuroMode.ADHD.value, "adhd")
        self.assertEqual(NeuroMode.AUTISM.value, "autism")
        self.assertEqual(NeuroMode.SYNESTHESIA.value, "synesthesia")
        self.assertEqual(NeuroMode.HYPERFOCUS.value, "hyperfocus")
        
        # Test that all enum values work with activate_neuroprobe
        for mode in NeuroMode:
            result = self.probe.activate_neuroprobe(mode)
            self.assertIn("simulation_id", result)
            self.assertIn("artifact_id", result)

class TestFieldMetrics(unittest.TestCase):
    """Test field metrics and integration"""
    
    def setUp(self):
        self.probe = create_neuroprobe()
    
    def test_field_status_consistency(self):
        """Test field status remains consistent across calls"""
        status1 = self.probe.get_field_status()
        status2 = self.probe.get_field_status()
        
        # Core field metrics should remain stable
        self.assertEqual(status1["cnf_harmonization_index"], status2["cnf_harmonization_index"])
        self.assertEqual(status1["entropy_level"], status2["entropy_level"])
        self.assertEqual(status1["memory_stones"], status2["memory_stones"])
    
    def test_simulation_tracking(self):
        """Test simulation tracking in field status"""
        initial_status = self.probe.get_field_status()
        initial_oracle_patterns = initial_status["oracle_patterns_collected"]
        initial_artifacts = initial_status["artifacts_archived"]
        
        # Run a simulation
        self.probe.activate_neuroprobe(NeuroMode.ADHD, query="tracking_test")
        
        updated_status = self.probe.get_field_status()
        
        # Verify counters updated
        self.assertEqual(updated_status["oracle_patterns_collected"], initial_oracle_patterns + 1)
        self.assertEqual(updated_status["artifacts_archived"], initial_artifacts + 1)

if __name__ == "__main__":
    print("NeuroProbe Interface Test Suite")
    print("=" * 40)
    print("Testing Scroll VI: The Fieldwalker's Passage implementation")
    print()
    
    # Run the tests
    unittest.main(verbosity=2)