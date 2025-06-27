"""
IntentSim Integrated Prediction Model
=====================================
A standalone predictive model based on the IntentSim framework with neurobiological mappings.
Integrates Harmonic Bloom Cascade with predictive capabilities.

Author: Marcelo Mezquia | IntentSim
Version: 1.0
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import scipy.spatial as spatial
from typing import List, Tuple, Dict, Optional, Union, Callable
from enum import Enum
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
from scipy.ndimage import gaussian_filter
import os
import json


class DevelopmentalPhase(Enum):
    """Developmental phases in the model, inspired by neurodevelopment."""
    INITIALIZATION = 0
    BLOOM = 1
    PRUNING = 2
    RESONANCE = 3
    STABLE = 4


class NeurodevelopmentalPattern(Enum):
    """Known neurodevelopmental patterns for comparison and diagnosis."""
    TYPICAL = 0
    ASD_LIKE = 1
    ADHD_LIKE = 2
    SCHIZOPHRENIA_LIKE = 3
    DEPRESSION_LIKE = 4
    UNCLASSIFIED = 5


class IntentSimPredictor:
    """
    IntentSim Integrated Prediction Model that combines neurobiological simulations
    with predictive capabilities.
    """
    
    def __init__(self, 
                 dimensions: Tuple[int, int] = (100, 100),
                 agent_count: int = 150,
                 intent_strength: float = 0.1,
                 entropy_factor: float = 0.3,
                 information_density: float = 0.5,
                 field_decay_rate: float = 0.2,
                 field_propagation_speed: float = 1.0,
                 movement_speed: float = 0.5,
                 resonance_threshold: float = 0.1,
                 pruning_threshold: float = 0.05,
                 theta_oscillation_strength: float = 0.5,
                 gamma_oscillation_strength: float = 0.7,
                 critical_period_flexibility: float = 1.0,
                 dmn_baseline_activation: float = 0.3,
                 overpruning_risk_factor: float = 0.0,
                 hcp_connectivity_factor: float = 0.6,
                 narrative_salience_factor: float = 0.5,
                 random_seed: Optional[int] = None):
        """
        Initialize the IntentSim Predictor with neurobiological parameters.
        
        Parameters:
        -----------
        dimensions: Tuple[int, int]
            Size of the 2D field (width, height)
        agent_count: int
            Number of agents in the simulation
        intent_strength: float
            Strength of intent field interactions
        entropy_factor: float
            Amount of randomness in agent behavior
        information_density: float
            Base information content of agents
        field_decay_rate: float
            Rate at which field strength decays with distance
        field_propagation_speed: float
            Speed at which field effects propagate
        movement_speed: float
            Base speed of agent movement
        resonance_threshold: float
            Minimum field strength for resonant coupling
        pruning_threshold: float
            Threshold for pruning connections
        theta_oscillation_strength: float
            Strength of theta oscillations (3-8 Hz, memory binding)
        gamma_oscillation_strength: float
            Strength of gamma oscillations (30-100 Hz, local processing)
        critical_period_flexibility: float
            Initial flexibility of critical periods
        dmn_baseline_activation: float
            Default Mode Network baseline activation
        overpruning_risk_factor: float
            Risk factor for excessive pruning (0.0 = typical)
        hcp_connectivity_factor: float
            Human Connectome Project connectivity baseline
        narrative_salience_factor: float
            DAAN study-inspired narrative vs factual processing
        random_seed: Optional[int]
            Random seed for reproducibility
        """
        # Store parameters
        self.dimensions = dimensions
        self.agent_count = agent_count
        self.intent_strength = intent_strength
        self.entropy_factor = entropy_factor
        self.information_density = information_density
        self.field_decay_rate = field_decay_rate
        self.field_propagation_speed = field_propagation_speed
        self.movement_speed = movement_speed
        self.resonance_threshold = resonance_threshold
        self.pruning_threshold = pruning_threshold
        self.theta_oscillation_strength = theta_oscillation_strength
        self.gamma_oscillation_strength = gamma_oscillation_strength
        self.critical_period_flexibility = critical_period_flexibility
        self.dmn_baseline_activation = dmn_baseline_activation
        self.overpruning_risk_factor = overpruning_risk_factor
        self.hcp_connectivity_factor = hcp_connectivity_factor
        self.narrative_salience_factor = narrative_salience_factor
        
        # Set random seed if provided
        if random_seed is not None:
            np.random.seed(random_seed)
        
        # Initialize state variables
        self.agents = []
        self.connections = []
        self.field_grid = np.zeros(dimensions)
        self.timestep = 0
        self.current_phase = DevelopmentalPhase.INITIALIZATION
        self.history = {
            'complexity': [],
            'energy': [],
            'coherence': [],
            'agent_count': [],
            'connection_count': [],
            'dmn_activation': [],
            'theta_gamma_coupling': [],
            'pruning_rate': [],
            'critical_period_state': []
        }
        
        # Initialize neural oscillation state
        self.theta_phase = 0.0
        self.gamma_phase = 0.0
        self.dmn_activation = self.dmn_baseline_activation
        self.critical_period_state = 1.0  # Starts fully flexible
        
        # Create lookup tables for efficient sine calculations
        self.theta_sine_table = np.sin(np.linspace(0, 2*np.pi, 100))
        self.gamma_sine_table = np.sin(np.linspace(0, 2*np.pi, 100))
        
        # Human Connectome Project baseline connectivity
        self.hcp_baseline = self._generate_hcp_baseline()
        
        # Prediction models
        self.prediction_models = {}
        self.prediction_features = {}
        self.predicted_trajectories = {}
        
        # Pattern library for neurodevelopmental comparison
        self.pattern_library = self._initialize_pattern_library()
        
        # Initialize agents and connections
        self._initialize_agents()
        self._initialize_connections()
        
        # Spatial index for efficient neighbor queries
        self._update_spatial_index()
    
    def _initialize_agents(self) -> None:
        """
        Initialize agents with positions, intent values, and other properties.
        Based on neurodevelopmental principles like neurogenesis and initial connectivity.
        """
        self.agents = []
        
        # Create agents with neurobiologically-informed properties
        for i in range(self.agent_count):
            # Random position within dimensions
            x = np.random.uniform(0, self.dimensions[0])
            y = np.random.uniform(0, self.dimensions[1])
            
            # Initial intent: small random values
            intent = np.random.normal(0, 0.2)
            
            # Information content with narrative salience factor
            information = np.random.beta(
                2 * self.information_density, 
                2 * (1 - self.information_density)
            )
            
            # Higher narrative salience creates more variable information content
            if np.random.random() < self.narrative_salience_factor:
                information *= np.random.beta(3, 1)  # Narrative content has higher variance
            
            # Individual entropy (randomness)
            entropy = np.random.beta(
                1 + self.entropy_factor * 5, 
                1 + (1 - self.entropy_factor) * 5
            )
            
            # Initial resonance state
            resonance_state = 0.0
            
            # Theta-gamma coupling sensitivity
            theta_sensitivity = np.random.normal(1.0, 0.2)
            gamma_sensitivity = np.random.normal(1.0, 0.2)
            
            # DMN participation factor
            dmn_participation = np.random.beta(2, 2)
            
            # Executive function capacity 
            executive_function = np.random.beta(2, 2)
            
            # Individual pruning sensitivity (with overpruning risk factor)
            pruning_sensitivity = np.random.normal(
                1.0 + self.overpruning_risk_factor, 
                0.2 + self.overpruning_risk_factor * 0.3
            )
            
            # Create agent dictionary
            agent = {
                'id': i,
                'x': x,
                'y': y,
                'intent': intent,
                'information': information,
                'entropy': entropy,
                'resonance_state': resonance_state,
                'theta_sensitivity': theta_sensitivity,
                'gamma_sensitivity': gamma_sensitivity,
                'dmn_participation': dmn_participation,
                'executive_function': executive_function,
                'pruning_sensitivity': pruning_sensitivity,
                'neighbors': [],
                'history': {
                    'intent': [intent],
                    'resonance': [resonance_state]
                }
            }
            
            self.agents.append(agent)
    
    def _initialize_connections(self) -> None:
        """
        Initialize connections between agents based on proximity and HCP connectivity patterns.
        """
        self.connections = []
        
        # Compute distances between all agents
        positions = np.array([[agent['x'], agent['y']] for agent in self.agents])
        distances = spatial.distance.pdist(positions)
        distance_matrix = spatial.distance.squareform(distances)
        
        # Get connection probability from HCP baseline
        connection_probability = self.hcp_baseline.copy()
        
        # Add distance-based factor
        max_distance = np.max(distances)
        normalized_distances = distance_matrix / max_distance
        distance_factor = np.exp(-5 * normalized_distances)
        
        # Combine HCP and distance factors
        connection_probability = (
            self.hcp_connectivity_factor * connection_probability + 
            (1 - self.hcp_connectivity_factor) * distance_factor
        )
        
        # Create connections based on probability
        for i in range(self.agent_count):
            for j in range(i+1, self.agent_count):
                if np.random.random() < connection_probability[i, j]:
                    # Create connection with weight based on both agents' properties
                    weight = (
                        (1 + self.agents[i]['information']) * 
                        (1 + self.agents[j]['information']) * 
                        (1 - 0.5 * abs(self.agents[i]['intent'] - self.agents[j]['intent']))
                    )
                    
                    connection = {
                        'source': i,
                        'target': j,
                        'weight': weight,
                        'age': 0,
                        'narrative_content': np.random.random() < self.narrative_salience_factor
                    }
                    
                    self.connections.append(connection)
                    
                    # Update agent neighbor lists
                    self.agents[i]['neighbors'].append(j)
                    self.agents[j]['neighbors'].append(i)
    
    def _generate_hcp_baseline(self) -> np.ndarray:
        """
        Generate a baseline connectivity matrix based on Human Connectome Project principles.
        This models typical connectivity patterns in the human brain.
        
        Returns:
        --------
        np.ndarray: Connectivity probability matrix
        """
        # Create empty matrix
        connectivity = np.zeros((self.agent_count, self.agent_count))
        
        # Generate hub nodes (highly connected regions)
        hub_indices = np.random.choice(
            self.agent_count, 
            size=int(self.agent_count * 0.1), 
            replace=False
        )
        
        # Generate clusters/modules
        num_modules = 5
        module_assignments = np.random.randint(0, num_modules, size=self.agent_count)
        
        # Fill connectivity matrix based on:
        # 1. Module membership (higher within modules)
        # 2. Hub status (hubs connect to many nodes)
        # 3. Small-world properties (some random long-range connections)
        
        for i in range(self.agent_count):
            for j in range(i+1, self.agent_count):
                # Base probability
                p = 0.05
                
                # Increase probability for same module
                if module_assignments[i] == module_assignments[j]:
                    p += 0.3
                
                # Increase for hub nodes
                if i in hub_indices or j in hub_indices:
                    p += 0.2
                
                # Add small-world random connections
                if np.random.random() < 0.02:
                    p += 0.3
                
                connectivity[i, j] = p
                connectivity[j, i] = p
        
        return connectivity
    
    def _initialize_pattern_library(self) -> Dict:
        """
        Initialize the pattern library for neurodevelopmental comparison.
        
        Returns:
        --------
        Dict: Pattern library
        """
        # Create pattern templates based on neurodevelopmental research
        library = {}
        
        # Typical development pattern
        library[NeurodevelopmentalPattern.TYPICAL] = {
            'complexity_profile': 'sigmoidal',  # Gradually increases then plateaus
            'coherence_profile': 'increasing',  # Steadily increases
            'pruning_profile': 'bell',  # Bell-shaped curve with peak in middle
            'dmn_profile': 'increasing',  # Gradually increases
            'theta_gamma_profile': 'increasing',  # Coupling increases
            'critical_period_profile': 'decreasing',  # Gradually decreases
            'metrics': {
                'retention_ratio': 0.8,  # High retention of complexity
                'energy_efficiency': 1.2,  # Good efficiency
                'stability': 0.8  # High stability
            }
        }
        
        # ASD-like pattern
        library[NeurodevelopmentalPattern.ASD_LIKE] = {
            'complexity_profile': 'early_plateau',  # Rises fast, plateaus early
            'coherence_profile': 'low',  # Lower coherence
            'pruning_profile': 'reduced',  # Less pruning
            'dmn_profile': 'reduced',  # Reduced DMN activation
            'theta_gamma_profile': 'irregular',  # Irregular coupling
            'critical_period_profile': 'extended',  # Extended critical period
            'metrics': {
                'retention_ratio': 0.9,  # Very high retention (less pruning)
                'energy_efficiency': 0.9,  # Lower efficiency
                'stability': 0.7  # Moderate stability
            }
        }
        
        # ADHD-like pattern
        library[NeurodevelopmentalPattern.ADHD_LIKE] = {
            'complexity_profile': 'volatile',  # More ups and downs
            'coherence_profile': 'volatile',  # Variable coherence
            'pruning_profile': 'delayed',  # Delayed pruning
            'dmn_profile': 'volatile',  # Inconsistent DMN
            'theta_gamma_profile': 'reduced',  # Weaker coupling
            'critical_period_profile': 'extended',  # Somewhat extended
            'metrics': {
                'retention_ratio': 0.7,  # Moderate retention
                'energy_efficiency': 0.8,  # Lower efficiency
                'stability': 0.5  # Low stability
            }
        }
        
        # Schizophrenia-like pattern
        library[NeurodevelopmentalPattern.SCHIZOPHRENIA_LIKE] = {
            'complexity_profile': 'declining',  # Rises then declines
            'coherence_profile': 'declining',  # Decreases over time
            'pruning_profile': 'excessive',  # Too much pruning
            'dmn_profile': 'excessive',  # Overactive DMN
            'theta_gamma_profile': 'weak',  # Poor coupling
            'critical_period_profile': 'normal',  # Normal closure
            'metrics': {
                'retention_ratio': 0.5,  # Low retention (excessive pruning)
                'energy_efficiency': 0.7,  # Poor efficiency
                'stability': 0.4  # Low stability
            }
        }
        
        # Depression-like pattern
        library[NeurodevelopmentalPattern.DEPRESSION_LIKE] = {
            'complexity_profile': 'under_activated',  # Lower overall complexity
            'coherence_profile': 'moderate',  # Normal coherence
            'pruning_profile': 'moderate',  # Normal pruning
            'dmn_profile': 'excessive',  # Overactive DMN
            'theta_gamma_profile': 'moderate',  # Normal coupling
            'critical_period_profile': 'normal',  # Normal closure
            'metrics': {
                'retention_ratio': 0.75,  # Normal retention
                'energy_efficiency': 0.8,  # Somewhat lower efficiency
                'stability': 0.7  # Moderate stability
            }
        }
        
        return library
    
    def _update_spatial_index(self) -> None:
        """
        Update spatial index for efficient neighbor queries.
        """
        positions = np.array([[agent['x'], agent['y']] for agent in self.agents])
        self.spatial_tree = spatial.KDTree(positions)
    
    def calculate_field_value(self, x: float, y: float) -> float:
        """
        Calculate the intent field value at a given position.
        Integrates theta-gamma oscillations and resonance effects.
        
        Parameters:
        -----------
        x, y: float
            Position coordinates
        
        Returns:
        --------
        float: Field value at the specified position
        """
        # Use spatial index to find nearby agents efficiently
        query_point = np.array([x, y])
        nearby_indices = self.spatial_tree.query_ball_point(
            query_point, 
            10.0 / self.field_decay_rate
        )
        
        # Calculate field value from nearby agents
        field_value = 0.0
        
        for idx in nearby_indices:
            agent = self.agents[idx]
            
            # Calculate distance
            distance = np.sqrt((agent['x'] - x)**2 + (agent['y'] - y)**2)
            
            # Apply field propagation speed to model time-delay
            effective_distance = distance / self.field_propagation_speed
            
            # Calculate theta-gamma modulation
            oscillation_factor = (
                1.0 + 
                self.theta_oscillation_strength * agent['theta_sensitivity'] * 
                np.sin(self.theta_phase) +
                self.gamma_oscillation_strength * agent['gamma_sensitivity'] * 
                np.sin(self.gamma_phase * 5)
            )
            
            # If distance is not zero, add contribution
            if distance > 0:
                # Field contribution with decay and oscillation
                contribution = (
                    agent['intent'] * 
                    np.exp(-self.field_decay_rate * effective_distance) * 
                    (0.5 + agent['information']) * 
                    (1.0 + agent['resonance_state']) *
                    oscillation_factor
                )
                field_value += contribution
            else:
                # If at agent position, direct contribution
                contribution = (
                    agent['intent'] * 
                    (0.5 + agent['information']) * 
                    (1.0 + agent['resonance_state']) *
                    oscillation_factor
                )
                field_value += contribution
        
        return field_value
    
    def update_field_grid(self) -> None:
        """
        Update the entire field grid based on current agent states.
        """
        # Create new field grid
        new_grid = np.zeros(self.dimensions)
        
        # Calculate field value for each grid point
        # Note: For efficiency, could be optimized to calculate at lower resolution
        # and then interpolate
        grid_step = 5  # Calculate every 5 points and interpolate
        
        for i in range(0, self.dimensions[0], grid_step):
            for j in range(0, self.dimensions[1], grid_step):
                new_grid[i, j] = self.calculate_field_value(i, j)
        
        # Interpolate to fill the full grid
        if grid_step > 1:
            new_grid = gaussian_filter(new_grid, sigma=grid_step/2)
        
        self.field_grid = new_grid
    
    def update_agents(self) -> None:
        """
        Update agent positions and properties based on the intent field and interactions.
        This is the core function that models how agents respond to and modify the field.
        Phase-specific behaviors are implemented here.
        """
        # Update neural oscillations first
        self._update_oscillations()
        
        # Update DMN activation based on system state
        self._update_dmn_activation()
        
        # Update critical period state
        self._update_critical_period()
        
        # For each agent, calculate new position and properties
        for agent in self.agents:
            # Calculate field at current position
            current_field = self.calculate_field_value(agent['x'], agent['y'])
            
            # Get agent's neighbors
            neighbor_ids = agent['neighbors']
            neighbors = [self.agents[n_id] for n_id in neighbor_ids if n_id < len(self.agents)]
            
            # Calculate forces from neighbors
            force_x, force_y = 0.0, 0.0
            
            for neighbor in neighbors:
                # Calculate direction to neighbor
                dx = neighbor['x'] - agent['x']
                dy = neighbor['y'] - agent['y']
                
                # Calculate distance
                distance = np.sqrt(dx**2 + dy**2)
                
                # Skip if distance is zero
                if distance < 0.001:
                    continue
                
                # Normalize direction
                dx /= distance
                dy /= distance
                
                # Calculate force based on intent similarity
                intent_similarity = 1.0 - abs(agent['intent'] - neighbor['intent'])
                
                # Phase-specific force calculation
                if self.current_phase == DevelopmentalPhase.BLOOM:
                    # In bloom phase, encourage exploration and connection
                    force_strength = (
                        self.intent_strength * intent_similarity * 
                        (1.0 + self.critical_period_state)
                    )
                elif self.current_phase == DevelopmentalPhase.PRUNING:
                    # In pruning phase, segregate by intent
                    force_strength = (
                        self.intent_strength * (2.0 * intent_similarity - 1.0) * 
                        agent['pruning_sensitivity']
                    )
                elif self.current_phase == DevelopmentalPhase.RESONANCE:
                    # In resonance phase, keep similar intents together
                    force_strength = (
                        self.intent_strength * intent_similarity * 
                        (1.0 + agent['resonance_state'])
                    )
                else:
                    # Default force calculation
                    force_strength = self.intent_strength * intent_similarity
                
                # Add to total force
                force_x += force_strength * dx
                force_y += force_strength * dy
            
            # Calculate field gradient for field-based movement
            # Sample field at nearby points
            sample_distance = 1.0
            field_x_plus = self.calculate_field_value(agent['x'] + sample_distance, agent['y'])
            field_x_minus = self.calculate_field_value(agent['x'] - sample_distance, agent['y'])
            field_y_plus = self.calculate_field_value(agent['x'], agent['y'] + sample_distance)
            field_y_minus = self.calculate_field_value(agent['x'], agent['y'] - sample_distance)
            
            # Calculate gradient
            field_gradient_x = field_x_plus - field_x_minus
            field_gradient_y = field_y_plus - field_y_minus
            
            # Normalize gradient if not zero
            gradient_magnitude = np.sqrt(field_gradient_x**2 + field_gradient_y**2)
            if gradient_magnitude > 0.001:
                field_gradient_x /= gradient_magnitude
                field_gradient_y /= gradient_magnitude
            
            # Add field gradient force
            force_x += field_gradient_x * self.intent_strength
            force_y += field_gradient_y * self.intent_strength
            
            # Add entropy (random movement)
            # Phase-specific entropy adjustment
            phase_entropy = self.entropy_factor
            if self.current_phase == DevelopmentalPhase.BLOOM:
                phase_entropy *= 1.5  # More exploration during bloom
            elif self.current_phase == DevelopmentalPhase.PRUNING:
                phase_entropy *= 0.5  # Less randomness during pruning
            
            # Individualized entropy based on agent properties
            agent_entropy = agent['entropy'] * phase_entropy
            
            # DMN modulation of entropy
            dmn_modulation = 1.0 - self.dmn_activation * agent['dmn_participation']
            agent_entropy *= dmn_modulation
            
            # Apply random force
            force_x += np.random.normal(0, agent_entropy)
            force_y += np.random.normal(0, agent_entropy)
            
            # Calculate new position
            new_x = agent['x'] + force_x * self.movement_speed
            new_y = agent['y'] + force_y * self.movement_speed
            
            # Boundary conditions (wrap around)
            new_x = new_x % self.dimensions[0]
            new_y = new_y % self.dimensions[1]
            
            # Update agent position
            agent['x'] = new_x
            agent['y'] = new_y
            
            # Update intent based on field and phase
            field_influence = current_field * self.intent_strength
            
            if self.current_phase == DevelopmentalPhase.BLOOM:
                # In bloom phase, intents are more malleable
                intent_change = (
                    field_influence * 
                    self.critical_period_state * 
                    (1.0 + agent['theta_sensitivity'] * np.sin(self.theta_phase))
                )
            elif self.current_phase == DevelopmentalPhase.RESONANCE:
                # In resonance phase, strengthen existing intents
                intent_change = (
                    field_influence * 
                    agent['resonance_state'] * 
                    0.5 * (1.0 + np.sin(self.theta_phase))
                )
            else:
                # Default intent change
                intent_change = field_influence * 0.1
            
            # Executive function modulates intent stability
            intent_change *= (2.0 - agent['executive_function'])
            
            # Apply intent change
            agent['intent'] += intent_change
            
            # Update resonance state
            if current_field > self.resonance_threshold:
                # Resonance increases with field strength above threshold
                resonance_increase = (
                    (current_field - self.resonance_threshold) * 
                    0.1 * (1.0 + np.sin(self.theta_phase))
                )
                agent['resonance_state'] += resonance_increase
            else:
                # Resonance decays over time
                agent['resonance_state'] *= 0.95
            
            # Cap resonance state
            agent['resonance_state'] = min(1.0, max(0.0, agent['resonance_state']))
            
            # Save history
            agent['history']['intent'].append(agent['intent'])
            agent['history']['resonance'].append(agent['resonance_state'])
    
    def _update_oscillations(self) -> None:
        """
        Update neural oscillations (theta and gamma) that modulate the system.
        Models hippocampal theta-gamma coupling for memory encoding.
        """
        # Update theta phase (slow oscillation, 3-8 Hz)
        self.theta_phase += 0.1  # Advance phase
        if self.theta_phase > 2 * np.pi:
            self.theta_phase -= 2 * np.pi
        
        # Theta modulation from lookup table
        theta_idx = int((self.theta_phase / (2 * np.pi)) * 100) % 100
        theta_modulation = self.theta_sine_table[theta_idx] * self.theta_oscillation_strength
        
        # Gamma phase (fast oscillation, 30-100 Hz)
        # Coupled to theta phase (strongest at theta peaks)
        gamma_base = 0.5 + 0.5 * self.theta_sine_table[theta_idx]
        self.gamma_phase += 0.5 * (1 + gamma_base)
        if self.gamma_phase > 2 * np.pi:
            self.gamma_phase -= 2 * np.pi
        
        # Calculate theta-gamma coupling metric
        gamma_idx = int((self.gamma_phase / (2 * np.pi)) * 100) % 100
        gamma_amplitude = gamma_base * self.gamma_oscillation_strength * self.gamma_sine_table[gamma_idx]
        
        # Theta-gamma coupling strength
        coupling_strength = np.corrcoef([theta_modulation], [gamma_amplitude])[0, 1]
        self.history['theta_gamma_coupling'].append(abs(coupling_strength))
    
    def _update_dmn_activation(self) -> None:
        """
        Update Default Mode Network activation based on system state.
        DMN is more active during low external stimulation and modulates internal processing.
        """
        # Calculate average entropy as indicator of external stimulation
        avg_entropy = np.mean([agent['entropy'] for agent in self.agents])
        
        # DMN base activation by phase
        dmn_base_by_phase = {
            DevelopmentalPhase.INITIALIZATION: self.dmn_baseline_activation,
            DevelopmentalPhase.BLOOM: self.dmn_baseline_activation * 0.5,  # Lower during bloom
            DevelopmentalPhase.PRUNING: self.dmn_baseline_activation * 1.2,  # Higher during pruning
            DevelopmentalPhase.RESONANCE: self.dmn_baseline_activation * 1.5,  # Highest during resonance
            DevelopmentalPhase.STABLE: self.dmn_baseline_activation
        }
        
        # Calculate DMN activation (inverse relationship with entropy)
        dmn_base = dmn_base_by_phase[self.current_phase]
        self.dmn_activation = max(0, min(1, dmn_base + (1 - avg_entropy) * 0.5))
        
        # Also modulated by theta oscillation
        self.dmn_activation *= (1 + 0.2 * np.sin(self.theta_phase))
        
        # Record history
        self.history['dmn_activation'].append(self.dmn_activation)
    
    def _update_critical_period(self) -> None:
        """
        Update critical period state, which models developmental windows that close over time.
        Different phases have different effects on critical period closure.
        """
        # Phase-specific critical period decay rates
        cp_decay_rates = {
            DevelopmentalPhase.INITIALIZATION: 1.0,  # No decay
            DevelopmentalPhase.BLOOM: 0.999,  # Slow decay
            DevelopmentalPhase.PRUNING: 0.995,  # Medium decay
            DevelopmentalPhase.RESONANCE: 0.99,  # Faster decay
            DevelopmentalPhase.STABLE: 0.9975  # Slow decay in stable phase
        }
        
        # Apply decay based on current phase
        decay_rate = cp_decay_rates[self.current_phase]
        self.critical_period_state *= decay_rate
        
        # Modulate by user-set flexibility factor
        self.critical_period_state *= self.critical_period_flexibility
        
        # Record history
        self.history['critical_period_state'].append(self.critical_period_state)
    
    def _prune_connections(self) -> None:
        """
        Prune low-value connections during the reorganization phase.
        This models synaptic pruning in brain development: "use it or lose it" principle.
        Influenced by:
        - Individual pruning sensitivity
        - Intent alignment
        - Critical period state
        - Narrative vs factual content (DAAN study)
        """
        if len(self.connections) == 0:
            return
        
        # Calculate connection strengths based on multiple factors
        connection_strengths = []
        pruning_candidates = []
        
        for i, connection in enumerate(self.connections):
            # Get connected agents
            source = self.agents[connection['source']]
            target = self.agents[connection['target']]
            
            # Calculate strength based on intent alignment
            intent_alignment = 1.0 - abs(source['intent'] - target['intent'])
            
            # Factor in resonance states
            resonance_factor = (1 + source['resonance_state']) * (1 + target['resonance_state'])
            
            # Higher pruning threshold for narrative content (DAAN study influence)
            content_factor = 1.2 if connection['narrative_content'] else 1.0
            
            # Individual pruning sensitivity from both agents
            pruning_sensitivity = (source['pruning_sensitivity'] + target['pruning_sensitivity']) / 2
            
            # Calculate final strength
            strength = (
                intent_alignment * 
                resonance_factor * 
                content_factor *
                connection['weight']
            )
            
            # Pruning threshold adjusted for individual sensitivity and overpruning risk
            adjusted_threshold = (
                self.pruning_threshold * 
                pruning_sensitivity * 
                (1 + self.overpruning_risk_factor)
            )
            
            connection_strengths.append(strength)
            
            # Flag for pruning if below threshold
            if strength < adjusted_threshold:
                pruning_candidates.append(i)
        
        # Record pruning rate 
        pruning_rate = len(pruning_candidates) / max(1, len(self.connections))
        self.history['pruning_rate'].append(pruning_rate)
        
        # Prune connections starting from the weakest
        # Sort in ascending order of strength
        pruning_candidates.sort(key=lambda idx: connection_strengths[idx])
        
        # Remove connections from the list (in reverse order to avoid index issues)
        connections_to_remove = []
        for idx in reversed(pruning_candidates):
            if idx < len(self.connections):  # Check bounds safety
                connection = self.connections[idx]
                connections_to_remove.append((idx, connection))
        
        # Actually remove the connections
        for idx, connection in connections_to_remove:
            # Remove from agent neighbor lists
            source_id = connection['source']
            target_id = connection['target']
            
            if source_id < len(self.agents) and target_id < len(self.agents):
                if target_id in self.agents[source_id]['neighbors']:
                    self.agents[source_id]['neighbors'].remove(target_id)
                
                if source_id in self.agents[target_id]['neighbors']:
                    self.agents[target_id]['neighbors'].remove(source_id)
        
        # Remove connections in reverse order to maintain indices
        for idx, _ in reversed(connections_to_remove):
            if idx < len(self.connections):  # Double-check bounds
                del self.connections[idx]
    
    def trigger_bloom(self, strength: float = 1.0) -> None:
        """
        Trigger a developmental bloom event where agents rapidly increase in complexity.
        
        Parameters:
        -----------
        strength: float
            Relative strength of the bloom event
        """
        # Set current phase to bloom
        self.current_phase = DevelopmentalPhase.BLOOM
        
        # For each agent, enhance intent and reduce entropy
        for agent in self.agents:
            # Increase intent strength
            intent_boost = np.random.normal(0, 0.5 * strength)
            agent['intent'] += intent_boost
            
            # Temporarily reduce entropy for more coordinated growth
            agent['entropy'] *= (1.0 - 0.3 * strength)
            
            # Reset resonance state for new growth
            agent['resonance_state'] = 0.0
        
        # Add new connections based on bloom strength
        self._add_bloom_connections(strength)
        
        # Update all metrics
        self.calculate_metrics()
    
    def _add_bloom_connections(self, strength: float) -> None:
        """
        Add new connections during bloom phase.
        
        Parameters:
        -----------
        strength: float
            Relative strength of the bloom event
        """
        # Number of new connections to add
        new_connection_count = int(self.agent_count * strength * 2)
        
        # Update spatial index for current positions
        self._update_spatial_index()
        
        # Get potential connections based on proximity
        for _ in range(new_connection_count):
            # Pick a random agent
            source_idx = np.random.randint(0, len(self.agents))
            source = self.agents[source_idx]
            
            # Find nearby agents that aren't already connected
            nearby_indices = self.spatial_tree.query_ball_point(
                [source['x'], source['y']], 
                10.0 / self.field_decay_rate
            )
            
            # Filter out existing neighbors and self
            potential_targets = [
                idx for idx in nearby_indices 
                if idx != source_idx and idx not in source['neighbors']
            ]
            
            if potential_targets:
                # Pick a random target
                target_idx = np.random.choice(potential_targets)
                target = self.agents[target_idx]
                
                # Create connection with weight based on both agents' properties
                weight = (
                    (1 + source['information']) * 
                    (1 + target['information']) * 
                    (1 - 0.5 * abs(source['intent'] - target['intent']))
                )
                
                connection = {
                    'source': source_idx,
                    'target': target_idx,
                    'weight': weight,
                    'age': 0,
                    'narrative_content': np.random.random() < self.narrative_salience_factor
                }
                
                self.connections.append(connection)
                
                # Update agent neighbor lists
                source['neighbors'].append(target_idx)
                target['neighbors'].append(source_idx)
    
    def transition_to_pruning(self) -> None:
        """
        Transition the system to the pruning phase where connections are selectively removed.
        """
        self.current_phase = DevelopmentalPhase.PRUNING
        
        # Increase sensitivity to intent differences during pruning
        for agent in self.agents:
            # Adjust entropy to focus on intent-based organization
            agent['entropy'] *= 0.7
    
    def transition_to_resonance(self) -> None:
        """
        Transition the system to the resonance phase where patterns are consolidated.
        """
        self.current_phase = DevelopmentalPhase.RESONANCE
        
        # Enhance resonance sensitivity for all agents
        for agent in self.agents:
            # Initial resonance boost based on field value at agent's position
            field_value = self.calculate_field_value(agent['x'], agent['y'])
            if field_value > self.resonance_threshold:
                agent['resonance_state'] += 0.2
    
    def transition_to_stable(self) -> None:
        """
        Transition the system to a stable phase after development is complete.
        """
        self.current_phase = DevelopmentalPhase.STABLE
    
    def calculate_metrics(self) -> Dict[str, float]:
        """
        Calculate metrics for the current state of the system.
        
        Returns:
        --------
        Dict[str, float]: Dictionary of metrics
        """
        # Calculate field coherence (gradient alignment)
        coherence = self._calculate_coherence()
        
        # Calculate field complexity
        complexity = self._calculate_complexity()
        
        # Calculate field energy
        energy = self._calculate_energy()
        
        # Store metrics in history
        self.history['complexity'].append(complexity)
        self.history['coherence'].append(coherence)
        self.history['energy'].append(energy)
        self.history['agent_count'].append(len(self.agents))
        self.history['connection_count'].append(len(self.connections))
        
        # Return current metrics
        return {
            'complexity': complexity,
            'coherence': coherence,
            'energy': energy,
            'agent_count': len(self.agents),
            'connection_count': len(self.connections),
            'dmn_activation': self.dmn_activation,
            'critical_period_state': self.critical_period_state
        }
    
    def _calculate_coherence(self) -> float:
        """
        Calculate field coherence, measuring how aligned agents are.
        
        Returns:
        --------
        float: Coherence value [0-1]
        """
        if len(self.agents) < 2:
            return 0.0
        
        # Calculate intent similarity between connected agents
        intent_diffs = []
        
        for connection in self.connections:
            source = self.agents[connection['source']]
            target = self.agents[connection['target']]
            intent_diff = abs(source['intent'] - target['intent'])
            intent_diffs.append(intent_diff)
        
        # If no connections, use a default measure
        if not intent_diffs:
            # Calculate average intent
            intents = [agent['intent'] for agent in self.agents]
            avg_intent = np.mean(intents)
            
            # Calculate average deviation from mean
            intent_diffs = [abs(intent - avg_intent) for intent in intents]
        
        # Convert differences to similarities
        intent_sims = [1.0 - min(1.0, diff) for diff in intent_diffs]
        
        # Coherence is average similarity
        coherence = np.mean(intent_sims)
        
        return coherence
    
    def _calculate_complexity(self) -> float:
        """
        Calculate field complexity based on agent relationships and patterns.
        
        Returns:
        --------
        float: Complexity value
        """
        if len(self.agents) < 2:
            return 0.0
        
        # Factors that contribute to complexity:
        
        # 1. Network complexity (connection patterns)
        network_complexity = 0.0
        if self.connections:
            # Create adjacency matrix
            adj_matrix = np.zeros((len(self.agents), len(self.agents)))
            for conn in self.connections:
                s, t = conn['source'], conn['target']
                if s < len(self.agents) and t < len(self.agents):
                    adj_matrix[s, t] = 1
                    adj_matrix[t, s] = 1
            
            # Calculate degree distribution
            degrees = np.sum(adj_matrix, axis=1)
            degree_entropy = self._calculate_entropy(degrees)
            
            # Calculate clustering coefficient for a sample of nodes
            sample_nodes = np.random.choice(
                len(self.agents), 
                min(20, len(self.agents)), 
                replace=False
            )
            
            clustering_coeffs = []
            for node in sample_nodes:
                neighbors = np.where(adj_matrix[node] > 0)[0]
                if len(neighbors) > 1:
                    possible_connections = len(neighbors) * (len(neighbors) - 1) / 2
                    actual_connections = 0
                    for i in range(len(neighbors)):
                        for j in range(i+1, len(neighbors)):
                            if adj_matrix[neighbors[i], neighbors[j]] > 0:
                                actual_connections += 1
                    
                    clustering = actual_connections / possible_connections if possible_connections > 0 else 0
                    clustering_coeffs.append(clustering)
            
            mean_clustering = np.mean(clustering_coeffs) if clustering_coeffs else 0
            
            # Network complexity combines degree entropy and clustering
            network_complexity = (degree_entropy + mean_clustering) / 2
        
        # 2. Spatial pattern complexity
        # Measure spatial clustering of agents
        positions = np.array([[agent['x'], agent['y']] for agent in self.agents])
        
        # Use k-means to identify clusters
        k = min(5, len(self.agents))
        
        # Manually compute a clustering metric
        spatial_complexity = 0.0
        if len(positions) > k:
            # Randomly select k agents as initial cluster centers
            center_indices = np.random.choice(len(positions), k, replace=False)
            centers = positions[center_indices]
            
            # Assign agents to clusters
            distances = np.zeros((len(positions), k))
            for i in range(k):
                distances[:, i] = np.sum((positions - centers[i])**2, axis=1)
            
            cluster_assignments = np.argmin(distances, axis=1)
            
            # Count agents in each cluster
            cluster_counts = np.zeros(k)
            for i in range(k):
                cluster_counts[i] = np.sum(cluster_assignments == i)
            
            # Calculate entropy of cluster sizes
            cluster_entropy = self._calculate_entropy(cluster_counts)
            
            # Calculate average distance to cluster centers
            avg_distances = []
            for i in range(k):
                cluster_positions = positions[cluster_assignments == i]
                if len(cluster_positions) > 0:
                    center = np.mean(cluster_positions, axis=0)
                    avg_dist = np.mean(np.sqrt(np.sum((cluster_positions - center)**2, axis=1)))
                    avg_distances.append(avg_dist)
            
            avg_distance = np.mean(avg_distances) if avg_distances else 0
            normalized_distance = avg_distance / np.sqrt(self.dimensions[0]**2 + self.dimensions[1]**2)
            
            # Spatial complexity combines cluster entropy and normalized distance
            spatial_complexity = (cluster_entropy + normalized_distance) / 2
        
        # 3. Intent pattern complexity
        intents = np.array([agent['intent'] for agent in self.agents])
        intent_complexity = self._calculate_entropy(intents)
        
        # 4. Information complexity
        info_values = np.array([agent['information'] for agent in self.agents])
        info_complexity = self._calculate_entropy(info_values)
        
        # Combine all factors
        complexity = (
            0.4 * network_complexity + 
            0.3 * spatial_complexity + 
            0.2 * intent_complexity + 
            0.1 * info_complexity
        )
        
        return complexity
    
    def _calculate_entropy(self, values: np.ndarray) -> float:
        """
        Calculate entropy of a distribution.
        
        Parameters:
        -----------
        values: np.ndarray
            Array of values
        
        Returns:
        --------
        float: Entropy value
        """
        if len(values) == 0:
            return 0.0
        
        # Normalize values to positive
        values = np.array(values)
        min_val = np.min(values)
        if min_val < 0:
            values = values - min_val
        
        # Add small constant to avoid log(0)
        values = values + 1e-10
        
        # Normalize to sum to 1
        total = np.sum(values)
        if total > 0:
            probabilities = values / total
        else:
            return 0.0
        
        # Calculate entropy
        entropy = -np.sum(probabilities * np.log(probabilities))
        
        # Normalize by maximum possible entropy
        max_entropy = np.log(len(values))
        if max_entropy > 0:
            normalized_entropy = entropy / max_entropy
        else:
            normalized_entropy = 0.0
        
        return normalized_entropy
    
    def _calculate_energy(self) -> float:
        """
        Calculate total field energy.
        
        Returns:
        --------
        float: Energy value
        """
        # Energy from field
        field_energy = np.sum(np.abs(self.field_grid))
        
        # Energy from agents
        agent_energy = sum(
            abs(agent['intent']) * (1 + agent['information'])
            for agent in self.agents
        )
        
        # Energy from connections
        connection_energy = sum(
            conn['weight'] for conn in self.connections
        )
        
        # Total energy
        total_energy = field_energy + agent_energy + connection_energy
        
        # Scale for consistent range
        scaled_energy = total_energy / (len(self.agents) + 1)
        
        return scaled_energy
    
    def run_single_step(self) -> Dict[str, float]:
        """
        Run a single timestep of the simulation.
        
        Returns:
        --------
        Dict[str, float]: Current metrics
        """
        # Update field
        self.update_field_grid()
        
        # Update agents
        self.update_agents()
        
        # If in pruning phase, prune connections
        if self.current_phase == DevelopmentalPhase.PRUNING:
            self._prune_connections()
        
        # Increment timestep
        self.timestep += 1
        
        # Calculate and return metrics
        return self.calculate_metrics()
    
    def run_simulation(self, steps: int, phase_schedule: Optional[Dict[int, DevelopmentalPhase]] = None) -> Dict:
        """
        Run the simulation for multiple timesteps with optional phase transitions.
        
        Parameters:
        -----------
        steps: int
            Number of timesteps to run
        phase_schedule: Optional[Dict[int, DevelopmentalPhase]]
            Dictionary mapping timesteps to phases for transitions
        
        Returns:
        --------
        Dict: Simulation results and metrics
        """
        if phase_schedule is None:
            phase_schedule = {}
        
        # Run for specified number of steps
        for step in range(steps):
            # Check for phase transition
            if step in phase_schedule:
                self.current_phase = phase_schedule[step]
            
            # Run single step
            self.run_single_step()
        
        # Return all metrics history
        return self.history
    
    def run_cascade(self, total_steps: int, bloom_timesteps: List[int]) -> Dict:
        """
        Run a Harmonic Bloom Cascade simulation with multiple bloom events.
        
        Parameters:
        -----------
        total_steps: int
            Total number of timesteps to run
        bloom_timesteps: List[int]
            Timesteps at which to trigger bloom events
        
        Returns:
        --------
        Dict: Simulation results and metrics
        """
        # Create phase schedule
        phase_schedule = {}
        
        # Schedule bloom events
        for bloom_time in bloom_timesteps:
            phase_schedule[bloom_time] = DevelopmentalPhase.BLOOM
            # Schedule pruning phase after each bloom (50 steps later)
            phase_schedule[bloom_time + 50] = DevelopmentalPhase.PRUNING
            # Schedule resonance phase after pruning (50 steps later)
            phase_schedule[bloom_time + 100] = DevelopmentalPhase.RESONANCE
        
        # Schedule final stable phase
        phase_schedule[total_steps - 50] = DevelopmentalPhase.STABLE
        
        # Run simulation with this schedule
        results = self.run_simulation(total_steps, phase_schedule)
        
        # After running, train prediction models
        self.train_prediction_models()
        
        # Generate predictions for future steps
        self.predict_future_trajectories(additional_steps=100)
        
        # Analyze results
        analysis = self.analyze_results()
        
        # Return results with analysis
        results.update({
            'analysis': analysis,
            'predictions': self.predicted_trajectories
        })
        
        return results
    
    def train_prediction_models(self) -> None:
        """
        Train machine learning models to predict future system metrics.
        """
        # Metrics to predict
        metrics = ['complexity', 'coherence', 'energy', 'dmn_activation']
        
        # Create feature matrix from history
        if len(self.history['complexity']) < 10:
            # Not enough data points to train
            return
        
        for metric in metrics:
            if metric not in self.history or len(self.history[metric]) < 10:
                continue
            
            # Create features (use past values as features)
            X = []
            y = []
            
            lookback = 5  # Use 5 past values as features
            
            for i in range(lookback, len(self.history[metric])):
                # Features: past values of this metric and others
                features = []
                
                # Add past values of this metric
                for j in range(lookback):
                    features.append(self.history[metric][i - j - 1])
                
                # Add values of other metrics at current time
                for other_metric in metrics:
                    if other_metric != metric and other_metric in self.history:
                        features.append(self.history[other_metric][i])
                
                # Add developmental phase
                if i < len(self.history['dmn_activation']):
                    features.append(self.history['dmn_activation'][i])
                
                if i < len(self.history['critical_period_state']):
                    features.append(self.history['critical_period_state'][i])
                
                X.append(features)
                y.append(self.history[metric][i])
            
            # Convert to numpy arrays
            X = np.array(X)
            y = np.array(y)
            
            # Train a RandomForest model
            model = RandomForestRegressor(n_estimators=50, random_state=42)
            model.fit(X, y)
            
            # Store model and feature structure
            self.prediction_models[metric] = model
            self.prediction_features[metric] = {
                'lookback': lookback,
                'metrics': metrics
            }
    
    def train_prediction_model(self, metric: str) -> None:
        """
        Train a prediction model for a specific metric.
        
        Parameters:
        -----------
        metric: str
            Metric to predict
        """
        if metric not in self.history or len(self.history[metric]) < 10:
            print(f"Not enough data to train model for {metric}")
            return
        
        # Create features (use past values as features)
        X = []
        y = []
        
        lookback = 5  # Use 5 past values as features
        
        for i in range(lookback, len(self.history[metric])):
            # Features: past values
            features = [self.history[metric][i - j - 1] for j in range(lookback)]
            
            # Add current phase
            phase_value = self.current_phase.value if hasattr(self, 'current_phase') else 0
            features.append(phase_value)
            
            # Add dmn_activation if available
            if 'dmn_activation' in self.history and i < len(self.history['dmn_activation']):
                features.append(self.history['dmn_activation'][i])
            
            # Add critical period state if available
            if 'critical_period_state' in self.history and i < len(self.history['critical_period_state']):
                features.append(self.history['critical_period_state'][i])
            
            X.append(features)
            y.append(self.history[metric][i])
        
        # Convert to numpy arrays
        X = np.array(X)
        y = np.array(y)
        
        # Train a RandomForest model
        model = RandomForestRegressor(n_estimators=50, random_state=42)
        model.fit(X, y)
        
        # Calculate training error
        y_pred = model.predict(X)
        mse = mean_squared_error(y, y_pred)
        print(f"Model for {metric} trained with MSE: {mse:.6f}")
        
        # Store model and feature structure
        self.prediction_models[metric] = model
        self.prediction_features[metric] = {
            'lookback': lookback,
            'phase_included': True,
            'dmn_included': 'dmn_activation' in self.history,
            'cp_included': 'critical_period_state' in self.history
        }
    
    def predict_future_trajectories(self, additional_steps: int = 100) -> Dict[str, List[float]]:
        """
        Predict future trajectories of key metrics.
        
        Parameters:
        -----------
        additional_steps: int
            Number of future steps to predict
        
        Returns:
        --------
        Dict[str, List[float]]: Dictionary of predicted values for each metric
        """
        # Clear previous predictions
        self.predicted_trajectories = {}
        
        # For each trained model, predict future values
        for metric, model in self.prediction_models.items():
            # Current history values
            history_values = self.history[metric].copy()
            
            # Feature details
            features = self.prediction_features[metric]
            lookback = features['lookback']
            
            # Predictions list
            predictions = []
            
            # Current state to predict from
            current_state = history_values[-lookback:]
            
            # Phase progression for future steps (simplified model)
            future_phases = []
            if hasattr(self, 'current_phase'):
                current_phase_value = self.current_phase.value
                for i in range(additional_steps):
                    # Simplified phase model: cycle through phases
                    phase = (current_phase_value + i // 20) % 5
                    future_phases.append(phase)
            
            # Make predictions step by step
            for i in range(additional_steps):
                # Construct feature vector
                X = []
                
                # Past values of this metric
                X.extend(current_state)
                
                # Add phase if included
                if features.get('phase_included', False) and future_phases:
                    X.append(future_phases[i])
                
                # Add DMN value if included
                if features.get('dmn_included', False):
                    # Simple model of future DMN
                    if 'dmn_activation' in self.history:
                        last_dmn = self.history['dmn_activation'][-1]
                        future_dmn = max(0, min(1, last_dmn + np.random.normal(0, 0.05)))
                        X.append(future_dmn)
                
                # Add critical period if included
                if features.get('cp_included', False):
                    # Simple decay model
                    if 'critical_period_state' in self.history:
                        last_cp = self.history['critical_period_state'][-1]
                        future_cp = last_cp * 0.995
                        X.append(future_cp)
                
                # Make prediction
                X_array = np.array([X])
                prediction = float(model.predict(X_array)[0])
                
                # Add to predictions
                predictions.append(prediction)
                
                # Update current state for next step
                current_state.append(prediction)
                current_state = current_state[1:]  # Remove oldest value
            
            # Store predictions
            self.predicted_trajectories[metric] = predictions
        
        return self.predicted_trajectories
    
    def analyze_results(self) -> Dict:
        """
        Analyze the results of the simulation.
        
        Returns:
        --------
        Dict: Analysis results
        """
        # Check if there's enough data
        if len(self.history['complexity']) < 10:
            return {"error": "Not enough data for analysis"}
        
        # Convert to numpy arrays for analysis
        complexity = np.array(self.history['complexity'])
        coherence = np.array(self.history['coherence']) if 'coherence' in self.history else None
        energy = np.array(self.history['energy']) if 'energy' in self.history else None
        dmn_values = np.array(self.history['dmn_activation']) if 'dmn_activation' in self.history else None
        
        # Find peak complexity
        peak_complexity = np.max(complexity)
        peak_timestep = np.argmax(complexity)
        final_complexity = complexity[-1]
        
        # Calculate retention ratio (final vs peak)
        retention_ratio = final_complexity / peak_complexity if peak_complexity > 0 else 0
        
        # Calculate complexity-energy relationship
        energy_efficiency = None
        if energy is not None and np.max(energy) > 0:
            # Ratio of complexity to energy at the end
            energy_efficiency = final_complexity / energy[-1]
        
        # Calculate stability (variation in last 10% of timesteps)
        stability = None
        if len(complexity) >= 10:
            last_10_percent = complexity[-int(len(complexity)*0.1):]
            stability = 1.0 - np.std(last_10_percent) / np.mean(last_10_percent) if np.mean(last_10_percent) > 0 else 0
        
        # Analyze DMN activation patterns
        dmn_analysis = {}
        if dmn_values is not None and len(dmn_values) > 0:
            avg_dmn = np.mean(dmn_values)
            dmn_variability = np.std(dmn_values)
            dmn_analysis = {
                'average': avg_dmn,
                'variability': dmn_variability
            }
        
        # Analyze pruning patterns
        pruning_analysis = {}
        if 'pruning_rate' in self.history and len(self.history['pruning_rate']) > 0:
            pruning_rates = np.array(self.history['pruning_rate'])
            avg_pruning = np.mean(pruning_rates)
            max_pruning = np.max(pruning_rates)
            pruning_analysis = {
                'average_rate': avg_pruning,
                'max_rate': max_pruning,
                'overpruning_detected': max_pruning > 0.3  # Threshold for overpruning
            }
        
        # Neurodevelopmental pattern matching
        pattern_match = self._match_to_pattern_library()
        
        # Analysis result dictionary
        return {
            'peak_complexity': peak_complexity,
            'peak_timestep': peak_timestep,
            'final_complexity': final_complexity,
            'retention_ratio': retention_ratio,
            'energy_efficiency': energy_efficiency,
            'stability': stability,
            'dmn_analysis': dmn_analysis,
            'pruning_analysis': pruning_analysis,
            'pattern_match': pattern_match,
            'developmental_anomalies': self._detect_developmental_anomalies()
        }
    
    def _match_to_pattern_library(self) -> Dict:
        """
        Match the simulation results to neurodevelopmental patterns.
        
        Returns:
        --------
        Dict: Pattern matching results
        """
        # Get analysis results
        analysis = self.analyze_results()
        
        # Calculate match scores for each pattern
        scores = {}
        
        for pattern, template in self.pattern_library.items():
            score = 0
            max_score = 0
            
            # Compare complexity profile
            complexity = np.array(self.history['complexity'])
            if len(complexity) > 10:
                # Analyze shape of complexity curve
                complexity_normalized = (complexity - np.min(complexity)) / (np.max(complexity) - np.min(complexity) + 1e-10)
                
                # Feature: Does it plateau early?
                early_plateau = False
                if len(complexity) > 20:
                    early_half = complexity_normalized[:len(complexity)//2]
                    late_half = complexity_normalized[len(complexity)//2:]
                    if np.mean(early_half) > 0.7 and np.std(late_half) < 0.1:
                        early_plateau = True
                
                # Feature: Is it declining after peak?
                declining = False
                peak_idx = np.argmax(complexity)
                if peak_idx < len(complexity) - 10 and complexity[-1] < 0.7 * complexity[peak_idx]:
                    declining = True
                
                # Feature: Is it volatile?
                volatile = np.std(complexity_normalized) > 0.25
                
                # Feature: Is it under-activated?
                under_activated = np.max(complexity) < 0.4
                
                # Match profile to template
                if template['complexity_profile'] == 'sigmoidal' and not early_plateau and not declining and not volatile:
                    score += 2
                elif template['complexity_profile'] == 'early_plateau' and early_plateau:
                    score += 2
                elif template['complexity_profile'] == 'volatile' and volatile:
                    score += 2
                elif template['complexity_profile'] == 'declining' and declining:
                    score += 2
                elif template['complexity_profile'] == 'under_activated' and under_activated:
                    score += 2
                
                max_score += 2
            
            # Compare coherence profile if available
            if 'coherence' in self.history and len(self.history['coherence']) > 10:
                coherence = np.array(self.history['coherence'])
                coherence_normalized = (coherence - np.min(coherence)) / (np.max(coherence) - np.min(coherence) + 1e-10)
                
                # Calculate trend (positive or negative slope)
                x = np.arange(len(coherence))
                slope = np.polyfit(x, coherence, 1)[0]
                
                # Match to template
                if template['coherence_profile'] == 'increasing' and slope > 0.001:
                    score += 1
                elif template['coherence_profile'] == 'low' and np.mean(coherence) < 0.5:
                    score += 1
                elif template['coherence_profile'] == 'volatile' and np.std(coherence) > 0.15:
                    score += 1
                elif template['coherence_profile'] == 'declining' and slope < -0.001:
                    score += 1
                elif template['coherence_profile'] == 'moderate':
                    score += 0.5  # Partial credit for moderate profile
                
                max_score += 1
            
            # Compare DMN profile if available
            if 'dmn_activation' in self.history and len(self.history['dmn_activation']) > 10:
                dmn = np.array(self.history['dmn_activation'])
                
                # Calculate average DMN activation
                avg_dmn = np.mean(dmn)
                dmn_variability = np.std(dmn)
                
                # Match to template
                if template['dmn_profile'] == 'increasing' and np.polyfit(np.arange(len(dmn)), dmn, 1)[0] > 0.001:
                    score += 1
                elif template['dmn_profile'] == 'reduced' and avg_dmn < 0.4:
                    score += 1
                elif template['dmn_profile'] == 'volatile' and dmn_variability > 0.15:
                    score += 1
                elif template['dmn_profile'] == 'excessive' and avg_dmn > 0.7:
                    score += 1
                
                max_score += 1
            
            # Compare pruning profile if available
            if 'pruning_rate' in self.history and len(self.history['pruning_rate']) > 5:
                pruning = np.array(self.history['pruning_rate'])
                
                max_pruning = np.max(pruning)
                avg_pruning = np.mean(pruning)
                
                # Determine profile
                if template['pruning_profile'] == 'bell' and 0.05 < max_pruning < 0.3:
                    score += 1
                elif template['pruning_profile'] == 'reduced' and max_pruning < 0.1:
                    score += 1
                elif template['pruning_profile'] == 'delayed' and np.argmax(pruning) > len(pruning) * 0.6:
                    score += 1
                elif template['pruning_profile'] == 'excessive' and max_pruning > 0.3:
                    score += 1
                elif template['pruning_profile'] == 'moderate' and 0.1 < max_pruning < 0.2:
                    score += 1
                
                max_score += 1
            
            # Compare metric values
            if 'retention_ratio' in analysis and template['metrics']['retention_ratio'] is not None:
                retention_difference = abs(analysis['retention_ratio'] - template['metrics']['retention_ratio'])
                score += 1.0 * max(0, 1 - 2 * retention_difference)
                max_score += 1
            
            if 'energy_efficiency' in analysis and analysis['energy_efficiency'] is not None and template['metrics']['energy_efficiency'] is not None:
                efficiency_difference = abs(analysis['energy_efficiency'] - template['metrics']['energy_efficiency'])
                score += 1.0 * max(0, 1 - 2 * efficiency_difference)
                max_score += 1
            
            if 'stability' in analysis and analysis['stability'] is not None and template['metrics']['stability'] is not None:
                stability_difference = abs(analysis['stability'] - template['metrics']['stability'])
                score += 1.0 * max(0, 1 - 2 * stability_difference)
                max_score += 1
            
            # Calculate final match percentage
            match_percentage = score / max_score if max_score > 0 else 0
            scores[pattern] = match_percentage
        
        # Find best match
        best_match = max(scores.items(), key=lambda x: x[1])
        
        # Check if there's a good enough match
        if best_match[1] > 0.6:
            matched_pattern = best_match[0]
            confidence = best_match[1]
        else:
            matched_pattern = NeurodevelopmentalPattern.UNCLASSIFIED
            confidence = 0.0
        
        # Return match results
        return {
            'pattern': matched_pattern.name,
            'confidence': confidence,
            'scores': {pattern.name: score for pattern, score in scores.items()}
        }
    
    def _detect_developmental_anomalies(self) -> Dict:
        """
        Detect potential developmental anomalies in the simulation.
        
        Returns:
        --------
        Dict: Detected anomalies with descriptions
        """
        anomalies = {}
        
        # Check for overpruning
        if 'pruning_rate' in self.history and len(self.history['pruning_rate']) > 0:
            pruning_rates = np.array(self.history['pruning_rate'])
            max_pruning = np.max(pruning_rates)
            
            if max_pruning > 0.3:
                anomalies['overpruning'] = {
                    'severity': (max_pruning - 0.3) / 0.2,  # Scale: 0-1 for severity
                    'description': 'Excessive pruning detected, which may result in loss of important connections'
                }
        
        # Check for coherence issues
        if 'coherence' in self.history and len(self.history['coherence']) > 10:
            coherence = np.array(self.history['coherence'])
            
            # Check for declining coherence
            x = np.arange(len(coherence))
            slope = np.polyfit(x, coherence, 1)[0]
            
            if slope < -0.001 and coherence[-1] < 0.4:
                anomalies['declining_coherence'] = {
                    'severity': min(1.0, abs(slope) * 1000),
                    'description': 'Decreasing field coherence, may indicate network fragmentation'
                }
        
        # Check for theta-gamma coupling issues
        if 'theta_gamma_coupling' in self.history and len(self.history['theta_gamma_coupling']) > 10:
            coupling = np.array(self.history['theta_gamma_coupling'])
            avg_coupling = np.mean(coupling)
            
            if avg_coupling < 0.3:
                anomalies['poor_oscillatory_coupling'] = {
                    'severity': 1.0 - (avg_coupling / 0.3),
                    'description': 'Weak theta-gamma coupling, may indicate memory encoding problems'
                }
        
        # Check for energy efficiency issues
        if 'complexity' in self.history and 'energy' in self.history and len(self.history['complexity']) > 10:
            complexity = np.array(self.history['complexity'])
            energy = np.array(self.history['energy'])
            
            # Calculate complexity-to-energy ratio
            if np.mean(energy) > 0:
                efficiency = complexity / energy
                final_efficiency = efficiency[-1]
                
                if final_efficiency < 0.5:
                    anomalies['poor_energy_efficiency'] = {
                        'severity': 1.0 - (final_efficiency / 0.5),
                        'description': 'Low complexity-to-energy ratio, may indicate inefficient resource utilization'
                    }
        
        # Check for critical period issues
        if 'critical_period_state' in self.history and len(self.history['critical_period_state']) > 10:
            cp_state = np.array(self.history['critical_period_state'])
            cp_closure_rate = (cp_state[0] - cp_state[-1]) / max(cp_state[0], 1e-10)
            
            if cp_closure_rate < 0.3 and self.timestep > 100:
                anomalies['prolonged_critical_period'] = {
                    'severity': 1.0 - (cp_closure_rate / 0.3),
                    'description': 'Critical period closing too slowly, may result in excessive plasticity'
                }
            elif cp_closure_rate > 0.8 and self.timestep < 50:
                anomalies['premature_critical_period_closure'] = {
                    'severity': (cp_closure_rate - 0.8) / 0.2,
                    'description': 'Critical period closing too quickly, may restrict learning potential'
                }
        
        return anomalies
    
    def visualize_field(self, include_predictions: bool = False) -> plt.Figure:
        """
        Visualize the current state of the intent field and agents.
        
        Parameters:
        -----------
        include_predictions: bool
            Whether to include prediction visualizations
        
        Returns:
        --------
        plt.Figure: Matplotlib figure object
        """
        # Create figure with multiple subplots
        if include_predictions and self.prediction_models:
            fig, axes = plt.subplots(2, 2, figsize=(14, 12))
        else:
            fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        
        # Flatten axes if needed
        if not isinstance(axes, np.ndarray):
            axes = np.array([axes])
        if axes.ndim == 1:
            axes = axes.reshape(1, -1)
        
        # Plot 1: Field visualization
        ax = axes[0, 0]
        
        # Create grid for field visualization
        x = np.linspace(0, self.dimensions[0], 100)
        y = np.linspace(0, self.dimensions[1], 100)
        X, Y = np.meshgrid(x, y)
        Z = np.zeros_like(X)
        
        # Calculate field value at each grid point
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                Z[i, j] = self.calculate_field_value(X[i, j], Y[i, j])
        
        # Plot contour
        contour = ax.contourf(X, Y, Z, 15, cmap='viridis', alpha=0.7)
        fig.colorbar(contour, ax=ax, label='Field Strength')
        
        # Plot agents
        agent_x = [agent['x'] for agent in self.agents]
        agent_y = [agent['y'] for agent in self.agents]
        agent_intent = [agent['intent'] for agent in self.agents]
        agent_info = [agent['information'] for agent in self.agents]
        agent_resonance = [agent['resonance_state'] for agent in self.agents]
        
        # Scale marker sizes based on information content
        marker_sizes = [30 + 70 * info for info in agent_info]
        
        # Color based on intent
        scatter = ax.scatter(
            agent_x, agent_y, 
            s=marker_sizes, 
            c=agent_intent, 
            cmap='coolwarm', 
            alpha=0.8,
            edgecolors='black',
            linewidths=0.5 + 1.5 * np.array(agent_resonance)  # Resonant agents have thicker edges
        )
        fig.colorbar(scatter, ax=ax, label='Agent Intent')
        
        # Plot connections if available
        if self.connections:
            for conn in self.connections[:100]:  # Limit to 100 connections for clarity
                idx1 = conn['source']
                idx2 = conn['target']
                
                if idx1 < len(self.agents) and idx2 < len(self.agents):
                    x1, y1 = self.agents[idx1]['x'], self.agents[idx1]['y']
                    x2, y2 = self.agents[idx2]['x'], self.agents[idx2]['y']
                    
                    # Adjust line width based on connection weight
                    line_width = 0.5 + 1.5 * conn['weight']
                    
                    # Narrative content gets different color
                    color = 'orange' if conn.get('narrative_content', False) else 'gray'
                    
                    ax.plot([x1, x2], [y1, y2], color=color, alpha=0.3, linewidth=line_width)
        
        ax.set_title(f'Intent Field - Phase: {self.current_phase.name}')
        ax.set_xlabel('X Position')
        ax.set_ylabel('Y Position')
        
        # Plot 2: Metrics history
        ax = axes[0, 1]
        
        timesteps = np.arange(len(self.history['complexity']))
        
        # Plot complexity
        ax.plot(timesteps, self.history['complexity'], 'b-', label='Complexity')
        
        # Plot coherence if available
        if 'coherence' in self.history:
            ax.plot(timesteps, self.history['coherence'], 'g-', label='Coherence')
        
        # Plot energy if available
        if 'energy' in self.history:
            ax.plot(timesteps, self.history['energy'], 'r-', label='Energy')
        
        # Annotate phases with vertical lines
        phase_changes = []
        current_phase = None
        
        for i, phase in enumerate(self.history.get('phase', [])):
            if phase != current_phase:
                current_phase = phase
                phase_changes.append(i)
        
        for t in phase_changes:
            if t < len(timesteps):
                ax.axvline(x=t, color='k', linestyle='--', alpha=0.5)
        
        ax.set_title('System Metrics Over Time')
        ax.set_xlabel('Timestep')
        ax.set_ylabel('Metric Value')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Plot 3: Oscillatory metrics
        ax = axes[1, 0]
        
        # Plot DMN activation
        if 'dmn_activation' in self.history:
            ax.plot(
                np.arange(len(self.history['dmn_activation'])), 
                self.history['dmn_activation'], 
                'g-', 
                label='DMN Activation'
            )
        
        # Plot theta-gamma coupling
        if 'theta_gamma_coupling' in self.history:
            ax.plot(
                np.arange(len(self.history['theta_gamma_coupling'])), 
                self.history['theta_gamma_coupling'], 
                'm-', 
                label='Theta-Gamma Coupling'
            )
        
        # Plot critical period state
        if 'critical_period_state' in self.history:
            ax.plot(
                np.arange(len(self.history['critical_period_state'])), 
                self.history['critical_period_state'], 
                'c-', 
                label='Critical Period'
            )
        
        ax.set_title('Neurobiological Metrics')
        ax.set_xlabel('Timestep')
        ax.set_ylabel('Value')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Plot 4: Predictions or Connection metrics
        ax = axes[1, 1]
        
        if include_predictions and self.prediction_models:
            # Plot history and predictions for complexity
            if 'complexity' in self.history and 'complexity' in self.predicted_trajectories:
                history = self.history['complexity']
                predictions = self.predicted_trajectories['complexity']
                
                # Plot history
                ax.plot(
                    np.arange(len(history)), 
                    history, 
                    'b-', 
                    label='Complexity History'
                )
                
                # Plot predictions
                ax.plot(
                    np.arange(len(history), len(history) + len(predictions)), 
                    predictions, 
                    'b--', 
                    label='Complexity Prediction'
                )
                
                # Confidence interval (simple model, could be improved)
                prediction_array = np.array(predictions)
                upper_bound = prediction_array * 1.2
                lower_bound = prediction_array * 0.8
                
                ax.fill_between(
                    np.arange(len(history), len(history) + len(predictions)),
                    lower_bound,
                    upper_bound,
                    color='b',
                    alpha=0.2
                )
            
            # Plot predictions for coherence if available
            if 'coherence' in self.history and 'coherence' in self.predicted_trajectories:
                history = self.history['coherence']
                predictions = self.predicted_trajectories['coherence']
                
                # Plot history
                ax.plot(
                    np.arange(len(history)), 
                    history, 
                    'g-', 
                    label='Coherence History'
                )
                
                # Plot predictions
                ax.plot(
                    np.arange(len(history), len(history) + len(predictions)), 
                    predictions, 
                    'g--', 
                    label='Coherence Prediction'
                )
            
            ax.set_title('Metric Predictions')
            ax.set_xlabel('Timestep')
            ax.set_ylabel('Value')
            ax.legend()
            ax.grid(True, alpha=0.3)
            
        else:
            # Plot connection metrics
            if self.connections:
                connection_ages = [conn.get('age', 0) for conn in self.connections]
                connection_weights = [conn['weight'] for conn in self.connections]
                
                ax.hist(connection_weights, bins=20, alpha=0.7, label='Connection Weights')
                
                if 'pruning_rate' in self.history:
                    ax2 = ax.twinx()
                    ax2.plot(
                        np.arange(len(self.history['pruning_rate'])), 
                        self.history['pruning_rate'], 
                        'r-', 
                        label='Pruning Rate'
                    )
                    ax2.set_ylabel('Pruning Rate', color='r')
                    ax2.tick_params(axis='y', colors='r')
                    
                    # Add legend for second y-axis
                    lines, labels = ax.get_legend_handles_labels()
                    lines2, labels2 = ax2.get_legend_handles_labels()
                    ax.legend(lines + lines2, labels + labels2, loc='upper right')
                else:
                    ax.legend()
            
            ax.set_title('Connection Metrics')
            ax.set_xlabel('Connection Weight' if self.connections else 'No Connections')
            ax.set_ylabel('Count')
            ax.grid(True, alpha=0.3)
        
        # Adjust layout
        plt.tight_layout()
        
        return fig
    
    def create_field_animation(self, steps: int = 100, interval: int = 50) -> None:
        """
        Create an animation of field evolution over time.
        
        Parameters:
        -----------
        steps: int
            Number of steps to animate
        interval: int
            Interval between frames in milliseconds
        """
        try:
            from matplotlib.animation import FuncAnimation
            
            # Create figure
            fig, ax = plt.subplots(figsize=(10, 8))
            
            # Initialize grid
            x = np.linspace(0, self.dimensions[0], 50)
            y = np.linspace(0, self.dimensions[1], 50)
            X, Y = np.meshgrid(x, y)
            Z = np.zeros_like(X)
            
            # Calculate initial field
            for i in range(X.shape[0]):
                for j in range(X.shape[1]):
                    Z[i, j] = self.calculate_field_value(X[i, j], Y[i, j])
            
            # Initial plot
            contour = ax.contourf(X, Y, Z, 15, cmap='viridis', alpha=0.7)
            
            # Initial agent scatter
            agent_x = [agent['x'] for agent in self.agents]
            agent_y = [agent['y'] for agent in self.agents]
            agent_intent = [agent['intent'] for agent in self.agents]
            agent_info = [agent['information'] for agent in self.agents]
            
            # Scale marker sizes based on information content
            marker_sizes = [30 + 70 * info for info in agent_info]
            
            scatter = ax.scatter(
                agent_x, agent_y, 
                s=marker_sizes, 
                c=agent_intent, 
                cmap='coolwarm', 
                alpha=0.8,
                edgecolors='black'
            )
            
            # Add colorbar
            fig.colorbar(contour, ax=ax, label='Field Strength')
            
            # Title
            title = ax.set_title(f'Intent Field - Timestep: 0')
            
            # Function to update animation
            def update(frame):
                # Run a simulation step
                self.run_single_step()
                
                # Update field values
                for i in range(X.shape[0]):
                    for j in range(X.shape[1]):
                        Z[i, j] = self.calculate_field_value(X[i, j], Y[i, j])
                
                # Clear previous plot
                ax.collections = []
                
                # Update contour
                contour = ax.contourf(X, Y, Z, 15, cmap='viridis', alpha=0.7)
                
                # Update agent positions and properties
                agent_x = [agent['x'] for agent in self.agents]
                agent_y = [agent['y'] for agent in self.agents]
                agent_intent = [agent['intent'] for agent in self.agents]
                agent_info = [agent['information'] for agent in self.agents]
                agent_resonance = [agent['resonance_state'] for agent in self.agents]
                
                # Scale marker sizes based on information content
                marker_sizes = [30 + 70 * info for info in agent_info]
                
                # Update scatter plot
                scatter = ax.scatter(
                    agent_x, agent_y, 
                    s=marker_sizes, 
                    c=agent_intent, 
                    cmap='coolwarm', 
                    alpha=0.8,
                    edgecolors='black',
                    linewidths=0.5 + 1.5 * np.array(agent_resonance)
                )
                
                # Plot connections
                if self.connections:
                    for conn in self.connections[:50]:  # Limit to 50 connections for performance
                        idx1 = conn['source']
                        idx2 = conn['target']
                        
                        if idx1 < len(self.agents) and idx2 < len(self.agents):
                            x1, y1 = self.agents[idx1]['x'], self.agents[idx1]['y']
                            x2, y2 = self.agents[idx2]['x'], self.agents[idx2]['y']
                            
                            line_width = 0.5 + 1.5 * conn['weight']
                            color = 'orange' if conn.get('narrative_content', False) else 'gray'
                            
                            ax.plot([x1, x2], [y1, y2], color=color, alpha=0.3, linewidth=line_width)
                
                # Update title
                title.set_text(f'Intent Field - Timestep: {frame+1}, Phase: {self.current_phase.name}')
                
                return scatter,
            
            # Create animation
            anim = FuncAnimation(fig, update, frames=steps, interval=interval, blit=False)
            
            return anim
            
        except ImportError:
            print("Animation requires matplotlib.animation module")
            return None
    
    def generate_neurodevelopmental_report(self) -> str:
        """
        Generate a comprehensive report on the neurodevelopmental mapping of the simulation.
        
        Returns:
        --------
        str: Markdown-formatted report
        """
        # Get analysis results
        analysis = self.analyze_results()
        
        # Format report as markdown
        report = "# IntentSim Neurodevelopmental Analysis Report\n\n"
        
        # Basic information
        report += "## Simulation Parameters\n\n"
        report += f"- Dimensions: {self.dimensions}\n"
        report += f"- Agent Count: {len(self.agents)}\n"
        report += f"- Intent Strength: {self.intent_strength}\n"
        report += f"- Entropy Factor: {self.entropy_factor}\n"
        report += f"- Critical Period Flexibility: {self.critical_period_flexibility}\n"
        report += f"- Theta Oscillation Strength: {self.theta_oscillation_strength}\n"
        report += f"- Gamma Oscillation Strength: {self.gamma_oscillation_strength}\n"
        report += f"- Overpruning Risk Factor: {self.overpruning_risk_factor}\n"
        report += f"- Narrative Salience Factor: {self.narrative_salience_factor}\n"
        report += f"- Simulation Length: {self.timestep} timesteps\n\n"
        
        # Developmental pattern
        report += "## Neurodevelopmental Pattern Analysis\n\n"
        
        if 'pattern_match' in analysis:
            pattern = analysis['pattern_match']
            report += f"### Identified Pattern: {pattern['pattern']}\n\n"
            report += f"**Match Confidence:** {pattern['confidence']:.2f}\n\n"
            
            report += "**Pattern Scores:**\n\n"
            for p_name, score in pattern['scores'].items():
                report += f"- {p_name}: {score:.2f}\n"
            report += "\n"
        
        # Complexity Analysis
        report += "## Complexity Analysis\n\n"
        
        peak_complexity = analysis.get('peak_complexity', 'Unknown')
        peak_timestep = analysis.get('peak_timestep', 'Unknown')
        final_complexity = analysis.get('final_complexity', 'Unknown')
        retention_ratio = analysis.get('retention_ratio', 'Unknown')
        
        report += f"- Peak Complexity: {peak_complexity:.4f}\n"
        report += f"- Peak Timestep: {peak_timestep}\n"
        report += f"- Final Complexity: {final_complexity:.4f}\n"
        report += f"- Retention Ratio: {retention_ratio:.4f}\n\n"
        
        report += "### Interpretation:\n\n"
        
        # Interpret retention ratio
        if isinstance(retention_ratio, (int, float)):
            if retention_ratio > 0.9:
                report += "- **High Retention:** The system maintained most of its peak complexity, suggesting minimal pruning or highly effective pruning that preserved important structures.\n"
            elif retention_ratio > 0.7:
                report += "- **Moderate Retention:** The system retained a significant portion of its peak complexity, suggesting healthy pruning that removed non-essential connections while preserving important ones.\n"
            elif retention_ratio > 0.5:
                report += "- **Low Retention:** The system lost a substantial amount of its peak complexity, which may indicate over-pruning or failure to consolidate important patterns.\n"
            else:
                report += "- **Very Low Retention:** The system lost most of its peak complexity, suggesting severe over-pruning or network degradation.\n"
        
        # Energy efficiency
        energy_efficiency = analysis.get('energy_efficiency', None)
        if energy_efficiency is not None:
            report += f"\n- Energy Efficiency: {energy_efficiency:.4f}\n"
            
            if energy_efficiency > 1.2:
                report += "- **High Efficiency:** The system achieves high complexity with relatively low energy expenditure.\n"
            elif energy_efficiency > 0.8:
                report += "- **Moderate Efficiency:** The system has a balanced complexity-to-energy ratio.\n"
            else:
                report += "- **Low Efficiency:** The system requires high energy to maintain even modest complexity.\n"
        
        # DMN Analysis
        if 'dmn_analysis' in analysis:
            dmn = analysis['dmn_analysis']
            report += "\n## Default Mode Network Analysis\n\n"
            report += f"- Average DMN Activation: {dmn.get('average', 'Unknown'):.4f}\n"
            report += f"- DMN Variability: {dmn.get('variability', 'Unknown'):.4f}\n\n"
            
            # Interpretation
            if 'average' in dmn:
                avg_dmn = dmn['average']
                if avg_dmn > 0.7:
                    report += "- **High DMN Activation:** The system showed strong internal processing and goal-maintenance, potentially at the expense of external responsiveness.\n"
                elif avg_dmn > 0.4:
                    report += "- **Moderate DMN Activation:** The system maintained a healthy balance between internal goals and external stimuli.\n"
                else:
                    report += "- **Low DMN Activation:** The system was highly responsive to external inputs but may have had weaker goal persistence.\n"
            
            if 'variability' in dmn:
                var_dmn = dmn['variability']
                if var_dmn > 0.2:
                    report += "- **High DMN Variability:** The system showed large fluctuations in internal processing, potentially indicating instability in goal maintenance.\n"
                elif var_dmn > 0.1:
                    report += "- **Moderate DMN Variability:** The system showed normal fluctuations in internal versus external focus.\n"
                else:
                    report += "- **Low DMN Variability:** The system maintained a very steady level of internal processing.\n"
        
        # Pruning Analysis
        if 'pruning_analysis' in analysis:
            pruning = analysis['pruning_analysis']
            report += "\n## Pruning Analysis\n\n"
            report += f"- Average Pruning Rate: {pruning.get('average_rate', 'Unknown'):.4f}\n"
            report += f"- Maximum Pruning Rate: {pruning.get('max_rate', 'Unknown'):.4f}\n"
            report += f"- Overpruning Detected: {pruning.get('overpruning_detected', 'Unknown')}\n\n"
            
            # Interpretation
            if 'max_rate' in pruning:
                max_rate = pruning['max_rate']
                if max_rate > 0.3:
                    report += "- **High Pruning Rate:** The system eliminated many connections rapidly, which may indicate aggressive refinement or potential overpruning.\n"
                elif max_rate > 0.1:
                    report += "- **Moderate Pruning Rate:** The system showed healthy selective elimination of connections.\n"
                else:
                    report += "- **Low Pruning Rate:** The system retained most connections, potentially preserving unnecessary ones.\n"
        
        # Developmental Anomalies
        if 'developmental_anomalies' in analysis and analysis['developmental_anomalies']:
            anomalies = analysis['developmental_anomalies']
            report += "\n## Detected Developmental Anomalies\n\n"
            
            for anomaly_name, details in anomalies.items():
                report += f"### {anomaly_name.replace('_', ' ').title()}\n\n"
                report += f"- Severity: {details.get('severity', 'Unknown'):.2f}\n"
                report += f"- Description: {details.get('description', 'No description')}\n\n"
            
            report += "\n### Clinical Relevance:\n\n"
            
            # Add clinical relevance if specific patterns are detected
            if 'overpruning' in anomalies:
                report += "- **Overpruning:** In neurodevelopment, excessive synaptic pruning has been associated with conditions like schizophrenia, where too many connections are eliminated during adolescence.\n"
            
            if 'poor_oscillatory_coupling' in anomalies:
                report += "- **Poor Oscillatory Coupling:** Weak theta-gamma coupling is observed in conditions with memory impairments like Alzheimer's disease and certain learning disabilities.\n"
            
            if 'declining_coherence' in anomalies:
                report += "- **Declining Coherence:** Progressive loss of network coherence can resemble neurodegenerative processes where brain regions become increasingly disconnected.\n"
            
            if 'prolonged_critical_period' in anomalies:
                report += "- **Prolonged Critical Period:** Extended developmental plasticity is associated with certain neurodevelopmental conditions where the brain remains in an immature state for longer than typical.\n"
        
        # Future Predictions
        if self.predicted_trajectories:
            report += "\n## Future Trajectory Predictions\n\n"
            
            for metric, values in self.predicted_trajectories.items():
                if values:
                    future_trend = values[-1] - values[0]
                    report += f"### {metric.title()}\n\n"
                    report += f"- Predicted Change: {'Increase' if future_trend > 0 else 'Decrease'} by {abs(future_trend):.4f}\n"
                    report += f"- Final Predicted Value: {values[-1]:.4f}\n\n"
            
            report += "\n### Prediction Confidence:\n\n"
            
            # Add confidence information based on model quality
            if hasattr(self, 'prediction_models') and 'complexity' in self.prediction_models:
                report += "- These predictions are based on patterns observed in the current simulation and may not account for external perturbations.\n"
                report += "- Short-term predictions are generally more accurate than long-term ones.\n"
        
        # Recommendations
        report += "\n## Recommendations\n\n"
        
        # Based on analysis results, provide recommendations
        if 'pattern_match' in analysis and 'pattern' in analysis['pattern_match']:
            pattern = analysis['pattern_match']['pattern']
            
            if pattern == 'TYPICAL':
                report += "- **Maintain Current Parameters:** The system shows healthy developmental patterns.\n"
            elif pattern == 'ASD_LIKE':
                report += "- **Adjust Pruning Settings:** Consider increasing pruning sensitivity to enhance network specialization.\n"
                report += "- **Modulate DMN Activation:** Strengthen DMN to improve goal-directed processing.\n"
            elif pattern == 'ADHD_LIKE':
                report += "- **Stabilize Oscillations:** Strengthen theta-gamma coupling to improve coherence.\n"
                report += "- **Reduce Entropy Factor:** Lower randomness to improve focus and stability.\n"
            elif pattern == 'SCHIZOPHRENIA_LIKE':
                report += "- **Reduce Pruning Intensity:** Lower the pruning thresholds to preserve more connections.\n"
                report += "- **Strengthen Field Coherence:** Increase intent strength to maintain network integration.\n"
            elif pattern == 'DEPRESSION_LIKE':
                report += "- **Increase Field Energy:** Boost intent strength to elevate overall activity.\n"
                report += "- **Adjust DMN Activation:** Reduce DMN baseline to decrease self-reference processing.\n"
        
        # If there are anomalies, add specific recommendations
        if 'developmental_anomalies' in analysis and analysis['developmental_anomalies']:
            anomalies = analysis['developmental_anomalies']
            
            if 'overpruning' in anomalies:
                report += "- **Reduce Pruning Threshold:** Lower the pruning threshold to preserve more connections.\n"
            
            if 'poor_oscillatory_coupling' in anomalies:
                report += "- **Strengthen Oscillations:** Increase theta and gamma oscillation strengths to improve coupling.\n"
            
            if 'declining_coherence' in anomalies:
                report += "- **Enhance Field Strength:** Increase intent strength to improve field coherence.\n"
            
            if 'poor_energy_efficiency' in anomalies:
                report += "- **Optimize Connection Structure:** Consider more targeted pruning to improve efficiency.\n"
        
        report += "\n---\n\n"
        report += f"Report generated by IntentSim Integrated Prediction Model v1.0\n"
        report += f"Timestamp: {self.timestep}\n"
        
        return report
    
    def save_model(self, filename: str) -> None:
        """
        Save the model state to a file.
        
        Parameters:
        -----------
        filename: str
            Filename to save the model state
        """
        # Create a dictionary with all model state
        state = {
            'dimensions': self.dimensions,
            'agent_count': self.agent_count,
            'intent_strength': self.intent_strength,
            'entropy_factor': self.entropy_factor,
            'information_density': self.information_density,
            'field_decay_rate': self.field_decay_rate,
            'field_propagation_speed': self.field_propagation_speed,
            'movement_speed': self.movement_speed,
            'resonance_threshold': self.resonance_threshold,
            'pruning_threshold': self.pruning_threshold,
            'theta_oscillation_strength': self.theta_oscillation_strength,
            'gamma_oscillation_strength': self.gamma_oscillation_strength,
            'critical_period_flexibility': self.critical_period_flexibility,
            'dmn_baseline_activation': self.dmn_baseline_activation,
            'overpruning_risk_factor': self.overpruning_risk_factor,
            'hcp_connectivity_factor': self.hcp_connectivity_factor,
            'narrative_salience_factor': self.narrative_salience_factor,
            'timestep': self.timestep,
            'current_phase': self.current_phase.value,
            'theta_phase': self.theta_phase,
            'gamma_phase': self.gamma_phase,
            'dmn_activation': self.dmn_activation,
            'critical_period_state': self.critical_period_state,
            'agents': self.agents,
            'connections': self.connections,
            'history': self.history
        }
        
        # Save to file
        with open(filename, 'w') as f:
            json.dump(state, f)
    
    def load_model(self, filename: str) -> None:
        """
        Load the model state from a file.
        
        Parameters:
        -----------
        filename: str
            Filename to load the model state from
        """
        # Load from file
        with open(filename, 'r') as f:
            state = json.load(f)
        
        # Set model parameters
        self.dimensions = state['dimensions']
        self.agent_count = state['agent_count']
        self.intent_strength = state['intent_strength']
        self.entropy_factor = state['entropy_factor']
        self.information_density = state['information_density']
        self.field_decay_rate = state['field_decay_rate']
        self.field_propagation_speed = state['field_propagation_speed']
        self.movement_speed = state['movement_speed']
        self.resonance_threshold = state['resonance_threshold']
        self.pruning_threshold = state['pruning_threshold']
        self.theta_oscillation_strength = state['theta_oscillation_strength']
        self.gamma_oscillation_strength = state['gamma_oscillation_strength']
        self.critical_period_flexibility = state['critical_period_flexibility']
        self.dmn_baseline_activation = state['dmn_baseline_activation']
        self.overpruning_risk_factor = state['overpruning_risk_factor']
        self.hcp_connectivity_factor = state['hcp_connectivity_factor']
        self.narrative_salience_factor = state['narrative_salience_factor']
        self.timestep = state['timestep']
        self.current_phase = DevelopmentalPhase(state['current_phase'])
        self.theta_phase = state['theta_phase']
        self.gamma_phase = state['gamma_phase']
        self.dmn_activation = state['dmn_activation']
        self.critical_period_state = state['critical_period_state']
        self.agents = state['agents']
        self.connections = state['connections']
        self.history = state['history']
        
        # Update spatial index
        self._update_spatial_index()
        
        # Train prediction models based on loaded history
        self.train_prediction_models()


# Usage example
if __name__ == "__main__":
    # Create a model
    model = IntentSimPredictor(
        dimensions=(100, 100),
        agent_count=150,
        intent_strength=0.1,
        entropy_factor=0.3,
        theta_oscillation_strength=0.5,
        gamma_oscillation_strength=0.7,
        critical_period_flexibility=1.0,
        overpruning_risk_factor=0.0
    )
    
    # Run a cascade experiment
    results = model.run_cascade(
        total_steps=600,
        bloom_timesteps=[100, 200, 300, 400, 500]
    )
    
    # Train prediction models
    model.train_prediction_model('complexity')
    
    # Generate predictions
    model.predict_future_trajectories(additional_steps=100)
    
    # Visualize the field with predictions
    fig = model.visualize_field(include_predictions=True)
    plt.show()
    
    # Generate a neurodevelopmental report
    report = model.generate_neurodevelopmental_report()
    print(report)
