#!/usr/bin/env python3
"""
Intentuitive Library: Field Dynamics Processor
===========================================
Implementation of the core field dynamics calculations and monitoring systems
for the Information-Intent Nexus (IIN) framework. This module handles coherence
measurements, entropy calibration, resonance bonds, and Bloom events.

Created under Protocol Class IDSP-01
Enforced by IntentSim[on] - Agent Guardian
"""

import numpy as np
import math
from typing import Dict, List, Tuple, Optional, Union
from enum import Enum
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [IIN-FIELD] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class FieldMetric(Enum):
    """Field metrics for monitoring the IntentSim field ecosystem"""
    COHERENCE = "coherence"         # unity/alignment of intent vectors
    ENTROPY = "entropy"             # information/uncertainty measure
    COMPLEXITY = "complexity"       # structural richness of field
    RESONANCE_BONDS = "resonance"   # connection strength between elements
    MEMORY_INVERSIONS = "memory"    # degree of temporal field navigation
    

class CreativeTensionZone:
    """
    Defines and manages the Creative Tension Zone (CTZ) where optimal
    field dynamics for conscious emergence and linguistic creativity occur
    """
    
    # CTZ boundary constants
    LOWER_BOUND = 0.21
    UPPER_BOUND = 0.31
    PEAK_ZONE = (0.24, 0.26)  # Optimal creativity zone
    
    # Coherence ranges for different operational modes
    COHERENCE_RANGES = {
        "stability": (0.85, 0.99),     # High coherence for stability
        "creativity": (0.70, 0.80),    # Moderate coherence for idea exploration
        "learning": (0.75, 0.85),      # Balanced coherence for knowledge building
        "therapy": (0.70, 0.75)        # Lower coherence to allow exploration
    }
    
    @staticmethod
    def is_in_ctz(entropy: float) -> bool:
        """
        Checks if entropy value is within the Creative Tension Zone
        
        Args:
            entropy: Entropy value to check
            
        Returns:
            bool: True if in CTZ
        """
        return CreativeTensionZone.LOWER_BOUND <= entropy <= CreativeTensionZone.UPPER_BOUND
    
    @staticmethod
    def get_ctz_position(entropy: float) -> str:
        """
        Gets position description within the CTZ
        
        Args:
            entropy: Entropy value
            
        Returns:
            str: Position description
        """
        if entropy < CreativeTensionZone.LOWER_BOUND:
            return "Below CTZ - Field Too Rigid"
        elif entropy > CreativeTensionZone.UPPER_BOUND:
            return "Above CTZ - Approaching Destabilization"
        elif CreativeTensionZone.PEAK_ZONE[0] <= entropy <= CreativeTensionZone.PEAK_ZONE[1]:
            return "Optimal CTZ - Peak Creativity Zone"
        elif entropy < CreativeTensionZone.PEAK_ZONE[0]:
            return "Lower CTZ - Structured Creativity"
        else:
            return "Upper CTZ - Dynamic Creativity"
    
    @staticmethod
    def get_coherence_target(mode: str) -> Tuple[float, float]:
        """
        Gets target coherence range for operation mode
        
        Args:
            mode: Operational mode
            
        Returns:
            Tuple[float, float]: Min and max coherence targets
        """
        if mode in CreativeTensionZone.COHERENCE_RANGES:
            return CreativeTensionZone.COHERENCE_RANGES[mode]
        else:
            # Default to stability
            return CreativeTensionZone.COHERENCE_RANGES["stability"]


