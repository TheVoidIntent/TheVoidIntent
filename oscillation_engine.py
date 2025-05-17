"""
Oscillation Engine for IntentSim Integrated Prediction Model
===========================================================
Implements biologically-inspired neural oscillations including theta-gamma coupling
and Default Mode Network dynamics based on neuroscience principles.

Author: Marcelo Mezquia | IntentSim
Version: 1.0
"""

import numpy as np
from typing import Dict, List, Tuple, Optional, Union
from enum import Enum


class OscillationType(Enum):
    """Types of neural oscillations modeled in the system."""
    DELTA = 0   # 0.5-4 Hz, deep sleep, large amplitude
    THETA = 1   # 4-8 Hz, spatial navigation, memory
    ALPHA = 2   # 8-12 Hz, relaxation, inhibition
    BETA = 3    # 12-30 Hz, motor, active thinking
    GAMMA = 4   # 30-100 Hz, feature binding, attention
    CUSTOM = 5  # User-defined oscillation


class CouplingType(Enum):
    """Types of oscillatory coupling mechanisms."""
    PHASE_AMPLITUDE = 0  # Phase of slow oscillation modulates amplitude of fast oscillation
    PHASE_PHASE = 1      # Phase alignment between different oscillations
    AMPLITUDE_AMPLITUDE = 2  # Amplitude correlation between different oscillations
    NONE = 3             # No coupling


