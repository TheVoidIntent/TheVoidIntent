import numpy as np
import logging
from typing import Dict, List, Any, Optional, Union
import time
import re

class ReasoningFramework:
    """Base class for different reasoning approaches"""
    def __init__(self, name: str, config: Dict = None):
        self.name = name
        self.config = config or {}
        
    def apply(self, component: Dict) -> Dict:
        """Apply reasoning framework to a problem component"""
        raise NotImplementedError("Subclasses must implement apply method")


class DeductiveReasoning(ReasoningFramework):
    """Deductive reasoning framework (general to specific)"""
    def apply(self, component: Dict) -> Dict:
        """Apply deductive reasoning to problem component"""
        premises = component.get('premises', [])
        conclusion = component.get('conclusion', '')
        
        # Validate logical chain
        validity_score = self._validate_deductive_chain(premises, conclusion)
        
        return {
            'type': 'deductive',
            'premises': premises,
            'conclusion': conclusion,
            'validity_score': validity_score,
            'reasoning_path': self._construct_reasoning_path(premises, conclusion)
        }
    
    def _validate_deductive_chain(self, premises: List, conclusion: str) -> float:
        """Validate the logical chain from premises to conclusion"""
        # Simplified validity check
        if not premises or not conclusion:
            return 0.0
        
        # Check if conclusion follows from premises
        # This is a simplified heuristic - real implementation would be more sophisticated
        premise_keywords = set()
        for premise in premises:
            if isinstance(premise, str):
                premise_keywords.update(premise.lower().split())
        
        conclusion_keywords = set(conclusion.lower().split())
        overlap = premise_keywords.intersection(conclusion_keywords)
        
        return min(1.0, len(overlap) / max(1, len(conclusion_keywords)))
    
    def _construct_reasoning_path(self, premises: List, conclusion: str) -> List[str]:
        """Construct explicit reasoning path"""
        path = []
        for i, premise in enumerate(premises):
            path.append(f"P{i+1}: {premise}")
        path.append(f"Therefore: {conclusion}")
        return path


class InductiveReasoning(ReasoningFramework):
    """Inductive reasoning framework (specific to general)"""
    def apply(self, component: Dict) -> Dict:
        """Apply inductive reasoning to problem component"""
        observations = component.get('observations', [])
        pattern = component.get('pattern', '')
        
        # Analyze observations for pattern
        pattern_strength = self._analyze_pattern_strength(observations, pattern)
        
        return {
            'type': 'inductive',
            'observations': observations,
            'pattern': pattern,
            'pattern_strength': pattern_strength,
            'generalization': self._generate_generalization(observations, pattern)
        }
    
    def _analyze_pattern_strength(self, observations: List, pattern: str) -> float:
        """Analyze how well the pattern fits the observations"""
        if not observations or not pattern:
            return 0.0
        
        # Count observations that support the pattern
        supporting_count = 0
        for obs in observations:
            if isinstance(obs, str) and self._observation_supports_pattern(obs, pattern):
                supporting_count += 1
        
        return supporting_count / len(observations)
    
    def _observation_supports_pattern(self, observation: str, pattern: str) -> bool:
        """Check if observation supports the pattern"""
        # Simplified pattern matching
        pattern_keywords = pattern.lower().split()
        observation_keywords = observation.lower().split()
        
        # Check for keyword overlap
        overlap = sum(1 for keyword in pattern_keywords if keyword in observation_keywords)
        return overlap > len(pattern_keywords) * 0.5
    
    def _generate_generalization(self, observations: List, pattern: str) -> str:
        """Generate a generalization from observations and pattern"""
        if not observations:
            return "No generalization possible - insufficient observations"
        
        return f"Based on {len(observations)} observations, the pattern '{pattern}' appears to hold"