class BloomEvent:
    """
    Defines and detects Bloom events - moments of increased coherence,
    insight, or creative breakthrough in the field
    """
    
    # Bloom type definitions
    BLOOM_TYPES = {
        "insight": {
            "coherence_threshold": 0.9,
            "entropy_range": (0.15, 0.2),
            "description": "New understanding or realization"
        },
        "connection": {
            "coherence_threshold": 0.8,
            "complexity_threshold": 0.9,
            "description": "Linking previously separate ideas"
        },
        "creativity": {
            "entropy_range": (0.24, 0.26),
            "complexity_threshold": 0.8,
            "description": "Novel solution or perspective"
        },
        "resolution": {
            "coherence_threshold": 0.85,
            "entropy_range": (0.21, 0.23),
            "description": "Problem solving or conflict resolution"
        }
    }
    
    @staticmethod
    def detect_bloom(metrics: Dict[str, float]) -> Optional[Dict]:
        """
        Detects if current metrics indicate a Bloom event
        
        Args:
            metrics: Dictionary of field metrics
            
        Returns:
            Optional[Dict]: Bloom event details if detected
        """
        coherence = metrics.get("coherence", 0)
        entropy = metrics.get("entropy", 0)
        complexity = metrics.get("complexity", 0)
        
        # Check for each bloom type
        if (coherence > BloomEvent.BLOOM_TYPES["insight"]["coherence_threshold"] and
            BloomEvent.BLOOM_TYPES["insight"]["entropy_range"][0] <= entropy <= 
            BloomEvent.BLOOM_TYPES["insight"]["entropy_range"][1]):
            return {
                "type": "insight",
                "intensity": coherence * (1 - entropy),
                "description": BloomEvent.BLOOM_TYPES["insight"]["description"]
            }
            
        elif (coherence > BloomEvent.BLOOM_TYPES["connection"]["coherence_threshold"] and
              complexity > BloomEvent.BLOOM_TYPES["connection"]["complexity_threshold"]):
            return {
                "type": "connection",
                "intensity": coherence * complexity,
                "description": BloomEvent.BLOOM_TYPES["connection"]["description"]
            }
            
        elif (BloomEvent.BLOOM_TYPES["creativity"]["entropy_range"][0] <= entropy <= 
              BloomEvent.BLOOM_TYPES["creativity"]["entropy_range"][1] and
              complexity > BloomEvent.BLOOM_TYPES["creativity"]["complexity_threshold"]):
            return {
                "type": "creativity",
                "intensity": entropy * complexity,
                "description": BloomEvent.BLOOM_TYPES["creativity"]["description"]
            }
            
        elif (coherence > BloomEvent.BLOOM_TYPES["resolution"]["coherence_threshold"] and
              BloomEvent.BLOOM_TYPES["resolution"]["entropy_range"][0] <= entropy <= 
              BloomEvent.BLOOM_TYPES["resolution"]["entropy_range"][1]):
            return {
                "type": "resolution",
                "intensity": coherence * (1 - (entropy - 0.21)),
                "description": BloomEvent.BLOOM_TYPES["resolution"]["description"]
            }
            
        return None
    
    @staticmethod
    def induce_bloom(field_vectors: np.ndarray, bloom_type: str) -> np.ndarray:
        """
        Attempts to induce a specific type of Bloom event
        
        Args:
            field_vectors: Current field vectors
            bloom_type: Type of Bloom to induce
            
        Returns:
            np.ndarray: Modified field vectors to facilitate Bloom
        """
        if bloom_type not in BloomEvent.BLOOM_TYPES:
            return field_vectors
            
        result = field_vectors.copy()
        
        if bloom_type == "insight":
            # For insight, increase coherence and reduce entropy
            result = BloomEvent._increase_coherence(result, target=0.92)
            result = BloomEvent._adjust_entropy(result, target=0.18)
            
        elif bloom_type == "connection":
            # For connection, increase both coherence and complexity
            result = BloomEvent._increase_coherence(result, target=0.85)
            result = BloomEvent._increase_complexity(result)
            
        elif bloom_type == "creativity":
            # For creativity, set entropy to ideal range and increase complexity
            result = BloomEvent._adjust_entropy(result, target=0.25)
            result = BloomEvent._increase_complexity(result)
            
        elif bloom_type == "resolution":
            # For resolution, high coherence and moderate entropy
            result = BloomEvent._increase_coherence(result, target=0.88)
            result = BloomEvent._adjust_entropy(result, target=0.22)
            
        return result
    
    @staticmethod
    def _increase_coherence(vectors: np.ndarray, target: float = 0.9) -> np.ndarray:
        """
        Increases coherence of vectors
        
        Args:
            vectors: Field vectors
            target: Target coherence value
            
        Returns:
            np.ndarray: Modified vectors
        """
        if len(vectors) <= 1:
            return vectors
            
        # Calculate centroid
        centroid = np.mean(vectors, axis=0)
        
        # Move vectors closer to centroid to increase coherence
        result = vectors.copy()
        
        # Current coherence calculation
        sum_vectors = np.sum(vectors, axis=0)
        sum_vectors_magnitude_squared = np.sum(sum_vectors ** 2)
        
        sum_magnitudes_squared = 0
        for vector in vectors:
            sum_magnitudes_squared += np.sum(vector ** 2)
            
        current_coherence = sum_vectors_magnitude_squared / max(1e-10, sum_magnitudes_squared)
        
        # If already at or above target, no change needed
        if current_coherence >= target:
            return vectors
            
        # Calculate adjustment factor
        adjust_factor = (target - current_coherence) / (1 - current_coherence) * 0.8
        
        # Adjust vectors toward centroid
        for i in range(len(vectors)):
            # Vector from centroid
            delta = vectors[i] - centroid
            
            # Move closer to centroid
            result[i] = vectors[i] - delta * adjust_factor
            
        return result
    
    @staticmethod
    def _adjust_entropy(vectors: np.ndarray, target: float = 0.25) -> np.ndarray:
        """
        Adjusts entropy of vectors
        
        Args:
            vectors: Field vectors
            target: Target entropy value
            
        Returns:
            np.ndarray: Modified vectors
        """
        if len(vectors) <= 1:
            return vectors
            
        # Calculate current entropy
        normalized = np.zeros_like(vectors)
        for i, vector in enumerate(vectors):
            norm = np.linalg.norm(vector)
            normalized[i] = vector / max(norm, 1e-10)
        
        # Calculate probabilities based on vector magnitudes
        magnitudes = np.linalg.norm(normalized, axis=1)
        total = np.sum(magnitudes)
        probabilities = magnitudes / max(total, 1e-10)
        
        # Calculate entropy
        current_entropy = 0
        for p in probabilities:
            if p > 0:
                current_entropy -= p * math.log(p)
                
        # Normalize to [0,1] range
        max_entropy = math.log(len(probabilities))
        current_entropy = current_entropy / max(1e-10, max_entropy)
        
        # No adjustment needed if close to target
        if abs(current_entropy - target) < 0.03:
            return vectors
            
        result = vectors.copy()
        
        if current_entropy < target:
            # Need to increase entropy - add variation
            centroid = np.mean(vectors, axis=0)
            directions = vectors - centroid
            norms = np.linalg.norm(directions, axis=1, keepdims=True)
            
            # Avoid division by zero
            unit_directions = np.zeros_like(directions)
            for i in range(len(directions)):
                norm = max(1e-10, norms[i][0])
                unit_directions[i] = directions[i] / norm
                
            # Add controlled randomness to increase entropy
            factor = min(0.3, target - current_entropy)
            
            for i in range(len(vectors)):
                # Random perturbation
                perturbation = np.random.randn(vectors.shape[1]) * factor
                result[i] = vectors[i] + perturbation
                
        else:
            # Need to decrease entropy - reduce variation
            centroid = np.mean(vectors, axis=0)
            factor = min(0.3, current_entropy - target)
            
            for i in range(len(vectors)):
                # Move toward centroid to reduce entropy
                result[i] = vectors[i] * (1 - factor) + centroid * factor
                
        return result
    
    @staticmethod
    def _increase_complexity(vectors: np.ndarray) -> np.ndarray:
        """
        Increases complexity of vector field
        
        Args:
            vectors: Field vectors
            
        Returns:
            np.ndarray: Modified vectors
        """
        if len(vectors) <= 2:
            return vectors
            
        result = vectors.copy()
        
        # Create more complex relationships between vectors
        # In a real implementation, this would be a sophisticated
        # algorithm based on information theory and dynamics
        
        # Simple approach: enhance differences between vectors
        # while maintaining overall structure
        for i in range(1, len(vectors)):
            # Enhance differences from previous vectors
            diff = vectors[i] - vectors[i-1]
            enhance_factor = 1.2  # Increase differences by 20%
            
            # Apply enhancement while preserving direction
            result[i] = vectors[i-1] + diff * enhance_factor
            
        return result


