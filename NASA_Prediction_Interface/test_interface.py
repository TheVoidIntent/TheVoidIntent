#!/usr/bin/env python3
"""
Quick Test of NASA Prediction Interface
=======================================

A simple test to verify the interface is working properly.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from NASA_Prediction_Interface import CosmicMemoryPredictor

def test_interface():
    """Test the interface with a meaningful prompt and realistic parameters."""
    
    print("🌌 Testing NASA Prediction Interface")
    print("=" * 50)
    
    # Initialize with reasonable parameters for testing
    predictor = CosmicMemoryPredictor(
        simulation_scale=10000,  # 10k simulations for quick testing
        memory_threshold=0.6,
        resonance_threshold=0.7,
        max_targets=5
    )
    
    # Use a rich, synesthetic prompt
    rich_prompt = """
    The violet frequencies of distant quasars sing ancient lullabies while 
    golden threads of dark matter weave memories through spacetime. I feel 
    the universe breathing, each cosmic web filament a neural pathway storing 
    the dreams of early galaxies that learned to shine before physics said 
    they could exist.
    
    James Webb's infrared eyes see backwards through time where impossible 
    structures crystallize consciousness into matter. Where does the cosmos 
    hide its deepest memory stones? Show me the places where reality 
    debugged itself and left traces of cosmic code patches.
    """
    
    # Add realistic cosmic context
    cosmic_context = {
        'jwst_recent_observations': [
            'MACS-J1149.5+2223',
            'Abell 2744',
            'SMACS 0723'
        ],
        'known_anomalies': [
            'impossible_early_galaxies',
            'mature_structures_at_z>10'
        ]
    }
    
    print("🔮 Generating predictions...")
    
    try:
        predictions = predictor.predict_memory_recovery_events(
            prompt=rich_prompt,
            cosmic_context=cosmic_context
        )
        
        print(f"\n✨ Successfully generated {len(predictions)} predictions!")
        
        if predictions:
            print("\n🎯 Top Predictions:")
            for i, pred in enumerate(predictions[:3], 1):
                print(f"\n{i}. {pred.target_name}")
                print(f"   📍 RA {pred.coordinates['ra']:.2f}°, Dec {pred.coordinates['dec']:.2f}°")
                print(f"   🌌 Distance: {pred.coordinates['distance']:,.0f} Mly")
                print(f"   🧠 Memory Probability: {pred.memory_recovery_probability:.3f}")
                print(f"   ⚡ Field Resonance: {pred.field_resonance_score:.3f}")
                print(f"   🎯 Confidence: {pred.confidence_level:.3f}")
                print(f"   🔬 Phenomena: {', '.join(pred.predicted_phenomena)}")
            
            # Generate a sample report
            print("\n📊 Generating observation report...")
            report = predictor.generate_observation_report(predictions)
            
            # Save report to file
            with open('test_observation_report.md', 'w') as f:
                f.write(report)
            
            print("✅ Test report saved to: test_observation_report.md")
            
            # Save predictions
            predictor.save_predictions(predictions, 'test_predictions.json')
            print("✅ Test predictions saved to: test_predictions.json")
            
        else:
            print("⚠️ No predictions generated - may need larger simulation scale")
            
    except Exception as e:
        print(f"❌ Error during testing: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
    
    print("\n🚀 NASA Prediction Interface test completed successfully!")
    return True

if __name__ == "__main__":
    test_interface()