class CausalReasoning(ReasoningFramework):
    """Causal reasoning framework"""
    def apply(self, component: Dict) -> Dict:
        """Apply causal reasoning to problem component"""
        causes = component.get('causes', [])
        effects = component.get('effects', [])
        
        # Analyze causal relationships
        causal_strength = self._analyze_causal_strength(causes, effects)
        
        return {
            'type': 'causal',
            'causes': causes,
            'effects': effects,
            'causal_strength': causal_strength,
            'causal_chain': self._construct_causal_chain(causes, effects)
        }
    
    def _analyze_causal_strength(self, causes: List, effects: List) -> float:
        """Analyze strength of causal relationships"""
        if not causes or not effects:
            return 0.0
        
        # Simple heuristic: more causes and effects = stronger relationship
        return min(1.0, (len(causes) * len(effects)) / 10.0)
    
    def _construct_causal_chain(self, causes: List, effects: List) -> List[str]:
        """Construct causal chain representation"""
        chain = []
        for cause in causes:
            for effect in effects:
                chain.append(f"{cause} → {effect}")
        return chain


class ProbabilisticReasoning(ReasoningFramework):
    """Probabilistic reasoning framework"""
    def apply(self, component: Dict) -> Dict:
        """Apply probabilistic reasoning to problem component"""
        events = component.get('events', [])
        probabilities = component.get('probabilities', {})
        
        # Calculate combined probabilities
        combined_prob = self._calculate_combined_probability(events, probabilities)
        
        return {
            'type': 'probabilistic',
            'events': events,
            'individual_probabilities': probabilities,
            'combined_probability': combined_prob,
            'uncertainty_analysis': self._analyze_uncertainty(probabilities)
        }
    
    def _calculate_combined_probability(self, events: List, probabilities: Dict) -> float:
        """Calculate combined probability for events"""
        if not events or not probabilities:
            return 0.0
        
        # Simplified calculation - assumes independence
        combined = 1.0
        for event in events:
            prob = probabilities.get(event, 0.5)  # Default to 0.5 if unknown
            combined *= prob
        
        return combined
    
    def _analyze_uncertainty(self, probabilities: Dict) -> Dict:
        """Analyze uncertainty in probability estimates"""
        if not probabilities:
            return {'uncertainty_level': 'high', 'confidence': 0.0}
        
        values = list(probabilities.values())
        mean_prob = np.mean(values)
        variance = np.var(values)
        
        return {
            'uncertainty_level': 'low' if variance < 0.1 else 'medium' if variance < 0.25 else 'high',
            'confidence': 1.0 - variance,
            'mean_probability': mean_prob
        }


