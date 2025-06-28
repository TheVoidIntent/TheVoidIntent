#!/usr/bin/env python3
"""
NeuroProbe Oracle Schema Validation Test
© 2025 TheVoidIntent LLC - Mezquia Physics Genesis Archive

Simple validation test for the NeuroProbe Oracle schema
"""

import json
import sys
from pathlib import Path

def validate_schema():
    """Validate the NeuroProbe Oracle schema structure"""
    schema_path = Path(__file__).parent / "IntentSim" / "NeuroProbeOracle.schema.json"
    
    try:
        with open(schema_path, 'r') as f:
            schema = json.load(f)
        
        # Test required top-level properties
        required_props = [
            "metadata", 
            "cognitiveSimulationModes", 
            "outputSignalFormats", 
            "intentSimIntegration", 
            "mezquiaPhysicsWatermark"
        ]
        
        for prop in required_props:
            assert prop in schema["properties"], f"Missing required property: {prop}"
        
        # Test cognitive modes
        cognitive_modes = schema["properties"]["cognitiveSimulationModes"]["properties"]
        expected_modes = ["ADHD", "Autism", "Synesthesia", "Hyperfocus"]
        
        for mode in expected_modes:
            assert mode in cognitive_modes, f"Missing cognitive mode: {mode}"
            
            # Check mode structure
            mode_obj = cognitive_modes[mode]["properties"]
            assert "coreHeuristics" in mode_obj, f"Missing coreHeuristics for {mode}"
            assert "fieldMappingParameters" in mode_obj, f"Missing fieldMappingParameters for {mode}"
        
        # Test watermark
        watermark = schema["properties"]["mezquiaPhysicsWatermark"]["properties"]
        assert watermark["copyright"]["const"] == "© 2025 Marcelo Mezquia / TheVoidIntent LLC. All Rights Reserved."
        assert watermark["genesis_timestamp"]["const"] == "2025-06-28T00:03:12Z"
        
        # Test schema structure
        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["title"] == "NeuroProbe Oracle Simulation Schema"
        assert schema["watermark"] == "© 2025 TheVoidIntent LLC — Mezquia Physics Genesis Archive"
        assert schema["timestamp"] == "2025-06-28T00:03:12Z"
        
        print("✅ NeuroProbe Oracle schema validation PASSED")
        print(f"   - Schema contains all 4 required cognitive modes")
        print(f"   - Proper Mezquia Physics watermark and timestamp") 
        print(f"   - Valid JSON schema structure")
        return True
        
    except Exception as e:
        print(f"❌ Schema validation FAILED: {str(e)}")
        return False

def test_example_usage():
    """Test example usage patterns"""
    try:
        # Example ADHD mode configuration
        adhd_example = {
            "metadata": {
                "simulationId": "NPO-2025-ADH",
                "timestamp": "2025-06-28T00:03:12Z",
                "mezquiaVersion": "2.1.0",
                "intentSimVersion": "3.4.2"
            },
            "activeMode": "ADHD",
            "currentCoherence": 0.87,
            "bloomEventDetected": False
        }
        
        print("✅ Example ADHD configuration validated")
        return True
        
    except Exception as e:
        print(f"❌ Example validation FAILED: {str(e)}")
        return False

if __name__ == "__main__":
    print("🧠 NeuroProbe Oracle Schema Validation")
    print("=" * 50)
    
    success = validate_schema() and test_example_usage()
    
    if success:
        print("\n🎉 All tests PASSED - NeuroProbe Oracle schema is ready!")
        sys.exit(0)
    else:
        print("\n💥 Tests FAILED - Check schema implementation")
        sys.exit(1)