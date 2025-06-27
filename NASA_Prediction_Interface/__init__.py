"""
NASA Prediction Interface
========================

A NASA prediction interface that leverages the Mezquia Physics framework and IntentSim simulation logic
to predict 'memory recovery' events and prioritize cosmic targets for future observation.

© 2025 TheVoidIntent LLC — Mezquia Physics Genesis Archive
Watermarked and timestamped for Mezquia Physics provenance.
"""

__version__ = "1.0.0"
__author__ = "Marcelo Mezquia / TheVoidIntent LLC"
__copyright__ = "© 2025 TheVoidIntent LLC - Mezquia Physics Genesis Archive"

from .cosmic_predictor import CosmicMemoryPredictor
from .prompt_processor import NeuroAssociativePromptProcessor
from .memory_recovery import MemoryRecoveryEngine
from .target_prioritizer import CosmicTargetPrioritizer

__all__ = [
    'CosmicMemoryPredictor',
    'NeuroAssociativePromptProcessor', 
    'MemoryRecoveryEngine',
    'CosmicTargetPrioritizer'
]