class StepByStepAnalyzer:
    """Breaks down problems into manageable components"""
    def __init__(self):
        self.decomposition_strategies = {
            'logical': self._logical_decomposition,
            'procedural': self._procedural_decomposition,
            'hierarchical': self._hierarchical_decomposition,
            'temporal': self._temporal_decomposition
        }
        
    def decompose(self, problem: Union[str, Dict]) -> List[Dict]:
        """Break down problem into components"""
        # Determine problem type
        problem_type = self._determine_problem_type(problem)
        
        # Select decomposition strategy
        strategy = self.decomposition_strategies.get(problem_type, self._logical_decomposition)
        
        # Decompose problem
        components = strategy(problem)
        
        # Add metadata to components
        for i, component in enumerate(components):
            component['component_id'] = i + 1
            component['parent_problem'] = str(problem)[:100] + '...' if len(str(problem)) > 100 else str(problem)
        
        return components
    
    def _determine_problem_type(self, problem: Union[str, Dict]) -> str:
        """Determine the type of problem for appropriate decomposition"""
        if isinstance(problem, dict):
            return problem.get('type', 'logical')
        
        # Analyze problem string for type indicators
        problem_str = str(problem).lower()
        
        if any(word in problem_str for word in ['steps', 'process', 'procedure', 'how to']):
            return 'procedural'
        elif any(word in problem_str for word in ['before', 'after', 'then', 'sequence', 'order']):
            return 'temporal'
        elif any(word in problem_str for word in ['level', 'category', 'type', 'class']):
            return 'hierarchical'
        else:
            return 'logical'
    
    def _logical_decomposition(self, problem: Union[str, Dict]) -> List[Dict]:
        """Decompose problem using logical structure"""
        if isinstance(problem, dict):
            problem_statement = problem.get('statement', problem.get('description', ''))
        else:
            problem_statement = str(problem)
        
        # Split into logical components based on conjunctions and sentence structure
        components = []
        sentences = re.split(r'[.!?]\s*', problem_statement)
        
        for sentence in sentences:
            if sentence.strip():
                # Further split by logical connectors
                sub_components = re.split(r'\b(and|or|but|if|then|because|since|therefore)\b', sentence)
                
                for i, sub in enumerate(sub_components):
                    if sub.strip() and sub not in ['and', 'or', 'but', 'if', 'then', 'because', 'since', 'therefore']:
                        components.append({
                            'type': 'logical',
                            'content': sub.strip(),
                            'context': sentence,
                            'decomposition_method': 'logical_split'
                        })
        
        return components or [{'type': 'logical', 'content': problem_statement, 'decomposition_method': 'no_split'}]
    
    def _procedural_decomposition(self, problem: Union[str, Dict]) -> List[Dict]:
        """Decompose problem into procedural steps"""
        if isinstance(problem, dict):
            problem_statement = problem.get('statement', problem.get('description', ''))
        else:
            problem_statement = str(problem)
        
        # Look for step indicators
        step_patterns = [
            r'step\s+\d+[:.]\s*([^.!?]+)',
            r'\d+\.\s*([^.!?]+)',
            r'first[,:\s]+([^.!?]+)',
            r'then[,:\s]+([^.!?]+)',
            r'next[,:\s]+([^.!?]+)',
            r'finally[,:\s]+([^.!?]+)'
        ]
        
        components = []
        step_number = 1
        
        for pattern in step_patterns:
            matches = re.findall(pattern, problem_statement, re.IGNORECASE)
            for match in matches:
                components.append({
                    'type': 'procedural',
                    'step_number': step_number,
                    'content': match.strip(),
                    'decomposition_method': 'procedural_pattern'
                })
                step_number += 1
        
        # If no explicit steps found, infer steps from problem structure
        if not components:
            sentences = problem_statement.split('.')
            for i, sentence in enumerate(sentences):
                if sentence.strip():
                    components.append({
                        'type': 'procedural',
                        'step_number': i + 1,
                        'content': sentence.strip(),
                        'decomposition_method': 'inferred_steps'
                    })
        
        return components
    
    def _hierarchical_decomposition(self, problem: Union[str, Dict]) -> List[Dict]:
        """Decompose problem into hierarchical levels"""
        if isinstance(problem, dict):
            problem_statement = problem.get('statement', problem.get('description', ''))
        else:
            problem_statement = str(problem)
        
        components = []
        
        # Look for hierarchical indicators
        hierarchy_patterns = [
            (r'main\s+([^.!?]+)', 1),
            (r'primary\s+([^.!?]+)', 1),
            (r'secondary\s+([^.!?]+)', 2),
            (r'sub[-\s]?([^.!?]+)', 2),
            (r'detail[s]?\s*[:-]?\s*([^.!?]+)', 3)
        ]
        
        for pattern, level in hierarchy_patterns:
            matches = re.findall(pattern, problem_statement, re.IGNORECASE)
            for match in matches:
                components.append({
                    'type': 'hierarchical',
                    'level': level,
                    'content': match.strip(),
                    'decomposition_method': 'hierarchical_pattern'
                })
        
        # If no explicit hierarchy found, create basic hierarchy
        if not components:
            # Main component
            components.append({
                'type': 'hierarchical',
                'level': 1,
                'content': problem_statement[:100] + '...' if len(problem_statement) > 100 else problem_statement,
                'decomposition_method': 'basic_hierarchy'
            })
            
            # Sub-components from sentences
            sentences = problem_statement.split('.')
            for sentence in sentences[1:]:
                if sentence.strip():
                    components.append({
                        'type': 'hierarchical',
                        'level': 2,
                        'content': sentence.strip(),
                        'decomposition_method': 'basic_hierarchy'
                    })
        
        return components
    
    def _temporal_decomposition(self, problem: Union[str, Dict]) -> List[Dict]:
        """Decompose problem into temporal sequence"""
        if isinstance(problem, dict):
            problem_statement = problem.get('statement', problem.get('description', ''))
        else:
            problem_statement = str(problem)
        
        components = []
        
        # Look for temporal indicators
        temporal_patterns = [
            (r'before\s+([^.!?]+)', 'before'),
            (r'first[,:\s]+([^.!?]+)', 'first'),
            (r'then[,:\s]+([^.!?]+)', 'middle'),
            (r'next[,:\s]+([^.!?]+)', 'middle'),
            (r'after\s+([^.!?]+)', 'after'),
            (r'finally[,:\s]+([^.!?]+)', 'last'),
            (r'eventually[,:\s]+([^.!?]+)', 'last')
        ]
        
        temporal_order = {'before': 1, 'first': 2, 'middle': 3, 'after': 4, 'last': 5}
        
        for pattern, time_marker in temporal_patterns:
            matches = re.findall(pattern, problem_statement, re.IGNORECASE)
            for match in matches:
                components.append({
                    'type': 'temporal',
                    'time_marker': time_marker,
                    'order': temporal_order[time_marker],
                    'content': match.strip(),
                    'decomposition_method': 'temporal_pattern'
                })
        
        # Sort by temporal order
        components.sort(key=lambda x: x['order'])
        
        # If no temporal indicators found, create basic sequence
        if not components:
            sentences = problem_statement.split('.')
            for i, sentence in enumerate(sentences):
                if sentence.strip():
                    components.append({
                        'type': 'temporal',
                        'time_marker': 'sequence',
                        'order': i + 1,
                        'content': sentence.strip(),
                        'decomposition_method': 'sequential_order'
                    })
        
        return components


