
"""
Nature's Wisdom Bloom - Static High-Resolution Phase Space Frame
IntentSim Framework Visualization
This script generates a high-quality static frame of the
Dynamic Coherence-Entropy Phase Space Map for export.
"""

import numpy as np
import matplotlib.pyplot as plt

# Simulated data
np.random.seed(42)
steps = 200
entropy = np.clip(np.cumsum(np.random.randn(steps) * 0.005) + 0.26, 0.21, 0.30)
coherence = np.clip(np.cumsum(np.random.randn(steps) * 0.001) + 0.98, 0.98, 1.0)
complexity = np.clip(np.cumsum(np.random.randn(steps) * 0.002) + 0.94, 0.90, 1.00)
memory_inversions = np.random.randint(0, 60, steps)

fig, ax = plt.subplots(figsize=(10, 8))
sc = ax.scatter(entropy, coherence, s=memory_inversions * 2 + 10, 
                 c=complexity, cmap='plasma', vmin=0.90, vmax=1.00)
ax.set_xlim(0.21, 0.30)
ax.set_ylim(0.98, 1.0)
ax.set_xlabel("Entropy")
ax.set_ylabel("Coherence Index")
ax.set_title("Static Coherence-Entropy Phase Space Map")

ax.axvspan(0.21, 0.30, color='green', alpha=0.1, label="Creative Tension Zone")
ax.legend()

# Save high-res static frame
plt.savefig("IntentSim_Static_Phase_Space_Frame.png", dpi=300, facecolor='white')
plt.show()
