import pygame
import random
import math
import json
import os
import time

# --- Configuration ---
WIDTH, HEIGHT = 800, 600
DEPTH = 100  # For 3D simulations
AGENT_COUNT = 200
INTENT_FIELD_RESOLUTION = 20  # Lower = faster, but coarser
CLUSTER_THRESHOLD = 20
MAX_PARTICLES = 500
DATA_DIR = "sim_data"
LOG_INTERVAL = 10  # Log data every X timesteps (increased frequency)
VISUALIZE = True  # Enable/disable Pygame visualization

# --- Helper Functions ---
def random_vector(magnitude):
    angle = random.uniform(0, 2 * math.pi)
    return math.cos(angle) * magnitude, math.sin(angle) * magnitude

def create_grid(width, height, initial_value=0.0):
    return [[initial_value for _ in range(width)] for _ in range(height)]

def create_3d_grid(width, height, depth, initial_value=0.0):
    return [[[initial_value for _ in range(width)] for _ in range(height)] for _ in range(depth)]

# --- Intent Field Class ---
class IntentField:
    def __init__(self, field_type, intensity=1.0, decay_rate=0.01, position=None, dimensions=(100, 100, 100)):
        self.field = create_3d_grid(*dimensions) if len(dimensions) == 3 else create_grid(*dimensions[:2])
        self.type = field_type
        self.intensity = intensity
        self.decay_rate = decay_rate
        self.position = position if position else (random.uniform(0, dimensions[0]), random.uniform(0, dimensions[1]), random.uniform(0, dimensions[2]) if len(dimensions) == 3 else 0)
        self.dimensions = dimensions
        self.memory = []  # Store past states (for visualization)
        self.depth = dimensions[2] if len(dimensions) == 3 else None  # Correct depth assignment

    def update(self):
        for z in range(self.depth) if self.depth else [0]:
            for y in range(self.dimensions[1]):
                for x in range(self.dimensions[0]):
                    self.field[z][y][x] *= (1 - self.decay_rate)
                    self.field[z][y][x] += random.uniform(-0.05, 0.05) * self.intensity
                    self.field[z][y][x] = max(min(self.field[z][y][x], 1), -1)
        self.memory.append([row[:] for row in self.field])  # Store a copy

    def influence(self, pos):
        # Calculate influence based on distance from the field's center
        if len(self.dimensions) == 2:  # 2D
            dx = pos[0] - self.position[0]
            dy = pos[1] - self.position[1]
            distance = math.sqrt(dx**2 + dy**2)
        else:  # 3D
            dx = pos[0] - self.position[0]
            dy = pos[1] - self.position[1]
            dz = pos[2] - self.position[2]
            distance = math.sqrt(dx**2 + dy**2 + dz**2)

        max_influence_distance = max(self.dimensions) / 2
        return self.intensity * max(0, 1 - distance / max_influence_distance)

    def visualize(self, screen):
        # Placeholder for visualization logic (adapt for 2D/3D)
        pass

# --- Agent Class ---
class IntentAgent(object):
    def __init__(self, agent_id, x, y, z=0, agent_type="basic", perception_radius=50, max_speed=2, dimensions=(WIDTH, HEIGHT, DEPTH)):
        self.id = agent_id
        self.x = x
        self.y = y
        self.z = z
        self.type = agent_type
        self.perception_radius = perception_radius
        self.max_speed = max_speed
        self.dimensions = dimensions  # Store dimensions
        if len(dimensions) == 3:
            self.vx, self.vy, self.vz = random_vector(0.5)
        else:
            self.vx, self.vy = random_vector(0.5)
            self.vz = 0
        self.knowledge = 0.0
        self.memory = []  # Store interactions
        self.communication_log = []
        self.intent_alignment = 0.0
        self.initial_x = x  # Store initial position for uncertainty calculation
        self.initial_y = y
        self.initial_z = z if len(dimensions) == 3 else 0

    def perceive(self, intent_fields):
        self.intent_alignment = 0.0
        for field in intent_fields:
            influence = field.influence(self.position())
            if influence > 0:
                self.intent_alignment += influence
                self.memory.append((field.type, influence))

    def communicate(self, other_agents):
        for other in other_agents:
            if other != self:
                dist = self.distance_to(other)
                if dist < self.perception_radius:
                    # Simplified: Exchange a fraction of knowledge
                    shared_knowledge = min(self.knowledge, other.knowledge) * 0.1
                    self.knowledge -= shared_knowledge
                    other.knowledge += shared_knowledge
                    self.communication_log.append({"with": other.id, "amount": shared_knowledge})

    def act(self):
        # Move based on intent alignment (simplified)
        dx, dy = random_vector(min(self.intent_alignment, self.max_speed))
        dz = random.uniform(-1, 1) * min(self.intent_alignment, self.max_speed) if self.dimensions[2] else 0

        self.x = (self.x + dx) % self.dimensions