class SolutionGenerator:
    """Synthesizes component solutions into final solution"""
    def __init__(self):
        self.integration_strategies = {
            'logical': self._integrate_logical,
            'procedural': self._integrate_procedural,
            'hierarchical': self._integrate_hierarchical,
            'temporal': self._integrate_temporal,
            'causal': self._integrate_causal,
            'probabilistic': self._integrate_probabilistic
        }
        
    def integrate(self, component_solutions: List[Dict], problem: Union[str, Dict]) -> Dict:
        """Synthesize component solutions into final solution"""
        # Determine integration strategy based on solution types
        solution_types = [sol.get('type', 'logical') for sol in component_solutions]
        primary_type = max(set(solution_types), key=solution_types.count)
        
        # Apply appropriate integration strategy
        integrator = self.integration_strategies.get(primary_type, self._integrate_logical)
        final_solution = integrator(component_solutions)
        
        # Add metadata
        final_solution.update({
            'problem': str(problem)[:200],
            'component_count': len(component_solutions),
            'primary_solution_type': primary_type,
            'integration_method': primary_type + '_integration',
            'confidence_score': self._calculate_solution_confidence(component_solutions)
        })
        
        return final_solution
    
    def _integrate_logical(self, component_solutions: List[Dict]) -> Dict:
        """Integrate logical reasoning solutions"""
        integrated_solution = {
            'type': 'logical',
            'reasoning_chain': [],
            'conclusion': '',
            'premises': []
        }
        
        # Collect all premises and reasoning paths
        for solution in component_solutions:
            if solution.get('type') == 'deductive':
                integrated_solution['premises'].extend(solution.get('premises', []))
                integrated_solution['reasoning_chain'].extend(solution.get('reasoning_path', []))
                if solution.get('conclusion'):
                    integrated_solution['conclusion'] = solution['conclusion']
        
        # Remove duplicates while preserving order
        integrated_solution['premises'] = list(dict.fromkeys(integrated_solution['premises']))
        integrated_solution['reasoning_chain'] = list(dict.fromkeys(integrated_solution['reasoning_chain']))
        
        return integrated_solution
    
    def _integrate_procedural(self, component_solutions: List[Dict]) -> Dict:
        """Integrate procedural solutions"""
        integrated_solution = {
            'type': 'procedural',
            'steps': [],
            'procedure': '',
            'prerequisites': []
        }
        
        # Sort component solutions by step number
        procedural_solutions = [sol for sol in component_solutions if sol.get('type') == 'procedural']
        procedural_solutions.sort(key=lambda x: x.get('step_number', 0))
        
        # Build integrated procedure
        for i, solution in enumerate(procedural_solutions):
            step = {
                'step_number': i + 1,
                'description': solution.get('content', ''),
                'component_id': solution.get('component_id')
            }
            integrated_solution['steps'].append(step)
        
        # Create textual procedure description
        procedure_text = "\n".join([f"Step {step['step_number']}: {step['description']}" 
                                   for step in integrated_solution['steps']])
        integrated_solution['procedure'] = procedure_text
        
        return integrated_solution
    
    def _integrate_hierarchical(self, component_solutions: List[Dict]) -> Dict:
        """Integrate hierarchical solutions"""
        integrated_solution = {
            'type': 'hierarchical',
            'structure': {},
            'levels': [],
            'hierarchy': ''
        }
        
        # Group solutions by level
        level_groups = {}
        for solution in component_solutions:
            if solution.get('type') == 'hierarchical':
                level = solution.get('level', 1)
                if level not in level_groups:
                    level_groups[level] = []
                level_groups[level].append(solution.get('content', ''))
        
        # Build hierarchical structure
        for level in sorted(level_groups.keys()):
            level_content = level_groups[level]
            integrated_solution['structure'][level] = level_content
            integrated_solution['levels'].append({
                'level': level,
                'items': level_content,
                'count': len(level_content)
            })
        
        # Create textual hierarchy representation
        hierarchy_lines = []
        for level in sorted(level_groups.keys()):
            indent = "  " * (level - 1)
            for item in level_groups[level]:
                hierarchy_lines.append(f"{indent}- {item}")
        
        integrated_solution['hierarchy'] = "\n".join(hierarchy_lines)
        
        return integrated_solution
    
    def _integrate_temporal(self, component_solutions: List[Dict]) -> Dict:
        """Integrate temporal sequence solutions"""
        integrated_solution = {
            'type': 'temporal',
            'timeline': [],
            'sequence': '',
            'duration_estimate': None
        }
        
        # Sort solutions by temporal order
        temporal_solutions = [sol for sol in component_solutions if sol.get('type') == 'temporal']
        temporal_solutions.sort(key=lambda x: x.get('order', 0))
        
        # Build temporal sequence
        for solution in temporal_solutions:
            timeline_entry = {
                'order': solution.get('order'),
                'time_marker': solution.get('time_marker'),
                'event': solution.get('content', ''),
                'component_id': solution.get('component_id')
            }
            integrated_solution['timeline'].append(timeline_entry)
        
        # Create textual sequence description
        sequence_text = "\n".join([f"{entry['time_marker'].capitalize()}: {entry['event']}" 
                                  for entry in integrated_solution['timeline']])
        integrated_solution['sequence'] = sequence_text
        
        return integrated_solution
    
    def _integrate_causal(self, component_solutions: List[Dict]) -> Dict:
        """Integrate causal reasoning solutions"""
        integrated_solution = {
            'type': 'causal',
            'causal_network': {},
            'chains': [],
            'root_causes': [],
            'final_effects': []
        }
        
        # Collect all causal relationships
        all_causes = []
        all_effects = []
        all_chains = []
        
        for solution in component_solutions:
            if solution.get('type') == 'causal':
                all_causes.extend(solution.get('causes', []))
                all_effects.extend(solution.get('effects', []))
                all_chains.extend(solution.get('causal_chain', []))
        
        # Build causal network
        for chain in all_chains:
            parts = chain.split(' → ')
            if len(parts) == 2:
                cause, effect = parts
                if cause not in integrated_solution['causal_network']:
                    integrated_solution['causal_network'][cause] = []
                integrated_solution['causal_network'][cause].append(effect)
        
        # Identify root causes (causes that are not effects of others)
        all_effects_set = set(all_effects)
        for cause in all_causes:
            if cause not in all_effects_set:
                integrated_solution['root_causes'].append(cause)
        
        # Identify final effects (effects that don't cause other things)
        all_causes_set = set(all_causes)
        for effect in all_effects:
            if effect not in all_causes_set:
                integrated_solution['final_effects'].append(effect)
        
        integrated_solution['chains'] = all_chains
        
        return integrated_solution
    
    def _integrate_probabilistic(self, component_solutions: List[Dict]) -> Dict:
        """Integrate probabilistic reasoning solutions"""
        integrated_solution = {
            'type': 'probabilistic',
            'events': [],
            'probabilities': {},
            'combined_probability': 0.0,
            'uncertainty_analysis': {}
        }
        
        # Collect all events and probabilities
        for solution in component_solutions:
            if solution.get('type') == 'probabilistic':
                integrated_solution['events'].extend(solution.get('events', []))
                integrated_solution['probabilities'].update(solution.get('individual_probabilities', {}))
        
        # Remove duplicate events
        integrated_solution['events'] = list(set(integrated_solution['events']))
        
        # Calculate combined probability (assuming independence for simplicity)
        if integrated_solution['probabilities']:
            combined = 1.0
            for event in integrated_solution['events']:
                prob = integrated_solution['probabilities'].get(event, 0.5)
                combined *= prob
            integrated_solution['combined_probability'] = combined
        
        # Aggregate uncertainty analysis
        all_uncertainties = []
        for solution in component_solutions:
            if solution.get('type') == 'probabilistic' and 'uncertainty_analysis' in solution:
                all_uncertainties.append(solution['uncertainty_analysis'])
        
        if all_uncertainties:
            # Average the uncertainty metrics
            integrated_solution['uncertainty_analysis'] = {
                'uncertainty_level': max([ua.get('uncertainty_level', 'medium') for ua in all_uncertainties]),
                'confidence': np.mean([ua.get('confidence', 0.5) for ua in all_uncertainties]),
                'mean_probability': np.mean([ua.get('mean_probability', 0.5) for ua in all_uncertainties])
            }
        
        return integrated_solution
    
    def _calculate_solution_confidence(self, component_solutions: List[Dict]) -> float:
        """Calculate overall confidence score for the solution"""
        if not component_solutions:
            return 0.0
        
        # Extract confidence scores from components
        confidence_scores = []
        for solution in component_solutions:
            if 'validity_score' in solution:
                confidence_scores.append(solution['validity_score'])
            elif 'pattern_strength' in solution:
                confidence_scores.append(solution['pattern_strength'])
            elif 'causal_strength' in solution:
                confidence_scores.append(solution['causal_strength'])
            elif 'combined_probability' in solution:
                confidence_scores.append(solution['combined_probability'])
            else:
                confidence_scores.append(0.5)  # Default confidence
        
        # Calculate weighted average with higher weight for more confident components
        if confidence_scores:
            return np.mean(confidence_scores)
        else:
            return 0.5


