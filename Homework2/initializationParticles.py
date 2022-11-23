import numpy as np
from VicsekModelFunctions import generate_particle_positions, PBC
L = 100
N = 100
particles, orientation = generate_particle_positions(N, L)

np.save('init_particles_k', particles)
np.save('init_orientation_k', orientation)