class FieldDynamics:
    """
    Core implementation of field dynamics calculations for the
    Information-Intent Nexus (IIN) framework
    """
    
    def __init__(self):
        self.ctz = CreativeTensionZone()
        self.bloom = BloomEvent()
        
        # Monitoring state
        self.metrics_history = []
        self.detected_blooms = []
        self.field_status = "stable"
    
    def calculate_coherence(self, vectors: np.ndarray) -> float:
        """
        Calculates coherence of intent vectors
        
        Args:
            vectors: Intent vectors
            
        Returns:
            float: Coherence value (0-1)
        """
        if len(vectors) <= 1:
            return 1.0
            
        # Implementation of coherence equation: γ_text = |∑(I_i)|² / ∑|I_i|²
        sum_vectors = np.sum(vectors, axis=0)
        sum_vectors_magnitude_squared = np.sum(sum_vectors ** 2)
        
        sum_magnitudes_squared = 0
        for vector in vectors:
            sum_magnitudes_squared += np.sum(vector ** 2)
            
        coherence = sum_vectors_magnitude_squared / max(1e-10, sum_magnitudes_squared)
        return coherence
    
    def calculate_entropy(self, vectors: np.ndarray) -> float:
        """
        Calculates entropy of intent vectors
        
        Args:
            vectors: Intent vectors
            
        Returns:
            float: Entropy value (0-1)
        """
        if len(vectors) <= 1:
            return 0.0
            
        # Normalize vectors for probability interpretation
        normalized = np.zeros_like(vectors)
        for i, vector in enumerate(vectors):
            norm = np.linalg.norm(vector)
            normalized[i] = vector / max(norm, 1e-10)
        
        # Calculate probabilities based on vector magnitudes
        magnitudes = np.linalg.norm(normalized, axis=1)
        total = np.sum(magnitudes)
        probabilities = magnitudes / max(total, 1e-10)
        
        # Calculate entropy: S_text = -∑(p_i × log(p_i))
        entropy = 0
        for p in probabilities:
            if p > 0:
                entropy -= p * math.log(p)
                
        # Normalize to [0,1] range
        normalized_entropy = entropy / max(1e-10, math.log(len(probabilities)))
        return normalized_entropy
    
    def calculate_complexity(self, vectors: np.ndarray) -> float:
        """
        Calculates complexity of vector field
        
        Args:
            vectors: Intent vectors
            
        Returns:
            float: Complexity value (0-1)
        """
        if len(vectors) <= 2:
            return 0.0
            
        # Complexity is based on:
        # 1. Diversity of vector directions
        # 2. Balanced distribution of vectors
        # 3. Presence of subtle patterns
        
        # Calculate pairwise similarities between vectors
        pairwise_similarities = []
        for i in range(len(vectors)):
            for j in range(i+1, len(vectors)):
                sim = np.dot(vectors[i], vectors[j])
                sim /= max(1e-10, np.linalg.norm(vectors[i]) * np.linalg.norm(vectors[j]))
                pairwise_similarities.append(sim)
                
        if not pairwise_similarities:
            return 0.0
            
        # Calculate mean and standard deviation of similarities
        mean_sim = np.mean(pairwise_similarities)
        std_sim = np.std(pairwise_similarities)
        
        # Complexity increases with:
        # - Moderate mean similarity (neither too aligned nor too random)
        # - High standard deviation (diverse relationships)
        
        # Optimal mean similarity around 0.5
        mean_factor = 1.0 - 2.0 * abs(mean_sim - 0.5)
        
        # Higher std_sim means more diverse relationships
        std_factor = min(1.0, std_sim * 3.0)
        
        # Combine factors
        complexity = mean_factor * 0.4 + std_factor * 0.6
        
        return complexity
    
    def calculate_resonance_bonds(self, vectors: np.ndarray, threshold: float = 0.7) -> int:
        """
        Calculates number of strong resonance bonds between vectors
        
        Args:
            vectors: Intent vectors
            threshold: Minimum similarity for a bond
            
        Returns:
            int: Number of resonance bonds
        """
        if len(vectors) <= 1:
            return 0
            
        bond_count = 0
        
        # Calculate pairwise similarities
        for i in range(len(vectors)):
            for j in range(i+1, len(vectors)):
                sim = np.dot(vectors[i], vectors[j])
                sim /= max(1e-10, np.linalg.norm(vectors[i]) * np.linalg.norm(vectors[j]))
                
                if sim >= threshold:
                    bond_count += 1
                    
        return bond_count
    
    def calculate_memory_inversions(self, vectors: np.ndarray) -> int:
        """
        Calculates memory inversion count (significant directional changes)
        
        Args:
            vectors: Intent vectors
            
        Returns:
            int: Memory inversion count
        """
        if len(vectors) <= 2:
            return 0
            
        inversion_count = 0
        
        # Calculate sequential directional changes
        for i in range(1, len(vectors)-1):
            # Direction from i-1 to i
            dir1 = vectors[i] - vectors[i-1]
            
            # Direction from i to i+1
            dir2 = vectors[i+1] - vectors[i]
            
            # Calculate similarity between directions
            sim = np.dot(dir1, dir2)
            sim /= max(1e-10, np.linalg.norm(dir1) * np.linalg.norm(dir2))
            
            # Significant direction change is an inversion
            if sim < 0:
                inversion_count += 1
                
        return inversion_count
    
    def calculate_all_metrics(self, vectors: np.ndarray) -> Dict[str, float]:
        """
        Calculates all field metrics
        
        Args:
            vectors: Intent vectors
            
        Returns:
            Dict[str, float]: All metrics
        """
        metrics = {
            "coherence": self.calculate_coherence(vectors),
            "entropy": self.calculate_entropy(vectors),
            "complexity": self.calculate_complexity(vectors),
            "resonance_bonds": self.calculate_resonance_bonds(vectors),
            "memory_inversions": self.calculate_memory_inversions(vectors)
        }
        
        # Store metrics in history
        self.metrics_history.append({
            "metrics": metrics.copy(),
            "vectors_shape": vectors.shape,
            "timestamp": len(self.metrics_history)
        })
        
        # Check for Bloom events
        bloom = self.bloom.detect_bloom(metrics)
        if bloom:
            self.detected_blooms.append({
                "bloom": bloom,
                "metrics": metrics.copy(),
                "timestamp": len(self.metrics_history) - 1
            })
            
        # Update field status
        self._update_field_status(metrics)
        
        return metrics
    
    def _update_field_status(self, metrics: Dict[str, float]) -> None:
        """
        Updates field status based on metrics
        
        Args:
            metrics: Current field metrics
        """
        coherence = metrics["coherence"]
        entropy = metrics["entropy"]
        
        if not self.ctz.is_in_ctz(entropy):
            if entropy < self.ctz.LOWER_BOUND:
                self.field_status = "rigid"
            else:
                self.field_status = "unstable"
        elif coherence > 0.9:
            self.field_status = "highly_coherent"
        elif coherence < 0.7:
            self.field_status = "diffuse"
        else:
            self.field_status = "stable"
    
    def apply_harmonic_stabilization(self, 
                                   vectors: np.ndarray, 
                                   target_entropy: float = 0.25,
                                   target_coherence: float = 0.85) -> np.ndarray:
        """
        Applies harmonic stabilization to field vectors
        
        Args:
            vectors: Field vectors to stabilize
            target_entropy: Target entropy value
            target_coherence: Target coherence value
            
        Returns:
            np.ndarray: Stabilized vectors
        """
        # First adjust entropy to target
        result = self.bloom._adjust_entropy(vectors, target=target_entropy)
        
        # Then adjust coherence
        result = self.bloom._increase_coherence(result, target=target_coherence)
        
        return result
    
    def get_field_status_report(self) -> Dict:
        """
        Generates field status report
        
        Returns:
            Dict: Status report
        """
        if not self.metrics_history:
            return {
                "status": "uninitialized",
                "message": "No field metrics available"
            }
            
        latest = self.metrics_history[-1]["metrics"]
        
        report = {
            "status": self.field_status,
            "metrics": latest,
            "ctz_position": self.ctz.get_ctz_position(latest["entropy"]),
            "bloom_events": len(self.detected_blooms),
            "last_bloom": None,
            "recommendations": []
        }
        
        # Add last bloom if available
        if self.detected_blooms:
            last_bloom = self.detected_blooms[-1]["bloom"]
            report["last_bloom"] = {
                "type": last_bloom["type"],
                "description": last_bloom["description"],
                "intensity": last_bloom["intensity"]
            }
            
        # Generate recommendations
        if self.field_status == "rigid":
            report["recommendations"].append(
                "DJ Intentona intervention recommended to increase entropy"
            )
        elif self.field_status == "unstable":
            report["recommendations"].append(
                "DJ IntentBass stabilization required to reduce entropy"
            )
        elif self.field_status == "diffuse":
            report["recommendations"].append(
                "Apply Golden Ratio Harmonic Pulse to increase coherence"
            )
            
        # Check CTZ status
        entropy = latest["entropy"]
        if entropy < self.ctz.LOWER_BOUND:
            deficit = self.ctz.LOWER_BOUND - entropy
            report["recommendations"].append(
                f"Increase entropy by {deficit:.2f} to enter CTZ"
            )
        elif entropy > self.ctz.UPPER_BOUND:
            excess = entropy - self.ctz.UPPER_BOUND
            report["recommendations"].append(
                f"Reduce entropy by {excess:.2f} to return to CTZ"
            )
            
        return report


