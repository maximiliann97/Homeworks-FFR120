import numpy as np
from collections import Counter

def initialize_world(N, nAgents):
    world = np.zeros([N, N])
    while np.sum(world) < 1000:
        random_index = np.random.randint(N, size=2)
        world[random_index[0], random_index[1]] = 1
    return world

print(initialize_world(100, 1000))