class AnalyticalProcessor:
    """
    Handles analytical tasks, problem-solving, and structured reasoning
    """
    def __init__(self, reasoning_config=None):
        self.reasoning_config = reasoning_config or {
            'default_framework': 'deductive',
            'confidence_threshold': 0.7,
            'max_components': 20
        }
        
        self.reasoning_frameworks = self._initialize_reasoning_frameworks()
        self.step_by_step_analyzer = StepByStepAnalyzer()
        self.solution_generator = SolutionGenerator()
        
        # Set up logging
        self.logger = logging.getLogger(f"{__name__}.AnalyticalProcessor")
        
    def _initialize_reasoning_frameworks(self) -> Dict:
        """Initialize different reasoning frameworks"""
        frameworks = {
            'deductive': DeductiveReasoning('deductive', self.reasoning_config),
            'inductive': InductiveReasoning('inductive', self.reasoning_config),
            'causal': CausalReasoning('causal', self.reasoning_config),
            'probabilistic': ProbabilisticReasoning('probabilistic', self.reasoning_config)
        }
        
        return frameworks
        
    def solve_analytical_problem(self, problem: Union[str, Dict]) -> Dict:
        """Process an analytical or reasoning-based problem"""
        self.logger.info(f"Processing analytical problem: {str(problem)[:100]}")
        
        start_time = time.time()
        
        # Identify appropriate reasoning framework
        framework = self._select_reasoning_framework(problem)
        
        # Break down problem into components
        components = self.step_by_step_analyzer.decompose(problem)
        
        self.logger.info(f"Problem decomposed into {len(components)} components")
        
        # Apply reasoning to each component
        component_solutions = []
        for component in components:
            solution = framework.apply(component)
            component_solutions.append(solution)
        
        # Synthesize component solutions
        final_solution = self.solution_generator.integrate(component_solutions, problem)
        
        # Add metadata
        final_solution.update({
            'processing_time': time.time() - start_time,
            'framework_used': framework.name,
            'analysis_depth': len(components),
            'processor_type': 'analytical'
        })
        
        self.logger.info(f"Problem solved using {framework.name} framework in {final_solution['processing_time']:.2f}s")
        
        return final_solution
    
    def _select_reasoning_framework(self, problem: Union[str, Dict]) -> ReasoningFramework:
        """Select the most appropriate reasoning framework for the problem"""
        if isinstance(problem, dict):
            # If problem specifies framework preference
            if 'preferred_framework' in problem:
                framework_name = problem['preferred_framework']
                if framework_name in self.reasoning_frameworks:
                    return self.reasoning_frameworks[framework_name]
            
            # Analyze problem content
            problem_text = problem.get('statement', problem.get('description', ''))
        else:
            problem_text = str(problem)
        
        # Analyze problem text for indicators
        text_lower = problem_text.lower()
        
        # Deductive reasoning indicators
        if any(word in text_lower for word in ['prove', 'given that', 'if...then', 'must be', 'necessarily']):
            return self.reasoning_frameworks['deductive']
        
        # Inductive reasoning indicators
        elif any(word in text_lower for word in ['pattern', 'trend', 'likely', 'probably', 'typically']):
            return self.reasoning_frameworks['inductive']
        
        # Causal reasoning indicators
        elif any(word in text_lower for word in ['because', 'caused by', 'leads to', 'results in', 'due to']):
            return self.reasoning_frameworks['causal']
        
        # Probabilistic reasoning indicators
        elif any(word in text_lower for word in ['probability', 'chance', 'risk', 'odds', 'likely']):
            return self.reasoning_frameworks['probabilistic']
        
        # Default to configuration setting
        default_framework_name = self.reasoning_config.get('default_framework', 'deductive')
        return self.reasoning_frameworks.get(default_framework_name, self.reasoning_frameworks['deductive'])
    
    def get_reasoning_summary(self) -> Dict:
        """Get a summary of available reasoning frameworks"""
        summary = {
            'available_frameworks': list(self.reasoning_frameworks.keys()),
            'default_framework': self.reasoning_config.get('default_framework', 'deductive'),
            'confidence_threshold': self.reasoning_config.get('confidence_threshold', 0.7),
            'framework_details': {}
        }
        
        for name, framework in self.reasoning_frameworks.items():
            summary['framework_details'][name] = {
                'name': framework.name,
                'type': type(framework).__name__,
                'config': framework.config
            }
        
        return summary
    
    def update_framework_config(self, framework_name: str, updates: Dict):
        """Update configuration for a specific reasoning framework"""
        if framework_name in self.reasoning_frameworks:
            framework = self.reasoning_frameworks[framework_name]
            framework.config.update(updates)
            self.logger.info(f"Updated configuration for framework: {framework_name}")
        else:
            self.logger.warning(f"Framework not found: {framework_name}")