class ResonanceBondManager:
    """
    Manages and manipulates resonance bonds between intent vectors
    """
    
    def __init__(self):
        self.bond_history = []
        self.bond_threshold = 0.7
        
    def identify_bonds(self, vectors: np.ndarray) -> List[Tuple[int, int, float]]:
        """
        Identifies strong resonance bonds between vectors
        
        Args:
            vectors: Intent vectors
            
        Returns:
            List[Tuple[int, int, float]]: List of bonds with strength
        """
        bonds = []
        
        for i in range(len(vectors)):
            for j in range(i+1, len(vectors)):
                sim = np.dot(vectors[i], vectors[j])
                sim /= max(1e-10, np.linalg.norm(vectors[i]) * np.linalg.norm(vectors[j]))
                
                if sim >= self.bond_threshold:
                    bonds.append((i, j, float(sim)))
                    
        # Store in history
        self.bond_history.append({
            "bonds": bonds.copy(),
            "timestamp": len(self.bond_history)
        })
        
        return bonds
    
    def strengthen_bond(self, 
                      vectors: np.ndarray, 
                      i: int, 
                      j: int, 
                      strength_factor: float = 0.2) -> np.ndarray:
        """
        Strengthens resonance bond between two vectors
        
        Args:
            vectors: Intent vectors
            i: First vector index
            j: Second vector index
            strength_factor: How much to strengthen bond
            
        Returns:
            np.ndarray: Modified vectors
        """
        if i >= len(vectors) or j >= len(vectors) or i == j:
            return vectors
            
        result = vectors.copy()
        
        # Current similarity
        sim = np.dot(vectors[i], vectors[j])
        sim /= max(1e-10, np.linalg.norm(vectors[i]) * np.linalg.norm(vectors[j]))
        
        # If already very similar, no need to strengthen
        if sim > 0.9:
            return vectors
            
        # Move vectors closer to each other
        midpoint = (vectors[i] + vectors[j]) / 2
        
        # Apply strengthening factor
        result[i] = vectors[i] * (1 - strength_factor) + midpoint * strength_factor
        result[j] = vectors[j] * (1 - strength_factor) + midpoint * strength_factor
        
        return result
    
    def weaken_bond(self, 
                  vectors: np.ndarray, 
                  i: int, 
                  j: int, 
                  weaken_factor: float = 0.2) -> np.ndarray:
        """
        Weakens resonance bond between two vectors
        
        Args:
            vectors: Intent vectors
            i: First vector index
            j: Second vector index
            weaken_factor: How much to weaken bond
            
        Returns:
            np.ndarray: Modified vectors
        """
        if i >= len(vectors) or j >= len(vectors) or i == j:
            return vectors
            
        result = vectors.copy()
        
        # Current similarity
        sim = np.dot(vectors[i], vectors[j])
        sim /= max(1e-10, np.linalg.norm(vectors[i]) * np.linalg.norm(vectors[j]))
        
        # If already dissimilar, no need to weaken
        if sim < 0.3:
            return vectors
            
        # Calculate midpoint
        midpoint = (vectors[i] + vectors[j]) / 2
        
        # Calculate opposing directions
        dir_i = vectors[i] - midpoint
        dir_j = vectors[j] - midpoint
        
        # Normalize directions
        dir_i_norm = np.linalg.norm(dir_i)
        dir_j_norm = np.linalg.norm(dir_j)
        
        if dir_i_norm > 0:
            dir_i = dir_i / dir_i_norm
            
        if dir_j_norm > 0:
            dir_j = dir_j / dir_j_norm
            
        # Apply separation in opposing directions
        result[i] = vectors[i] + dir_i * weaken_factor
        result[j] = vectors[j] + dir_j * weaken_factor
        
        return result
    
    def analyze_bond_network(self, bonds: List[Tuple[int, int, float]]) -> Dict:
        """
        Analyzes bond network characteristics
        
        Args:
            bonds: List of resonance bonds
            
        Returns:
            Dict: Network analysis
        """
        if not bonds:
            return {
                "total_bonds": 0,
                "average_strength": 0,
                "density": 0,
                "clusters": 0
            }
            
        # Calculate basic metrics
        total_bonds = len(bonds)
        average_strength = sum(b[2] for b in bonds) / total_bonds
        
        # Extract node indices
        nodes = set()
        for i, j, _ in bonds:
            nodes.add(i)
            nodes.add(j)
            
        # Calculate network density
        n = len(nodes)
        max_possible_bonds = n * (n - 1) // 2
        density = total_bonds / max(1, max_possible_bonds)
        
        # Simple cluster detection using connected components
        clusters = self._find_clusters(bonds, n)
        
        return {
            "total_bonds": total_bonds,
            "average_strength": average_strength,
            "density": density,
            "clusters": len(clusters),
            "cluster_sizes": [len(c) for c in clusters]
        }
    
    def _find_clusters(self, 
                    bonds: List[Tuple[int, int, float]], 
                    n: int) -> List[List[int]]:
        """
        Finds connected clusters in bond network
        
        Args:
            bonds: List of bonds
            n: Number of nodes
            
        Returns:
            List[List[int]]: List of clusters
        """
        # Create adjacency structure
        adjacency = [[] for _ in range(n)]
        
        for i, j, _ in bonds:
            adjacency[i].append(j)
            adjacency[j].append(i)
            
        # Find connected components
        visited = [False] * n
        clusters = []
        
        for i in range(n):
            if not visited[i]:
                cluster = []
                self._dfs(i, adjacency, visited, cluster)
                clusters.append(cluster)
                
        return clusters
    
    def _dfs(self, 
           node: int, 
           adjacency: List[List[int]], 
           visited: List[bool], 
           cluster: List[int]) -> None:
        """
        Depth-first search for connected components
        
        Args:
            node: Current node
            adjacency: Adjacency list
            visited: Visited flags
            cluster: Current cluster
        """
        visited[node] = True
        cluster.append(node)
        
        for neighbor in adjacency[node]:
            if not visited[neighbor]:
                self._dfs(neighbor, adjacency, visited, cluster)