class OscillationEngine:
    """
    Implements biologically-inspired neural oscillations for the IntentSim model.
    Handles theta-gamma coupling, Default Mode Network activation,
    and other oscillatory dynamics based on neuroscience principles.
    """
    
    def __init__(self, 
                 theta_strength: float = 0.5,
                 gamma_strength: float = 0.7,
                 alpha_strength: float = 0.3,
                 coupling_strength: float = 0.8,
                 dmn_baseline: float = 0.3,
                 sample_rate: int = 100,
                 random_seed: Optional[int] = None):
        """
        Initialize the oscillation engine with parameters controlling different oscillations.
        
        Parameters:
        -----------
        theta_strength: float
            Strength of theta oscillations (4-8 Hz, memory encoding)
        gamma_strength: float
            Strength of gamma oscillations (30-100 Hz, local processing)
        alpha_strength: float
            Strength of alpha oscillations (8-12 Hz, inhibition)
        coupling_strength: float
            Strength of coupling between oscillations (e.g., theta-gamma)
        dmn_baseline: float
            Baseline activation of the Default Mode Network
        sample_rate: int
            Number of samples per second for oscillation calculation
        random_seed: Optional[int]
            Random seed for reproducibility
        """
        # Store parameters
        self.theta_strength = theta_strength
        self.gamma_strength = gamma_strength
        self.alpha_strength = alpha_strength
        self.coupling_strength = coupling_strength
        self.dmn_baseline = dmn_baseline
        self.sample_rate = sample_rate
        
        # Set random seed if provided
        if random_seed is not None:
            np.random.seed(random_seed)
        
        # Initialize oscillation state
        self.theta_phase = 0.0
        self.gamma_phase = 0.0
        self.alpha_phase = 0.0
        self.beta_phase = 0.0
        self.delta_phase = 0.0
        
        # Initialize DMN state
        self.dmn_activation = dmn_baseline
        
        # Initialize coupling parameters
        self.theta_gamma_coupling = coupling_strength
        self.alpha_gamma_coupling = 0.3  # Alpha inhibits gamma
        
        # Create frequency parameters (in Hz)
        self.frequencies = {
            OscillationType.DELTA: 2.0,    # 2 Hz (deep sleep)
            OscillationType.THETA: 6.0,    # 6 Hz (memory, navigation)
            OscillationType.ALPHA: 10.0,   # 10 Hz (relaxation, inhibition)
            OscillationType.BETA: 20.0,    # 20 Hz (motor, active thinking)
            OscillationType.GAMMA: 40.0    # 40 Hz (feature binding)
        }
        
        # Phase increments per step based on frequencies
        self.phase_increments = {
            osc_type: 2 * np.pi * freq / sample_rate 
            for osc_type, freq in self.frequencies.items()
        }
        
        # Oscillation strengths
        self.strengths = {
            OscillationType.DELTA: 0.2,
            OscillationType.THETA: theta_strength,
            OscillationType.ALPHA: alpha_strength,
            OscillationType.BETA: 0.4,
            OscillationType.GAMMA: gamma_strength
        }
        
        # Oscillation history for analysis
        self.history = {
            'theta_phase': [],
            'gamma_amplitude': [],
            'theta_gamma_coupling': [],
            'dmn_activation': []
        }
        
        # Create lookup tables for efficient sine calculations
        self._create_lookup_tables()
        
        # Initialize custom oscillations dictionary
        self.custom_oscillations = {}
    
    def _create_lookup_tables(self, resolution: int = 1000) -> None:
        """
        Create lookup tables for efficient sine calculations.
        
        Parameters:
        -----------
        resolution: int
            Number of points in the lookup table
        """
        self.sine_table = np.sin(np.linspace(0, 2*np.pi, resolution))
        self.cos_table = np.cos(np.linspace(0, 2*np.pi, resolution))
        self.table_resolution = resolution
    
    def _get_sine(self, phase: float) -> float:
        """
        Get sine value from lookup table for a given phase.
        
        Parameters:
        -----------
        phase: float
            Phase value (in radians)
        
        Returns:
        --------
        float: Sine of the phase
        """
        # Normalize phase to 0-2π range
        normalized_phase = phase % (2 * np.pi)
        
        # Convert to index
        index = int((normalized_phase / (2 * np.pi)) * self.table_resolution) % self.table_resolution
        
        # Return value from lookup table
        return self.sine_table[index]
    
    def _get_cosine(self, phase: float) -> float:
        """
        Get cosine value from lookup table for a given phase.
        
        Parameters:
        -----------
        phase: float
            Phase value (in radians)
        
        Returns:
        --------
        float: Cosine of the phase
        """
        # Normalize phase to 0-2π range
        normalized_phase = phase % (2 * np.pi)
        
        # Convert to index
        index = int((normalized_phase / (2 * np.pi)) * self.table_resolution) % self.table_resolution
        
        # Return value from lookup table
        return self.cos_table[index]
    
    def update(self) -> Dict[str, float]:
        """
        Update oscillation states for one time step.
        
        Returns:
        --------
        Dict[str, float]: Dictionary of current oscillation values
        """
        # Update phases
        self._update_phases()
        
        # Calculate oscillation values
        oscillation_values = self._calculate_oscillation_values()
        
        # Update DMN activation
        self._update_dmn_activation()
        
        # Calculate theta-gamma coupling
        theta_gamma_coupling = self._calculate_coupling(
            OscillationType.THETA, 
            OscillationType.GAMMA,
            CouplingType.PHASE_AMPLITUDE
        )
        
        # Store in history
        self.history['theta_phase'].append(self.theta_phase)
        self.history['gamma_amplitude'].append(oscillation_values['gamma'])
        self.history['theta_gamma_coupling'].append(theta_gamma_coupling)
        self.history['dmn_activation'].append(self.dmn_activation)
        
        # Return current state
        return {
            'theta': oscillation_values['theta'],
            'gamma': oscillation_values['gamma'],
            'alpha': oscillation_values['alpha'],
            'beta': oscillation_values['beta'],
            'delta': oscillation_values['delta'],
            'theta_gamma_coupling': theta_gamma_coupling,
            'dmn_activation': self.dmn_activation
        }
    
    def _update_phases(self) -> None:
        """Update all oscillation phases for one time step."""
        # Basic phase updates
        self.theta_phase = (self.theta_phase + self.phase_increments[OscillationType.THETA]) % (2 * np.pi)
        self.gamma_phase = (self.gamma_phase + self.phase_increments[OscillationType.GAMMA]) % (2 * np.pi)
        self.alpha_phase = (self.alpha_phase + self.phase_increments[OscillationType.ALPHA]) % (2 * np.pi)
        self.beta_phase = (self.beta_phase + self.phase_increments[OscillationType.BETA]) % (2 * np.pi)
        self.delta_phase = (self.delta_phase + self.phase_increments[OscillationType.DELTA]) % (2 * np.pi)
        
        # Apply theta-gamma coupling (gamma frequency increases near theta peaks)
        theta_modulation = 0.5 + 0.5 * self._get_sine(self.theta_phase)
        gamma_freq_modulation = 1.0 + self.theta_gamma_coupling * theta_modulation
        
        # Apply additional gamma phase increment based on coupling
        gamma_extra_increment = self.phase_increments[OscillationType.GAMMA] * (gamma_freq_modulation - 1.0)
        self.gamma_phase = (self.gamma_phase + gamma_extra_increment) % (2 * np.pi)
        
        # Update custom oscillation phases
        for name, osc in self.custom_oscillations.items():
            increment = 2 * np.pi * osc['frequency'] / self.sample_rate
            osc['phase'] = (osc['phase'] + increment) % (2 * np.pi)
    
    def _calculate_oscillation_values(self) -> Dict[str, float]:
        """
        Calculate oscillation values based on current phase and couplings.
        
        Returns:
        --------
        Dict[str, float]: Dictionary of oscillation values
        """
        # Basic oscillation values from sine lookup
        theta_value = self.strengths[OscillationType.THETA] * self._get_sine(self.theta_phase)
        alpha_value = self.strengths[OscillationType.ALPHA] * self._get_sine(self.alpha_phase)
        beta_value = self.strengths[OscillationType.BETA] * self._get_sine(self.beta_phase)
        delta_value = self.strengths[OscillationType.DELTA] * self._get_sine(self.delta_phase)
        
        # Apply theta-gamma coupling (gamma amplitude modulated by theta phase)
        theta_phase_factor = 0.5 + 0.5 * self._get_sine(self.theta_phase)
        gamma_base_amplitude = self.strengths[OscillationType.GAMMA]
        
        # Alpha inhibits gamma (anti-correlation)
        alpha_inhibition = 1.0 - self.alpha_gamma_coupling * (0.5 + 0.5 * self._get_sine(self.alpha_phase))
        
        # Calculate gamma with all modulations
        gamma_amplitude = (
            gamma_base_amplitude * 
            (1.0 + self.theta_gamma_coupling * theta_phase_factor) * 
            alpha_inhibition
        )
        
        gamma_value = gamma_amplitude * self._get_sine(self.gamma_phase)
        
        # Calculate values for custom oscillations
        custom_values = {}
        for name, osc in self.custom_oscillations.items():
            base_value = osc['strength'] * self._get_sine(osc['phase'])
            
            # Apply coupling if specified
            if osc.get('coupling_with') and osc.get('coupling_type'):
                target = osc['coupling_with']
                coupling_type = osc['coupling_type']
                coupling_strength = osc.get('coupling_strength', 0.5)
                
                if target == 'theta' and coupling_type == CouplingType.PHASE_AMPLITUDE:
                    # Amplitude modulated by theta phase
                    target_phase_factor = 0.5 + 0.5 * self._get_sine(self.theta_phase)
                    base_value *= (1.0 + coupling_strength * target_phase_factor)
            
            custom_values[name] = base_value
        
        # Combine all values
        values = {
            'theta': theta_value,
            'gamma': gamma_value,
            'alpha': alpha_value,
            'beta': beta_value,
            'delta': delta_value,
            **custom_values
        }
        
        return values
    
    def _update_dmn_activation(self) -> None:
        """
        Update Default Mode Network activation based on alpha and theta activity.
        DMN activation is positively correlated with alpha and anti-correlated with gamma.
        """
        # Calculate alpha contribution (positive)
        alpha_contrib = 0.6 * (0.5 + 0.5 * self._get_sine(self.alpha_phase)) * self.strengths[OscillationType.ALPHA]
        
        # Calculate gamma contribution (negative)
        gamma_amplitude = self.strengths[OscillationType.GAMMA] * (0.5 + 0.5 * self._get_sine(self.theta_phase))
        gamma_contrib = -0.3 * gamma_amplitude
        
        # Calculate delta contribution (positive during slow-wave sleep)
        delta_contrib = 0.2 * self.strengths[OscillationType.DELTA] * (0.5 + 0.5 * self._get_sine(self.delta_phase))
        
        # Combine contributions with baseline and apply small random fluctuation
        self.dmn_activation = self.dmn_baseline + alpha_contrib + gamma_contrib + delta_contrib
        
        # Add small noise
        self.dmn_activation += np.random.normal(0, 0.02)
        
        # Constrain to valid range
        self.dmn_activation = max(0.0, min(1.0, self.dmn_activation))
    
    def _calculate_coupling(self, 
                           oscillation1: OscillationType, 
                           oscillation2: OscillationType,
                           coupling_type: CouplingType) -> float:
        """
        Calculate coupling strength between two oscillations.
        
        Parameters:
        -----------
        oscillation1: OscillationType
            First oscillation
        oscillation2: OscillationType
            Second oscillation
        coupling_type: CouplingType
            Type of coupling to measure
        
        Returns:
        --------
        float: Coupling strength [0-1]
        """
        if coupling_type == CouplingType.PHASE_AMPLITUDE:
            # Phase-amplitude coupling (e.g., theta phase modulates gamma amplitude)
            if oscillation1 == OscillationType.THETA and oscillation2 == OscillationType.GAMMA:
                # Get theta phase
                theta_phase = self.theta_phase
                
                # Get gamma amplitude modulation by theta
                theta_mod = 0.5 + 0.5 * self._get_sine(theta_phase)
                
                # Actual coupling is scaled by coupling strength parameter
                return self.theta_gamma_coupling * theta_mod
        
        elif coupling_type == CouplingType.PHASE_PHASE:
            # Phase-phase coupling (phase synchronization)
            phase1 = self._get_oscillation_phase(oscillation1)
            phase2 = self._get_oscillation_phase(oscillation2)
            
            # Calculate phase synchronization index
            # Using phase locking value (PLV)
            phase_diff = phase1 - phase2
            sync = abs(np.exp(1j * phase_diff))
            
            return sync
        
        # Default: no coupling
        return 0.0
    
    def _get_oscillation_phase(self, oscillation: OscillationType) -> float:
        """
        Get the current phase of a specific oscillation.
        
        Parameters:
        -----------
        oscillation: OscillationType
            The oscillation to get the phase for
        
        Returns:
        --------
        float: Current phase in radians
        """
        if oscillation == OscillationType.THETA:
            return self.theta_phase
        elif oscillation == OscillationType.GAMMA:
            return self.gamma_phase
        elif oscillation == OscillationType.ALPHA:
            return self.alpha_phase
        elif oscillation == OscillationType.BETA:
            return self.beta_phase
        elif oscillation == OscillationType.DELTA:
            return self.delta_phase
        else:
            raise ValueError(f"Unknown oscillation type: {oscillation}")
    
    def add_custom_oscillation(self, 
                              name: str, 
                              frequency: float, 
                              strength: float = 0.5,
                              coupling_with: Optional[str] = None,
                              coupling_type: Optional[CouplingType] = None,
                              coupling_strength: float = 0.5) -> None:
        """
        Add a custom oscillation to the system.
        
        Parameters:
        -----------
        name: str
            Name of the custom oscillation
        frequency: float
            Frequency in Hz
        strength: float
            Oscillation strength
        coupling_with: Optional[str]
            Name of oscillation to couple with
        coupling_type: Optional[CouplingType]
            Type of coupling
        coupling_strength: float
            Strength of coupling
        """
        self.custom_oscillations[name] = {
            'frequency': frequency,
            'phase': 0.0,
            'strength': strength,
            'coupling_with': coupling_with,
            'coupling_type': coupling_type,
            'coupling_strength': coupling_strength
        }
    
    def set_oscillation_strength(self, oscillation: OscillationType, strength: float) -> None:
        """
        Set the strength of a specific oscillation.
        
        Parameters:
        -----------
        oscillation: OscillationType
            The oscillation to modify
        strength: float
            New strength value
        """
        self.strengths[oscillation] = strength
        
        # Update specific attributes for convenient access
        if oscillation == OscillationType.THETA:
            self.theta_strength = strength
        elif oscillation == OscillationType.GAMMA:
            self.gamma_strength = strength
        elif oscillation == OscillationType.ALPHA:
            self.alpha_strength = strength
    
    def set_coupling_strength(self, coupling_strength: float) -> None:
        """
        Set the strength of theta-gamma coupling.
        
        Parameters:
        -----------
        coupling_strength: float
            New coupling strength value
        """
        self.theta_gamma_coupling = coupling_strength
        self.coupling_strength = coupling_strength
    
    def set_dmn_baseline(self, dmn_baseline: float) -> None:
        """
        Set the baseline activation of the Default Mode Network.
        
        Parameters:
        -----------
        dmn_baseline: float
            New DMN baseline value
        """
        self.dmn_baseline = dmn_baseline
    
    def generate_oscillation_report(self) -> str:
        """
        Generate a report on oscillation characteristics and coupling patterns.
        
        Returns:
        --------
        str: Markdown-formatted oscillation report
        """
        report = "# Neural Oscillation Analysis Report\n\n"
        
        # Add oscillation parameters
        report += "## Oscillation Parameters\n\n"
        report += f"- Theta strength: {self.theta_strength:.2f}\n"
        report += f"- Gamma strength: {self.gamma_strength:.2f}\n"
        report += f"- Alpha strength: {self.alpha_strength:.2f}\n"
        report += f"- Theta-Gamma coupling: {self.theta_gamma_coupling:.2f}\n"
        report += f"- DMN baseline: {self.dmn_baseline:.2f}\n\n"
        
        # Add history analysis
        if len(self.history['theta_gamma_coupling']) > 10:
            report += "## Coupling Analysis\n\n"
            
            # Calculate average theta-gamma coupling
            avg_tg_coupling = np.mean(self.history['theta_gamma_coupling'])
            report += f"- Average Theta-Gamma Coupling: {avg_tg_coupling:.4f}\n"
            
            # Calculate DMN variability
            dmn_variability = np.std(self.history['dmn_activation'])
            report += f"- DMN Activation Variability: {dmn_variability:.4f}\n\n"
            
            # Add interpretation
            report += "### Interpretation\n\n"
            
            if avg_tg_coupling > 0.7:
                report += "- **Strong Theta-Gamma Coupling**: The system shows robust hierarchical organization of information processing, typical of effective memory encoding and cognitive integration.\n"
            elif avg_tg_coupling > 0.4:
                report += "- **Moderate Theta-Gamma Coupling**: The system shows normal hierarchical processing with room for both structured and exploratory dynamics.\n"
            else:
                report += "- **Weak Theta-Gamma Coupling**: The system may struggle with coordinating local and global processing, potentially reducing memory encoding efficiency.\n"
            
            if dmn_variability > 0.2:
                report += "- **High DMN Variability**: The system shows strong fluctuations between internally-focused and externally-focused states, which may indicate flexibility but potential instability.\n"
            elif dmn_variability > 0.1:
                report += "- **Moderate DMN Variability**: The system shows normal fluctuations between internal and external focus.\n"
            else:
                report += "- **Low DMN Variability**: The system maintains a very stable balance between internal and external processing, which may indicate either rigidity or strong goal maintenance.\n"
        
        return report
    
    def get_oscillation_history(self) -> Dict[str, List[float]]:
        """
        Get the history of oscillation values and couplings.
        
        Returns:
        --------
        Dict[str, List[float]]: Dictionary of oscillation histories
        """
        return self.history


# Usage example
if __name__ == "__main__":
    # Create an oscillation engine
    osc_engine = OscillationEngine(
        theta_strength=0.5,
        gamma_strength=0.7,
        alpha_strength=0.3,
        coupling_strength=0.8,
        dmn_baseline=0.3
    )
    
    # Add a custom oscillation (e.g., for emotion simulation)
    osc_engine.add_custom_oscillation(
        name="emotion",
        frequency=0.1,  # Very slow oscillation
        strength=0.6,
        coupling_with="theta",
        coupling_type=CouplingType.PHASE_AMPLITUDE,
        coupling_strength=0.4
    )
    
    # Run for several timesteps
    for _ in range(100):
        state = osc_engine.update()
    
    # Generate report
    report = osc_engine.generate_oscillation_report()
    print(report)
