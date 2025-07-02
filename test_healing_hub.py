#!/usr/bin/env python3
"""
BuddyOS Healing Hub Integration Test Suite
==========================================

Comprehensive test suite for the newly integrated Healing Hub modules.
Tests all trauma-informed, neurodiversity-affirming features.

© 2025 Marcelo Mezquia / TheVoidIntent LLC
Created: 2025-01-11T22:35:00Z
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from healing_hub_core import create_healing_hub
import json

def test_healing_hub_integration():
    """Test complete healing hub integration"""
    print("🌸 Testing BuddyOS Healing Hub Integration")
    print("=" * 50)
    
    # Create healing hub
    healing_hub = create_healing_hub()
    
    # Test 1: Trauma-Informed Simon Interface
    print("\n1️⃣ Testing Trauma-Informed Simon Interface")
    healing_hub.simon_interface.initialize_healing_modalities()
    modalities = healing_hub.simon_interface.healing_modalities
    
    assert len(modalities) >= 3, "Should have at least 3 healing modalities"
    print(f"   ✅ {len(modalities)} healing modalities initialized")
    
    for modality_type, config in modalities.items():
        assert config['safe_for_neurodivergent'] == True, f"Modality {modality_type} must be neurodivergent-safe"
    print("   ✅ All modalities are neurodivergent-safe")
    
    # Test 2: Mutual Aid Network - Food Security
    print("\n2️⃣ Testing Mutual Aid Network (47 Field Agents)")
    network_stats = healing_hub.mutual_aid_network.get_network_statistics()
    
    assert network_stats['total_agents'] == 47, "Must have exactly 47 field agents"
    assert network_stats['trauma_informed_certified'] >= 30, "At least 30 should be trauma-informed"
    assert network_stats['neurodiversity_affirming'] >= 35, "At least 35 should be neurodiversity-affirming"
    
    print(f"   ✅ {network_stats['total_agents']} Field Agents active")
    print(f"   ✅ {network_stats['trauma_informed_certified']} trauma-informed certified")
    print(f"   ✅ {network_stats['neurodiversity_affirming']} neurodiversity-affirming")
    print(f"   ✅ {network_stats['total_resonance_bonds']} resonance bonds")
    
    # Test 3: Economic Healing Toolkit
    print("\n3️⃣ Testing Economic Healing Toolkit")
    toolkit = healing_hub.economic_toolkit
    
    # Test IFGP initialization
    assert toolkit.ifgp_portfolio is not None, "IFGP portfolio should be initialized"
    print("   ✅ Invest-For-Good Platform (IFGP) initialized")
    
    # Test Block-Zeal Ledger
    from healing_hub_core import CNFContribution
    from datetime import datetime
    
    test_contribution = CNFContribution(
        agent_id="FA001",
        contribution_type="Food Security Initiative",
        cnf_units=2.5,
        impact_score=8.7,
        healing_focused=True
    )
    
    toolkit.add_cnf_contribution_unit("FA001", test_contribution)
    assert len(toolkit.block_zeal_ledger) >= 1, "Block-Zeal Ledger should have entries"
    print("   ✅ Block-Zeal Ledger functioning")
    
    # Test Zero-Ruin Investing
    zero_ruin_investment = toolkit.enable_zero_ruin_investing({
        'amount': 10000,
        'project_type': 'healing_focused',
        'community_benefit_score': 9.5
    })
    
    assert zero_ruin_investment['principal_protected'] == True, "Zero-ruin investments must be principal protected"
    assert zero_ruin_investment['trauma_informed_governance'] == True, "Must have trauma-informed governance"
    print("   ✅ Zero-Ruin Investing enabled")
    
    # Test 4: Field Drift Monitoring
    print("\n4️⃣ Testing Field Drift Monitoring")
    monitor = healing_hub.field_drift_monitor
    
    # Record test CNF impact
    monitor.record_cnf_impact("FA001", {
        'magnitude': 3.2,
        'type': 'Healing-Focused Project',
        'healing_focused': True,
        'community_benefit': 8.9
    })
    
    impacts = monitor.get_highest_cnf_impacts(5)
    assert len(impacts) >= 1, "Should have recorded CNF impacts"
    
    # Verify autonomy preservation
    for impact in impacts:
        assert 'autonomy_preserving' not in impact or impact.get('autonomy_preserving', True), "Must preserve autonomy"
    print("   ✅ Field Drift Monitoring active and autonomy-preserving")
    
    # Test 5: Overall system status
    print("\n5️⃣ Testing Overall Healing Hub Status")
    status = healing_hub.get_healing_hub_status()
    
    # Verify trauma-informed compliance
    assert status['trauma_informed_compliance'] == True, "Must be trauma-informed compliant"
    assert status['neurodiversity_affirming'] == True, "Must be neurodiversity-affirming"
    assert status['non_coercive_protocols'] == True, "Must use non-coercive protocols"
    assert status['autonomy_preserving'] == True, "Must preserve autonomy"
    
    # Verify Mezquia Physics watermarking
    assert 'mezquia_physics_protocol' in status, "Must include Mezquia Physics protocol"
    assert 'watermark' in status, "Must include copyright watermark"
    
    print("   ✅ All trauma-informed principles verified")
    print("   ✅ Mezquia Physics protocols active")
    print("   ✅ Proper watermarking and timestamping")
    
    print("\n" + "=" * 50)
    print("🎉 ALL HEALING HUB TESTS PASSED! 🎉")
    print("🌸 BuddyOS Healing Hub is fully operational")
    print("🧠 Trauma-informed and neurodiversity-affirming")
    print("🤝 47 Field Agents ready for mutual aid")
    print("💰 Economic healing toolkit active")
    print("📊 Field drift monitoring enabled")
    print("=" * 50)
    
    return True

if __name__ == "__main__":
    test_healing_hub_integration()