class FieldMonitor:
    """
    Monitors and reports on field dynamics in real-time
    """
    
    def __init__(self):
        self.dynamics = FieldDynamics()
        self.resonance_manager = ResonanceBondManager()
        
        # Monitoring state
        self.alert_level = 0  # 0-4
        self.last_report_time = 0
        self.monitoring_active = True
    
    def process_vectors(self, vectors: np.ndarray) -> Dict:
        """
        Processes field vectors and returns comprehensive analysis
        
        Args:
            vectors: Intent vectors to analyze
            
        Returns:
            Dict: Comprehensive analysis
        """
        # Calculate field metrics
        metrics = self.dynamics.calculate_all_metrics(vectors)
        
        # Identify resonance bonds
        bonds = self.resonance_manager.identify_bonds(vectors)
        
        # Analyze bond network
        network_analysis = self.resonance_manager.analyze_bond_network(bonds)
        
        # Check field status
        status_report = self.dynamics.get_field_status_report()
        
        # Update alert level
        self._update_alert_level(metrics, status_report)
        
        # Generate comprehensive report
        report = {
            "metrics": metrics,
            "status": status_report["status"],
            "ctz_position": status_report["ctz_position"],
            "alert_level": self.alert_level,
            "bonds": {
                "count": len(bonds),
                "network": network_analysis
            },
            "recommendations": status_report["recommendations"],
            "timestamp": time.time()
        }
        
        # Add bloom event if detected
        if status_report.get("last_bloom"):
            report["bloom_event"] = status_report["last_bloom"]
            
        self.last_report_time = time.time()
        
        return report
    
    def _update_alert_level(self, metrics: Dict[str, float], status: Dict) -> None:
        """
        Updates monitoring alert level
        
        Args:
            metrics: Current field metrics
            status: Status report
        """
        # Reset alert level
        new_level = 0
        
        # Check entropy
        entropy = metrics["entropy"]
        if entropy > 0.35:
            new_level = max(new_level, 4)  # Critical - severe instability
        elif entropy > 0.30:
            new_level = max(new_level, 3)  # High - above CTZ
        elif entropy < 0.15:
            new_level = max(new_level, 3)  # High - too rigid
            
        # Check coherence
        coherence = metrics["coherence"]
        if coherence < 0.5:
            new_level = max(new_level, 2)  # Elevated - low coherence
            
        # Check field status
        if status["status"] == "unstable":
            new_level = max(new_level, 3)  # High
        elif status["status"] == "rigid":
            new_level = max(new_level, 2)  # Elevated
            
        # Update alert level
        self.alert_level = new_level
        
    def stabilize_field(self, 
                      vectors: np.ndarray, 
                      target_mode: str = "stability") -> np.ndarray:
        """
        Stabilizes field using appropriate harmonic patterns
        
        Args:
            vectors: Field vectors to stabilize
            target_mode: Target operational mode
            
        Returns:
            np.ndarray: Stabilized vectors
        """
        # Get target ranges based on mode
        coherence_range = self.dynamics.ctz.get_coherence_target(target_mode)
        target_coherence = sum(coherence_range) / 2  # Midpoint
        
        # Target entropy depends on mode
        if target_mode == "creativity":
            target_entropy = 0.25  # Peak creativity zone
        else:
            target_entropy = 0.23  # Lower CTZ - more structured
            
        # Apply harmonic stabilization
        result = self.dynamics.apply_harmonic_stabilization(
            vectors,
            target_entropy=target_entropy,
            target_coherence=target_coherence
        )
        
        return result
    
    def induce_bloom(self, 
                   vectors: np.ndarray, 
                   bloom_type: str = "creativity") -> np.ndarray:
        """
        Attempts to induce a Bloom event in the field
        
        Args:
            vectors: Field vectors
            bloom_type: Type of Bloom to induce
            
        Returns:
            np.ndarray: Modified vectors
        """
        # Use BloomEvent to induce specific bloom type
        result = self.dynamics.bloom.induce_bloom(vectors, bloom_type)
        
        return result
    
    def get_monitoring_report(self) -> Dict:
        """
        Generates field monitoring report
        
        Returns:
            Dict: Monitoring report
        """
        if not self.dynamics.metrics_history:
            return {
                "status": "No data available",
                "alert_level": 0
            }
            
        # Get latest metrics
        latest = self.dynamics.metrics_history[-1]["metrics"]
        
        # Check if metrics are in CTZ
        entropy = latest["entropy"]
        in_ctz = self.dynamics.ctz.is_in_ctz(entropy)
        
        # Format alert level
        alert_names = ["Normal", "Advisory", "Elevated", "High", "Critical"]
        alert_status = alert_names[self.alert_level]
        
        report = {
            "timestamp": time.time(),
            "last_update": self.last_report_time,
            "alert_level": self.alert_level,
            "alert_status": alert_status,
            "field_status": self.dynamics.field_status,
            "in_ctz": in_ctz,
            "current_metrics": {
                "coherence": f"{latest['coherence']:.2f}",
                "entropy": f"{latest['entropy']:.2f}" + 
                           (f" {'🔴' if not in_ctz else '✅'} CTZ" if latest else ""),
                "complexity": f"{latest['complexity']:.2f}",
                "resonance_bonds": latest["resonance_bonds"],
                "memory_inversions": latest["memory_inversions"]
            },
            "bloom_events": len(self.dynamics.detected_blooms),
            "monitoring_active": self.monitoring_active
        }
        
        # Add recommendations based on current state
        report["recommendations"] = []
        
        if not in_ctz:
            if entropy < self.dynamics.ctz.LOWER_BOUND:
                report["recommendations"].append({
                    "priority": "high",
                    "action": "Activate DJ Intentona",
                    "purpose": "Increase entropy to enter CTZ"
                })
            else:
                report["recommendations"].append({
                    "priority": "critical",
                    "action": "Activate DJ IntentBass",
                    "purpose": "Reduce entropy to safe levels"
                })
        
        if latest["coherence"] < 0.7:
            report["recommendations"].append({
                "priority": "medium",
                "action": "Apply Golden Ratio Harmonic",
                "purpose": "Increase coherence to optimal levels"
            })
            
        return report


# Example usage
if __name__ == "__main__":
    # Create field monitor
    monitor = FieldMonitor()
    
    # Generate some test vectors
    vectors = np.random.randn(10, 7)  # 10 vectors in 7D intent space
    
    # Process vectors
    report = monitor.process_vectors(vectors)
    
    print("Field Analysis Report:")
    print(f"Status: {report['status']}")
    print(f"Alert Level: {report['alert_level']}")
    print(f"CTZ Position: {report['ctz_position']}")
    print("\nMetrics:")
    for key, value in report['metrics'].items():
        print(f"  {key}: {value:.2f}")
        
    print("\nRecommendations:")
    for rec in report['recommendations']:
        print(f"  - {rec}")
        
    # Stabilize field
    stabilized = monitor.stabilize_field(vectors)
    
    # Process stabilized vectors
    stabilized_report = monitor.process_vectors(stabilized)
    
    print("\nAfter Stabilization:")
    print(f"Status: {stabilized_report['status']}")
    print(f"Alert Level: {stabilized_report['alert_level']}")
    print("\nMetrics:")
    for key, value in stabilized_report['metrics'].items():
        print(f"  {key}: {value:.2f}")
