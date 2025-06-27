"""
Neuro-Associative Prompt Processor
==================================

Processes non-linear, associative, and synesthetic-style prompts to extract
cosmic intent patterns for memory recovery simulation.

© 2025 TheVoidIntent LLC — Mezquia Physics Genesis Archive
Timestamp: 2025-01-27 04:47:00 UTC
"""

import re
import numpy as np
from typing import Dict, List, Tuple, Optional, Any
from collections import defaultdict
import json
import datetime


class NeuroAssociativePromptProcessor:
    """
    Processes neurodivergent thought patterns in prompts to extract
    cosmic intent patterns for IntentSim configuration.
    """
    
    def __init__(self):
        """Initialize the prompt processor with pattern recognition systems."""
        
        # Synesthetic pattern recognition
        self.synesthetic_patterns = {
            'color_sound': ['red frequency', 'blue tone', 'violet hum', 'golden resonance'],
            'texture_light': ['rough brightness', 'smooth glow', 'crystalline flash'],
            'emotion_temperature': ['warm sadness', 'cold joy', 'burning peace'],
            'time_space': ['future echoes', 'past ripples', 'present depth'],
            'abstract_concrete': ['heavy thoughts', 'light ideas', 'dense meaning']
        }
        
        # Associative density markers
        self.associative_markers = [
            'like', 'reminds me of', 'connects to', 'feels similar to',
            'branches into', 'spirals toward', 'echoes', 'resonates with',
            'mirrors', 'parallels', 'interweaves', 'crystallizes into'
        ]
        
        # Temporal non-linearity indicators
        self.temporal_markers = [
            'suddenly', 'meanwhile', 'before this', 'in another time',
            'simultaneously', 'overlapping', 'recurring', 'cycling back',
            'jumping forward', 'memory loops', 'future bleeding through'
        ]
        
        # Cosmic archetypal patterns
        self.cosmic_archetypes = {
            'creation': ['birth', 'genesis', 'origin', 'first breath', 'emergence'],
            'memory': ['remembers', 'forgotten', 'recall', 'traces', 'imprints'],
            'consciousness': ['aware', 'observing', 'witness', 'perceiving', 'knowing'],
            'connection': ['entangled', 'linked', 'bonded', 'unified', 'merged'],
            'transformation': ['becoming', 'evolving', 'shifting', 'metamorphosis'],
            'mystery': ['unknown', 'hidden', 'secret', 'veiled', 'impossible']
        }
        
        # Emotional frequency mapping
        self.emotional_frequencies = {
            'wonder': 528,  # Love frequency
            'awe': 741,     # Awakening intuition
            'curiosity': 396,  # Liberation from guilt/fear
            'joy': 528,
            'peace': 528,
            'fear': 174,    # Foundation frequency
            'anger': 417,   # Facilitating change
            'sadness': 396
        }
        
        print("🧠 Neuro-Associative Prompt Processor initialized")
        print("   Synesthetic pattern recognition: Active")
        print("   Associative density mapping: Ready")
        print("   Temporal non-linearity detection: Online")
    
    def process_prompt(self, prompt: str) -> Dict[str, Any]:
        """
        Process a non-linear, associative prompt into cosmic intent patterns.
        
        Parameters:
        -----------
        prompt: str
            The input prompt (can be non-linear, associative, synesthetic)
            
        Returns:
        --------
        Dict[str, Any]: Processed prompt with extracted patterns
        """
        print(f"🔍 Processing prompt: {len(prompt)} characters")
        
        # Clean and normalize prompt
        cleaned_prompt = self._clean_prompt(prompt)
        
        # Extract different types of patterns
        synesthetic_analysis = self._analyze_synesthetic_patterns(cleaned_prompt)
        associative_analysis = self._analyze_associative_density(cleaned_prompt)
        temporal_analysis = self._analyze_temporal_nonlinearity(cleaned_prompt)
        cosmic_analysis = self._analyze_cosmic_archetypes(cleaned_prompt)
        emotional_analysis = self._analyze_emotional_frequencies(cleaned_prompt)
        
        # Generate cosmic intent vectors
        intent_vectors = self._generate_intent_vectors(
            synesthetic_analysis,
            associative_analysis,
            temporal_analysis,
            cosmic_analysis,
            emotional_analysis
        )
        
        # Create final processed prompt structure
        processed = {
            'original_prompt': prompt,
            'cleaned_prompt': cleaned_prompt,
            'timestamp': datetime.datetime.utcnow().isoformat(),
            
            # Pattern analysis results
            'synesthetic_strength': synesthetic_analysis['strength'],
            'synesthetic_patterns': synesthetic_analysis['patterns'],
            
            'associative_density': associative_analysis['density'],
            'associative_connections': associative_analysis['connections'],
            
            'temporal_nonlinearity': temporal_analysis['nonlinearity'],
            'temporal_markers': temporal_analysis['markers'],
            
            'cosmic_archetypes': cosmic_analysis['archetypes'],
            'dominant_archetype': cosmic_analysis['dominant'],
            
            'emotional_frequency': emotional_analysis['primary_frequency'],
            'emotional_resonance': emotional_analysis['resonance_map'],
            
            # Intent vectors for IntentSim configuration
            'intent_vectors': intent_vectors,
            
            # Mezquia Physics watermarking
            'mezquia_processed': True,
            'processing_signature': f"NAP-{datetime.datetime.utcnow().isoformat()}",
            'copyright': '© 2025 TheVoidIntent LLC'
        }
        
        print(f"✨ Prompt processed:")
        print(f"   Synesthetic strength: {synesthetic_analysis['strength']:.3f}")
        print(f"   Associative density: {associative_analysis['density']:.3f}")
        print(f"   Temporal non-linearity: {temporal_analysis['nonlinearity']:.3f}")
        print(f"   Dominant archetype: {cosmic_analysis['dominant']}")
        
        return processed
    
    def _clean_prompt(self, prompt: str) -> str:
        """Clean and normalize the prompt while preserving meaningful patterns."""
        
        # Convert to lowercase for pattern matching
        cleaned = prompt.lower()
        
        # Remove extra whitespace but preserve line breaks (they might be meaningful)
        cleaned = re.sub(r'[ \t]+', ' ', cleaned)
        
        # Remove some punctuation but keep meaningful ones
        cleaned = re.sub(r'[(){}[\]"]', '', cleaned)
        
        return cleaned.strip()
    
    def _analyze_synesthetic_patterns(self, prompt: str) -> Dict[str, Any]:
        """Analyze synesthetic cross-modal sensory patterns in the prompt."""
        
        synesthetic_count = 0
        found_patterns = []
        
        for pattern_type, patterns in self.synesthetic_patterns.items():
            for pattern in patterns:
                if pattern in prompt:
                    synesthetic_count += 1
                    found_patterns.append({
                        'type': pattern_type,
                        'pattern': pattern,
                        'strength': prompt.count(pattern)
                    })
        
        # Look for custom synesthetic constructions
        # Patterns like "adjective + sense" (e.g., "loud colors", "bright sounds")
        synesthetic_constructions = re.findall(
            r'\b(bright|dark|loud|quiet|soft|hard|warm|cold|sweet|bitter|rough|smooth)\s+(sound|color|light|taste|feeling|vibration|frequency|resonance)\b',
            prompt
        )
        
        for construction in synesthetic_constructions:
            synesthetic_count += 1
            found_patterns.append({
                'type': 'custom_synesthetic',
                'pattern': f"{construction[0]} {construction[1]}",
                'strength': 1
            })
        
        # Calculate overall synesthetic strength
        total_words = len(prompt.split())
        strength = min(1.0, synesthetic_count / max(total_words * 0.1, 1))
        
        return {
            'strength': strength,
            'patterns': found_patterns,
            'count': synesthetic_count
        }
    
    def _analyze_associative_density(self, prompt: str) -> Dict[str, Any]:
        """Analyze associative connection density in the prompt."""
        
        connections = []
        connection_count = 0
        
        # Find explicit associative markers
        for marker in self.associative_markers:
            if marker in prompt:
                # Find the context around the marker
                marker_positions = [m.start() for m in re.finditer(re.escape(marker), prompt)]
                for pos in marker_positions:
                    start = max(0, pos - 30)
                    end = min(len(prompt), pos + len(marker) + 30)
                    context = prompt[start:end]
                    
                    connections.append({
                        'marker': marker,
                        'context': context,
                        'position': pos
                    })
                    connection_count += 1
        
        # Look for implicit associative patterns (rapid topic shifts)
        sentences = re.split(r'[.!?]+', prompt)
        topic_shifts = 0
        
        for i in range(len(sentences) - 1):
            current_words = set(sentences[i].split())
            next_words = set(sentences[i + 1].split())
            
            # If sentences share very few words, it might be an associative jump
            if len(current_words & next_words) < 2 and len(current_words) > 3 and len(next_words) > 3:
                topic_shifts += 1
        
        # Calculate associative density
        total_sentences = len(sentences)
        explicit_density = connection_count / max(total_sentences, 1)
        implicit_density = topic_shifts / max(total_sentences - 1, 1)
        overall_density = min(1.0, (explicit_density + implicit_density * 0.5))
        
        return {
            'density': overall_density,
            'connections': connections,
            'explicit_count': connection_count,
            'implicit_shifts': topic_shifts
        }
    
    def _analyze_temporal_nonlinearity(self, prompt: str) -> Dict[str, Any]:
        """Analyze temporal non-linearity in the prompt."""
        
        temporal_markers_found = []
        nonlinearity_score = 0
        
        # Find explicit temporal markers
        for marker in self.temporal_markers:
            if marker in prompt:
                count = prompt.count(marker)
                temporal_markers_found.append({
                    'marker': marker,
                    'count': count
                })
                nonlinearity_score += count
        
        # Look for tense switching within sentences
        sentences = re.split(r'[.!?]+', prompt)
        tense_switches = 0
        
        for sentence in sentences:
            # Simple tense detection (this could be more sophisticated)
            has_past = bool(re.search(r'\b(was|were|had|did|been)\b', sentence))
            has_present = bool(re.search(r'\b(is|are|am|do|does)\b', sentence))
            has_future = bool(re.search(r'\b(will|shall|going to)\b', sentence))
            
            tense_count = sum([has_past, has_present, has_future])
            if tense_count > 1:
                tense_switches += 1
        
        # Calculate overall temporal non-linearity
        total_sentences = len(sentences)
        explicit_nonlinearity = nonlinearity_score / max(len(prompt.split()), 1)
        implicit_nonlinearity = tense_switches / max(total_sentences, 1)
        overall_nonlinearity = min(1.0, explicit_nonlinearity + implicit_nonlinearity * 0.3)
        
        return {
            'nonlinearity': overall_nonlinearity,
            'markers': temporal_markers_found,
            'tense_switches': tense_switches
        }
    
    def _analyze_cosmic_archetypes(self, prompt: str) -> Dict[str, Any]:
        """Analyze cosmic archetypal patterns in the prompt."""
        
        archetype_scores = defaultdict(int)
        found_patterns = defaultdict(list)
        
        for archetype, patterns in self.cosmic_archetypes.items():
            for pattern in patterns:
                if pattern in prompt:
                    count = prompt.count(pattern)
                    archetype_scores[archetype] += count
                    found_patterns[archetype].append({
                        'pattern': pattern,
                        'count': count
                    })
        
        # Find dominant archetype
        dominant_archetype = max(archetype_scores, key=archetype_scores.get) if archetype_scores else 'none'
        
        return {
            'archetypes': dict(archetype_scores),
            'dominant': dominant_archetype,
            'patterns': dict(found_patterns)
        }
    
    def _analyze_emotional_frequencies(self, prompt: str) -> Dict[str, Any]:
        """Analyze emotional frequencies in the prompt."""
        
        emotional_resonance = defaultdict(int)
        
        # Simple emotion detection (could be enhanced with NLP libraries)
        emotion_words = {
            'wonder': ['wonder', 'amazing', 'incredible', 'awe-inspiring'],
            'awe': ['awe', 'magnificent', 'breathtaking', 'overwhelming'],
            'curiosity': ['curious', 'explore', 'investigate', 'discover'],
            'joy': ['joy', 'happy', 'delight', 'bliss', 'ecstasy'],
            'peace': ['peace', 'calm', 'tranquil', 'serene'],
            'fear': ['fear', 'afraid', 'terror', 'dread'],
            'anger': ['anger', 'rage', 'fury', 'frustrated'],
            'sadness': ['sad', 'melancholy', 'grief', 'sorrow']
        }
        
        for emotion, words in emotion_words.items():
            for word in words:
                if word in prompt:
                    emotional_resonance[emotion] += prompt.count(word)
        
        # Find primary emotional frequency
        primary_emotion = max(emotional_resonance, key=emotional_resonance.get) if emotional_resonance else 'neutral'
        primary_frequency = self.emotional_frequencies.get(primary_emotion, 528)  # Default to love frequency
        
        # Create resonance map
        resonance_map = {}
        for emotion, count in emotional_resonance.items():
            if count > 0:
                resonance_map[emotion] = {
                    'frequency': self.emotional_frequencies[emotion],
                    'intensity': count,
                    'resonance': count / max(len(prompt.split()), 1)
                }
        
        return {
            'primary_emotion': primary_emotion,
            'primary_frequency': primary_frequency,
            'resonance_map': resonance_map
        }
    
    def _generate_intent_vectors(self, 
                               synesthetic_analysis: Dict,
                               associative_analysis: Dict,
                               temporal_analysis: Dict,
                               cosmic_analysis: Dict,
                               emotional_analysis: Dict) -> Dict[str, List[float]]:
        """Generate intent vectors for IntentSim configuration."""
        
        # Create multi-dimensional intent vectors
        intent_vectors = {}
        
        # Synesthetic vector (cross-modal integration)
        synesthetic_strength = synesthetic_analysis['strength']
        intent_vectors['synesthetic'] = [
            synesthetic_strength,
            synesthetic_strength * 0.8,  # Secondary resonance
            synesthetic_strength * 0.6,  # Tertiary harmonics
            synesthetic_strength * 0.4   # Base frequency
        ]
        
        # Associative vector (connection density)
        associative_density = associative_analysis['density']
        intent_vectors['associative'] = [
            associative_density,
            associative_density * 0.7,
            associative_density * 0.5,
            associative_density * 0.3
        ]
        
        # Temporal vector (non-linear time perception)
        temporal_nonlinearity = temporal_analysis['nonlinearity']
        intent_vectors['temporal'] = [
            temporal_nonlinearity,
            temporal_nonlinearity * 0.9,
            temporal_nonlinearity * 0.7,
            temporal_nonlinearity * 0.5
        ]
        
        # Cosmic archetype vector
        archetype_scores = cosmic_analysis['archetypes']
        max_archetype_score = max(archetype_scores.values()) if archetype_scores else 1.0
        normalized_scores = [score / max_archetype_score for score in archetype_scores.values()]
        
        # Pad or truncate to 4 dimensions
        while len(normalized_scores) < 4:
            normalized_scores.append(0.0)
        intent_vectors['cosmic'] = normalized_scores[:4]
        
        # Emotional frequency vector
        resonance_map = emotional_analysis['resonance_map']
        if resonance_map:
            frequencies = [data['resonance'] for data in resonance_map.values()]
            while len(frequencies) < 4:
                frequencies.append(0.0)
            intent_vectors['emotional'] = frequencies[:4]
        else:
            intent_vectors['emotional'] = [0.528, 0.0, 0.0, 0.0]  # Default love frequency
        
        # Composite vector (weighted combination)
        composite = []
        for i in range(4):
            composite_value = (
                intent_vectors['synesthetic'][i] * 0.25 +
                intent_vectors['associative'][i] * 0.25 +
                intent_vectors['temporal'][i] * 0.2 +
                intent_vectors['cosmic'][i] * 0.15 +
                intent_vectors['emotional'][i] * 0.15
            )
            composite.append(composite_value)
        
        intent_vectors['composite'] = composite
        
        return intent_vectors
    
    def extract_cosmic_keywords(self, prompt: str) -> List[str]:
        """Extract cosmic-relevant keywords for target generation."""
        
        cosmic_keywords = []
        
        # Astronomical objects and phenomena
        astro_patterns = [
            r'\b(galaxy|galaxies|star|stars|planet|planets|nebula|nebulae)\b',
            r'\b(black hole|white dwarf|neutron star|pulsar|quasar)\b',
            r'\b(supernova|cosmic|universe|cosmos|space|void)\b',
            r'\b(dark matter|dark energy|quantum|gravitational)\b',
            r'\b(jwst|hubble|telescope|observation|discovery)\b'
        ]
        
        for pattern in astro_patterns:
            matches = re.findall(pattern, prompt.lower())
            cosmic_keywords.extend(matches)
        
        # Unique keywords only
        return list(set(cosmic_keywords))
    
    def generate_target_hints(self, processed_prompt: Dict) -> List[str]:
        """Generate hints for cosmic target generation based on processed prompt."""
        
        hints = []
        
        # Based on dominant archetype
        dominant_archetype = processed_prompt.get('dominant_archetype', 'none')
        
        if dominant_archetype == 'creation':
            hints.extend([
                "early universe structures",
                "primordial galaxy formation",
                "first stars and stellar nurseries",
                "cosmic microwave background anomalies"
            ])
        elif dominant_archetype == 'memory':
            hints.extend([
                "ancient light preservation",
                "quantum information storage",
                "gravitational memory effects",
                "cosmic archaeological sites"
            ])
        elif dominant_archetype == 'consciousness':
            hints.extend([
                "observer effect manifestations",
                "quantum consciousness signatures",
                "information processing centers",
                "cosmic awareness indicators"
            ])
        elif dominant_archetype == 'connection':
            hints.extend([
                "quantum entanglement networks",
                "cosmic web structures",
                "non-local correlation phenomena",
                "universal connection points"
            ])
        elif dominant_archetype == 'transformation':
            hints.extend([
                "morphing cosmic structures",
                "phase transition regions",
                "evolutionary boundaries",
                "metamorphosis zones"
            ])
        elif dominant_archetype == 'mystery':
            hints.extend([
                "anomalous cosmic phenomena",
                "impossible early structures",
                "paradoxical observations",
                "hidden cosmic mechanics"
            ])
        
        # Based on synesthetic strength
        if processed_prompt.get('synesthetic_strength', 0) > 0.5:
            hints.extend([
                "multi-spectral anomalies",
                "cross-modal cosmic phenomena",
                "synesthetic cosmic signatures",
                "integrated sensory manifestations"
            ])
        
        # Based on temporal non-linearity
        if processed_prompt.get('temporal_nonlinearity', 0) > 0.5:
            hints.extend([
                "temporal loop structures",
                "causality-defying regions",
                "time-reversed phenomena",
                "non-linear temporal effects"
            ])
        
        return hints