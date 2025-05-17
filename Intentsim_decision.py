# intentsim_enhanced.py

import pygame
import random
import math
import json
import os

# --- Configuration ---
WIDTH, HEIGHT = 1000, 800
AGENT_COUNT = 150
DATA_DIR = "sim_data"

# --- Helper Functions ---
def random_vector(magnitude=1.0):
    angle = random.uniform(0, 2 * math.pi)
    return math.cos(angle) * magnitude, math.sin(angle) * magnitude

# --- Intent Field ---
class IntentField:
    def __init__(self, field_type, intensity, position):
        self.type = field_type
        self.intensity = intensity
        self.position = position  # (x, y)
        self.decay_rate = 0.001

    def influence(self, pos):
        dx, dy = pos[0] - self.position[0], pos[1] - self.position[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)
        max_distance = 200.0
        return self.intensity * max(0, 1 - distance / max_distance)

# --- Intent Agent ---
class IntentAgent:
    def __init__(self, x, y, agent_id):
        self.x = x
        self.y = y
        self.id = agent_id
        self.vx, self.vy = random_vector(1.0)
        self.knowledge = 0.0
        self.intent_alignment = 0.0
        self.memory = []
        self.color = (100, 200, 255)

    def position(self):
        return (self.x, self.y)

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    # --- New Decision Framework ---

    def calculate_pressure(self, fields):
        return sum(f.influence(self.position()) for f in fields)

    def calculate_field_complexity(self, fields):
        return len(set(f.type for f in fields))

    def perceive_relevant_info(self, fields, agents):
        near_agents = [a for a in agents if a != self and self.distance_to(a) < 100]
        total_knowledge = sum(a.knowledge for a in near_agents)
        return total_knowledge / max(len(near_agents), 1)

    def generate_actions(self):
        return [random_vector(1.0) for _ in range(5)]

    def evaluate_actions(self, actions, intent_drive, pressure, load, info):
        scored = []
        for dx, dy in actions:
            value = intent_drive + pressure - 0.1 * load + 0.2 * info
            scored.append(((dx, dy), value + random.uniform(-0.5, 0.5)))
        return scored

    def select_action(self, scored):
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[0][0]

    def execute_action(self, dx, dy):
        self.x = (self.x + dx) % WIDTH
        self.y = (self.y + dy) % HEIGHT

    def calculate_knowledge_gain(self):
        return random.uniform(0.1, 0.3)

    def act(self, fields, agents):
        self.intent_alignment = sum(f.influence(self.position()) for f in fields)
        pressure = self.calculate_pressure(fields)
        load = self.calculate_field_complexity(fields)
        info = self.perceive_relevant_info(fields, agents)
        actions = self.generate_actions()
        scored = self.evaluate_actions(actions, self.intent_alignment, pressure, load, info)
        dx, dy = self.select_action(scored)
        self.execute_action(dx, dy)
        self.knowledge += self.calculate_knowledge_gain()
        self.memory.append((dx, dy, self.knowledge))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 4)

# --- Main Simulation ---
class IntentSim:
    def __init__(self):
        self.agents = [IntentAgent(random.uniform(0, WIDTH), random.uniform(0, HEIGHT), i) for i in range(AGENT_COUNT)]
        self.fields = [IntentField("challenge", 1.2, (WIDTH/2, HEIGHT/2))]
        self.running = True

    def step(self):
        for agent in self.agents:
            agent.act(self.fields, self.agents)

    def draw(self, screen):
        screen.fill((0, 0, 0))
        for agent in self.agents:
            agent.draw(screen)
        pygame.display.flip()

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("IntentSim Live Run")
        clock = pygame.time.Clock()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.step()
            self.draw(screen)
            clock.tick(30)

        pygame.quit()

if __name__ == "__main__":
    sim = IntentSim()
    sim.run()
