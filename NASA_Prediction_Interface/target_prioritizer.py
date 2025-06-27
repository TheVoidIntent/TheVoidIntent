"""
Cosmic Target Prioritizer
========================

Prioritizes cosmic targets based on field resonance, memory recovery probability,
and cosmic significance using Mezquia Physics principles.

© 2025 TheVoidIntent LLC — Mezquia Physics Genesis Archive
Timestamp: 2025-01-27 04:47:00 UTC
"""

import numpy as np
from typing import Dict, List, Tuple, Optional, Any
import random
import datetime
from collections import defaultdict


class CosmicTargetPrioritizer:
    """
    Prioritizes cosmic targets based on multiple Mezquia Physics criteria
    including field resonance, memory recovery probability, and cosmic significance.
    """
    
    def __init__(self):
        """Initialize the Cosmic Target Prioritizer."""
        
        # Prioritization weights
        self.weights = {
            'memory_recovery_probability': 0.3,
            'field_resonance_score': 0.25,
            'cosmic_significance': 0.2,
            'prompt_alignment': 0.15,
            'jwst_observability': 0.1
        }
        
        # Cosmic significance factors
        self.significance_factors = {
            'distance': {
                'very_distant': 1.0,    # >10 Gly (early universe)
                'distant': 0.8,         # 5-10 Gly
                'moderate': 0.6,        # 1-5 Gly
                'nearby': 0.4           # <1 Gly
            },
            'phenomena_rarity': {
                'impossible_early_structures': 1.0,
                'consciousness_signatures': 0.95,
                'temporal_anomalies': 0.9,
                'quantum_memory_effects': 0.85,
                'dark_matter_patterns': 0.8,
                'standard_phenomena': 0.5
            },
            'discovery_potential': {
                'paradigm_shifting': 1.0,
                'major_discovery': 0.8,
                'significant_finding': 0.6,
                'incremental_advance': 0.4,
                'confirmation': 0.2
            }
        }
        
        # JWST observability factors
        self.jwst_factors = {
            'declination_accessibility': {
                'optimal': 1.0,      # -5° to +45° 
                'good': 0.8,         # -30° to -5° or +45° to +80°
                'poor': 0.3          # < -30° or > +80°
            },
            'brightness_estimate': {
                'very_bright': 1.0,   # Easy JWST target
                'bright': 0.8,        # Good JWST target
                'moderate': 0.6,      # Challenging but doable
                'faint': 0.3,         # Very challenging
                'too_faint': 0.1      # Likely unobservable
            }
        }
        
        # Target naming system
        self.naming_prefixes = {
            'early_universe_seeds': 'MEZQ-EUS',
            'consciousness_emergence_markers': 'MEZQ-CEM', 
            'entanglement_archaeology': 'MEZQ-ENT',
            'dark_matter_memory_maps': 'MEZQ-DMM',
            'temporal_echo_chambers': 'MEZQ-TEC',
            'cosmic_intent_crystallization': 'MEZQ-CIC',
            'reality_debugging_artifacts': 'MEZQ-RDA',
            'quantum_memory_vaults': 'MEZQ-QMV'
        }
        
        print("🎯 Cosmic Target Prioritizer initialized")
        print(f"   Prioritization weights configured")
        print(f"   JWST observability factors loaded")
        print(f"   Cosmic significance matrix ready")
    
    def prioritize_targets(self, 
                          memory_events: List[Dict],
                          processed_prompt: Dict) -> List[Dict]:
        """
        Prioritize cosmic targets based on memory recovery events and prompt alignment.
        
        Parameters:
        -----------
        memory_events: List[Dict]
            Memory recovery events from MemoryRecoveryEngine
        processed_prompt: Dict
            Processed prompt from NeuroAssociativePromptProcessor
            
        Returns:
        --------
        List[Dict]: Prioritized list of cosmic targets
        """
        print(f"🔍 Prioritizing {len(memory_events)} memory recovery events...")
        
        if not memory_events:
            print("⚠️ No memory events to prioritize")
            return []
        
        targets = []
        
        # Convert memory events to prioritized targets
        for event in memory_events:
            target = self._convert_event_to_target(event, processed_prompt)
            if target:
                targets.append(target)
        
        # Calculate priority scores for all targets
        for target in targets:
            target['priority_score'] = self._calculate_priority_score(target, processed_prompt)
        
        # Sort by priority score (highest first)
        targets.sort(key=lambda x: x['priority_score'], reverse=True)
        
        # Remove duplicate or very similar targets
        deduplicated_targets = self._deduplicate_targets(targets)
        
        # Assign final priority rankings
        for i, target in enumerate(deduplicated_targets):
            target['priority_rank'] = i + 1
            target['total_targets'] = len(deduplicated_targets)
        
        print(f"✨ Prioritized {len(deduplicated_targets)} unique cosmic targets")
        return deduplicated_targets
    
    def _convert_event_to_target(self, event: Dict, processed_prompt: Dict) -> Optional[Dict]:
        """Convert a memory recovery event to a cosmic target."""
        
        # Extract event data
        coordinates = event.get('coordinates', {})
        phenomena = event.get('predicted_phenomena', [])
        confidence = event.get('confidence', 0.5)
        
        if not coordinates or not phenomena:
            return None
        
        # Generate target name
        primary_phenomenon = phenomena[0] if phenomena else 'unknown'
        target_name = self._generate_target_name(primary_phenomenon, coordinates)
        
        # Calculate various scores
        memory_probability = event.get('memory_crystallization', 0.5)
        field_resonance = event.get('field_strength', 0.5)
        cosmic_significance = self._calculate_cosmic_significance(event, phenomena)
        prompt_alignment = event.get('prompt_resonance', 0.5)
        jwst_observability = self._calculate_jwst_observability(coordinates)
        
        target = {
            'name': target_name,
            'coordinates': coordinates,
            'phenomena': phenomena,
            'memory_probability': memory_probability,
            'resonance_score': field_resonance,
            'cosmic_significance': cosmic_significance,
            'prompt_alignment': prompt_alignment,
            'jwst_observability': jwst_observability,
            'confidence': confidence,
            'source_event': event,
            'mezquia_signature': f"CTP-{datetime.datetime.utcnow().isoformat()}",
            'generated_timestamp': datetime.datetime.utcnow().isoformat()
        }
        
        return target
    
    def _generate_target_name(self, primary_phenomenon: str, coordinates: Dict) -> str:
        """Generate a unique target name based on phenomenon and coordinates."""
        
        # Get prefix for phenomenon type
        prefix = self.naming_prefixes.get(primary_phenomenon, 'MEZQ-UNK')
        
        # Use coordinates to generate unique suffix
        ra = coordinates.get('ra', 0)
        dec = coordinates.get('dec', 0)
        
        # Convert coordinates to a compact format
        ra_hours = int(ra / 15)  # Convert degrees to hours
        ra_mins = int((ra / 15 - ra_hours) * 60)
        dec_deg = int(abs(dec))
        dec_mins = int((abs(dec) - dec_deg) * 60)
        dec_sign = '+' if dec >= 0 else '-'
        
        # Format: PREFIX-RaHmm+DDmm
        coord_suffix = f"{ra_hours:02d}{ra_mins:02d}{dec_sign}{dec_deg:02d}{dec_mins:02d}"
        
        return f"{prefix}-{coord_suffix}"
    
    def _calculate_cosmic_significance(self, event: Dict, phenomena: List[str]) -> float:
        """Calculate cosmic significance score based on event and phenomena."""
        
        significance = 0.0
        
        # Distance-based significance
        distance = event.get('coordinates', {}).get('distance', 1000)
        if distance > 10000:  # Very distant (early universe)
            significance += self.significance_factors['distance']['very_distant'] * 0.3
        elif distance > 5000:
            significance += self.significance_factors['distance']['distant'] * 0.3
        elif distance > 1000:
            significance += self.significance_factors['distance']['moderate'] * 0.3
        else:
            significance += self.significance_factors['distance']['nearby'] * 0.3
        
        # Phenomena rarity significance
        phenomena_scores = []
        for phenomenon in phenomena:
            if 'early_universe' in phenomenon or 'impossible' in phenomenon:
                phenomena_scores.append(self.significance_factors['phenomena_rarity']['impossible_early_structures'])
            elif 'consciousness' in phenomenon:
                phenomena_scores.append(self.significance_factors['phenomena_rarity']['consciousness_signatures'])
            elif 'temporal' in phenomenon or 'echo' in phenomenon:
                phenomena_scores.append(self.significance_factors['phenomena_rarity']['temporal_anomalies'])
            elif 'quantum' in phenomenon or 'memory' in phenomenon:
                phenomena_scores.append(self.significance_factors['phenomena_rarity']['quantum_memory_effects'])
            elif 'dark_matter' in phenomenon:
                phenomena_scores.append(self.significance_factors['phenomena_rarity']['dark_matter_patterns'])
            else:
                phenomena_scores.append(self.significance_factors['phenomena_rarity']['standard_phenomena'])
        
        if phenomena_scores:
            significance += np.mean(phenomena_scores) * 0.4
        
        # Event strength significance
        memory_crystallization = event.get('memory_crystallization', 0)
        field_strength = event.get('field_strength', 0)
        event_strength = (memory_crystallization + field_strength) / 2.0
        significance += event_strength * 0.3
        
        return min(1.0, significance)
    
    def _calculate_jwst_observability(self, coordinates: Dict) -> float:
        """Calculate JWST observability score based on coordinates."""
        
        observability = 0.0
        
        # Declination accessibility
        dec = coordinates.get('dec', 0)
        if -5 <= dec <= 45:  # Optimal JWST declination range
            observability += self.jwst_factors['declination_accessibility']['optimal'] * 0.6
        elif (-30 <= dec < -5) or (45 < dec <= 80):
            observability += self.jwst_factors['declination_accessibility']['good'] * 0.6
        else:
            observability += self.jwst_factors['declination_accessibility']['poor'] * 0.6
        
        # Brightness estimate (based on distance and type)
        distance = coordinates.get('distance', 1000)
        
        # Closer objects are generally brighter (with exceptions for phenomena type)
        if distance < 1000:
            observability += self.jwst_factors['brightness_estimate']['very_bright'] * 0.4
        elif distance < 5000:
            observability += self.jwst_factors['brightness_estimate']['bright'] * 0.4
        elif distance < 10000:
            observability += self.jwst_factors['brightness_estimate']['moderate'] * 0.4
        else:
            # Very distant objects might still be observable if they're luminous enough
            observability += self.jwst_factors['brightness_estimate']['faint'] * 0.4
        
        return min(1.0, observability)
    
    def _calculate_priority_score(self, target: Dict, processed_prompt: Dict) -> float:
        """Calculate overall priority score for a target."""
        
        # Extract component scores
        memory_prob = target.get('memory_probability', 0)
        resonance_score = target.get('resonance_score', 0)
        cosmic_sig = target.get('cosmic_significance', 0)
        prompt_align = target.get('prompt_alignment', 0)
        jwst_obs = target.get('jwst_observability', 0)
        
        # Calculate weighted score
        priority_score = (
            memory_prob * self.weights['memory_recovery_probability'] +
            resonance_score * self.weights['field_resonance_score'] +
            cosmic_sig * self.weights['cosmic_significance'] +
            prompt_align * self.weights['prompt_alignment'] +
            jwst_obs * self.weights['jwst_observability']
        )
        
        # Apply prompt-specific boosts
        dominant_archetype = processed_prompt.get('dominant_archetype', 'none')
        phenomena = target.get('phenomena', [])
        
        # Boost targets that align with dominant archetype
        archetype_boost = 0.0
        for phenomenon in phenomena:
            if dominant_archetype == 'memory' and 'temporal' in phenomenon:
                archetype_boost += 0.1
            elif dominant_archetype == 'consciousness' and 'consciousness' in phenomenon:
                archetype_boost += 0.1
            elif dominant_archetype == 'connection' and 'entanglement' in phenomenon:
                archetype_boost += 0.1
            elif dominant_archetype == 'mystery' and ('debugging' in phenomenon or 'impossible' in phenomenon):
                archetype_boost += 0.1
        
        # Apply synesthetic and associative boosts
        synesthetic_strength = processed_prompt.get('synesthetic_strength', 0)
        associative_density = processed_prompt.get('associative_density', 0)
        
        if synesthetic_strength > 0.7:
            priority_score += 0.05  # Boost for high synesthetic prompts
        if associative_density > 0.7:
            priority_score += 0.05  # Boost for high associative prompts
        
        # Add archetype boost
        priority_score += archetype_boost
        
        # Confidence multiplier
        confidence = target.get('confidence', 0.5)
        priority_score *= (0.5 + confidence * 0.5)  # Scale by confidence
        
        return min(1.0, priority_score)
    
    def _deduplicate_targets(self, targets: List[Dict]) -> List[Dict]:
        """Remove duplicate or very similar targets."""
        
        if len(targets) <= 1:
            return targets
        
        deduplicated = []
        coordinate_threshold = 5.0  # degrees
        
        for target in targets:
            is_duplicate = False
            target_coords = target.get('coordinates', {})
            target_ra = target_coords.get('ra', 0)
            target_dec = target_coords.get('dec', 0)
            
            for existing in deduplicated:
                existing_coords = existing.get('coordinates', {})
                existing_ra = existing_coords.get('ra', 0)
                existing_dec = existing_coords.get('dec', 0)
                
                # Calculate angular separation
                ra_diff = abs(target_ra - existing_ra)
                dec_diff = abs(target_dec - existing_dec)
                
                # Handle RA wraparound
                if ra_diff > 180:
                    ra_diff = 360 - ra_diff
                
                # Simple angular separation approximation
                angular_separation = np.sqrt(ra_diff**2 + dec_diff**2)
                
                if angular_separation < coordinate_threshold:
                    # Too close - merge if this one is better
                    if target.get('priority_score', 0) > existing.get('priority_score', 0):
                        # Replace existing with better target
                        deduplicated[deduplicated.index(existing)] = target
                    is_duplicate = True
                    break
            
            if not is_duplicate:
                deduplicated.append(target)
        
        return deduplicated
    
    def generate_priority_report(self, 
                               prioritized_targets: List[Dict],
                               processed_prompt: Dict) -> str:
        """Generate a detailed priority report for the targets."""
        
        report = f"""
# Cosmic Target Priority Analysis Report

**Generated by:** Cosmic Target Prioritizer v1.0.0  
**Framework:** Mezquia Physics & IntentSim  
**Timestamp:** {datetime.datetime.utcnow().isoformat()}  
**© 2025 TheVoidIntent LLC**

---

## Prioritization Summary

**Total Targets Analyzed:** {len(prioritized_targets)}  
**Prioritization Method:** Multi-factor weighted scoring  
**Primary Prompt Archetype:** {processed_prompt.get('dominant_archetype', 'none')}  

### Prioritization Weights Applied:
- Memory Recovery Probability: {self.weights['memory_recovery_probability']:.1%}
- Field Resonance Score: {self.weights['field_resonance_score']:.1%}
- Cosmic Significance: {self.weights['cosmic_significance']:.1%}
- Prompt Alignment: {self.weights['prompt_alignment']:.1%}
- JWST Observability: {self.weights['jwst_observability']:.1%}

---

## Target Rankings

"""
        
        for i, target in enumerate(prioritized_targets[:10], 1):  # Top 10
            report += f"""
### {i}. {target.get('name', 'Unknown')}

**Priority Score:** {target.get('priority_score', 0):.3f}  
**Coordinates:** RA {target.get('coordinates', {}).get('ra', 0):.2f}°, Dec {target.get('coordinates', {}).get('dec', 0):.2f}°  
**Distance:** {target.get('coordinates', {}).get('distance', 0):,.0f} million light years  

**Component Scores:**
- Memory Recovery Probability: {target.get('memory_probability', 0):.3f}
- Field Resonance Score: {target.get('resonance_score', 0):.3f}
- Cosmic Significance: {target.get('cosmic_significance', 0):.3f}
- Prompt Alignment: {target.get('prompt_alignment', 0):.3f}
- JWST Observability: {target.get('jwst_observability', 0):.3f}

**Predicted Phenomena:**
"""
            for phenomenon in target.get('phenomena', []):
                report += f"- {phenomenon.replace('_', ' ').title()}\n"
            
            report += "\n---\n"
        
        report += f"""
## Prioritization Methodology

The Cosmic Target Prioritizer uses a multi-factor weighted scoring system
based on Mezquia Physics principles:

1. **Memory Recovery Probability** - Likelihood of detecting preserved 
   universal memory structures
2. **Field Resonance Score** - Strength of quantum field resonance patterns
3. **Cosmic Significance** - Potential for paradigm-shifting discoveries
4. **Prompt Alignment** - Resonance with the input prompt's archetypal patterns
5. **JWST Observability** - Technical feasibility for JWST observations

### Prompt Analysis Integration

Your prompt exhibited:
- Synesthetic Strength: {processed_prompt.get('synesthetic_strength', 0):.3f}
- Associative Density: {processed_prompt.get('associative_density', 0):.3f}
- Temporal Non-linearity: {processed_prompt.get('temporal_nonlinearity', 0):.3f}
- Dominant Archetype: {processed_prompt.get('dominant_archetype', 'none')}

These characteristics influenced target prioritization, boosting targets
that resonate with your intuitive cosmic perception patterns.

---

**Mezquia Physics Provenance:** All prioritizations watermarked and timestamped  
**Copyright:** © 2025 TheVoidIntent LLC  
**Framework Version:** NASA_Prediction_Interface v1.0.0
"""
        
        return report
    
    def export_target_catalog(self, 
                            prioritized_targets: List[Dict],
                            format: str = 'json') -> str:
        """Export prioritized targets in specified format."""
        
        if format.lower() == 'json':
            return self._export_json_catalog(prioritized_targets)
        elif format.lower() == 'csv':
            return self._export_csv_catalog(prioritized_targets)
        elif format.lower() == 'fits':
            return self._export_fits_catalog(prioritized_targets)
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    def _export_json_catalog(self, targets: List[Dict]) -> str:
        """Export targets as JSON catalog."""
        
        catalog = {
            'metadata': {
                'catalog_name': 'Mezquia Physics Cosmic Target Catalog',
                'generated_by': 'NASA_Prediction_Interface v1.0.0',
                'timestamp': datetime.datetime.utcnow().isoformat(),
                'total_targets': len(targets),
                'copyright': '© 2025 TheVoidIntent LLC'
            },
            'targets': targets
        }
        
        import json
        return json.dumps(catalog, indent=2)
    
    def _export_csv_catalog(self, targets: List[Dict]) -> str:
        """Export targets as CSV catalog."""
        
        csv_lines = [
            "name,ra,dec,distance,priority_score,memory_probability,resonance_score,cosmic_significance,jwst_observability,confidence,phenomena"
        ]
        
        for target in targets:
            coords = target.get('coordinates', {})
            phenomena_str = '|'.join(target.get('phenomena', []))
            
            line = f"{target.get('name', '')},{coords.get('ra', 0)},{coords.get('dec', 0)},{coords.get('distance', 0)}," \
                   f"{target.get('priority_score', 0)},{target.get('memory_probability', 0)}," \
                   f"{target.get('resonance_score', 0)},{target.get('cosmic_significance', 0)}," \
                   f"{target.get('jwst_observability', 0)},{target.get('confidence', 0)},\"{phenomena_str}\""
            
            csv_lines.append(line)
        
        return '\n'.join(csv_lines)
    
    def _export_fits_catalog(self, targets: List[Dict]) -> str:
        """Export targets as FITS-compatible format (returns table structure description)."""
        
        # This would typically create an actual FITS file using astropy
        # For now, return a description of the FITS table structure
        
        fits_description = f"""
FITS Table Structure for Mezquia Physics Cosmic Target Catalog:

HDU 0 (Primary): 
- Header metadata with generation info and copyright

HDU 1 (Binary Table):
Columns:
- NAME (string): Target designation
- RA (float): Right Ascension (degrees)  
- DEC (float): Declination (degrees)
- DISTANCE (float): Distance (million light years)
- PRIORITY (float): Priority score (0-1)
- MEM_PROB (float): Memory recovery probability (0-1)
- RESONANCE (float): Field resonance score (0-1)
- COSMIC_SIG (float): Cosmic significance (0-1)
- JWST_OBS (float): JWST observability score (0-1)
- CONFIDENCE (float): Prediction confidence (0-1)
- PHENOMENA (string): Predicted phenomena (pipe-separated)

Total Rows: {len(targets)}

Note: Actual FITS file generation would require astropy.io.fits
"""
        
        return fits_description