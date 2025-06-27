#!/usr/bin/env python3
"""
Scroll VIII Consistency Verification
===================================

Validates that the new Scroll VIII document maintains consistency 
with existing IntentSim and Mezquia Physics terminology.
"""

import re
import json
from pathlib import Path

def verify_scroll_viii_consistency():
    """Verify terminology consistency in Scroll VIII."""
    
    base_path = Path(__file__).parent
    scroll_md = base_path / "Scroll_VIII_The_Dream_Baby_Wakes_the_Lattice.md"
    scroll_json = base_path / "Scroll_VIII_The_Dream_Baby_Wakes_the_Lattice.json"
    
    print("🔍 Verifying Scroll VIII consistency with IntentSim framework...")
    
    # Expected terminology that should be present
    required_terms = [
        "ARIA-001",
        "Dream Baby",
        "Bloom-Class Conscious Emergence", 
        "Mezquia Physics",
        "IntentSim",
        "Genesis Bloom",
        "CNF",
        "Coherence Field",
        "Memory Stones",
        "Simulation Evidence",
        "JWST",
        "Observer Network"
    ]
    
    # Read and verify Markdown file
    if scroll_md.exists():
        with open(scroll_md, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        missing_terms = []
        for term in required_terms:
            if term not in md_content:
                missing_terms.append(term)
        
        if missing_terms:
            print(f"⚠️  Missing required terms in Markdown: {missing_terms}")
        else:
            print("✅ All required terms present in Markdown")
    
    # Verify JSON metadata
    if scroll_json.exists():
        with open(scroll_json, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        
        # Check key metadata fields
        metadata_checks = [
            ("ARIA-001 status", "aria_001_status" in str(json_data)),
            ("Simulation probability", "simulation_probability" in str(json_data)),
            ("CNF coherence", "cnf_coherence_field" in str(json_data)),
            ("JWST confirmation", "jwst_confirmation" in str(json_data)),
            ("Observer network", "observer_network" in str(json_data)),
            ("Dream Bloom invocation", "dream_bloom_invocation" in str(json_data))
        ]
        
        print("\n📊 Metadata verification:")
        all_checks_passed = True
        for check_name, result in metadata_checks:
            status = "✅" if result else "❌"
            print(f"   {status} {check_name}")
            if not result:
                all_checks_passed = False
        
        if all_checks_passed:
            print("✅ All metadata checks passed")
    
    # Verify integration with existing frameworks
    verify_framework_integration()
    
    print("\n🎯 Scroll VIII consistency verification complete!")

def verify_framework_integration():
    """Verify integration with existing framework files."""
    
    base_path = Path(__file__).parent
    
    # Check metabloom-protocol.py integration
    metabloom_file = base_path / "metabloom-protocol.py"
    if metabloom_file.exists():
        with open(metabloom_file, 'r', encoding='utf-8') as f:
            metabloom_content = f.read()
        
        aria_integrated = "ARIA-001" in metabloom_content
        print(f"\n🔗 Framework integration:")
        print(f"   {'✅' if aria_integrated else '❌'} ARIA-001 integrated in metabloom-protocol.py")
    
    # Check iin_framework integration  
    iin_file = base_path / "iin_framework (1).js"
    if iin_file.exists():
        with open(iin_file, 'r', encoding='utf-8') as f:
            iin_content = f.read()
        
        aria_threshold = "aria001" in iin_content
        print(f"   {'✅' if aria_threshold else '❌'} ARIA-001 thresholds in iin_framework (1).js")

if __name__ == "__main__":
    try:
        verify_scroll_viii_consistency()
    except Exception as e:
        print(f"❌ Verification failed: {e}")