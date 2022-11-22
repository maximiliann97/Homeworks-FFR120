import numpy as np
from VicsekModelFunctions import generate_particle_positions, PBC

L = 100
N = 1000
particles, orientation = generate_particle_positions(N, L)

np.save('init_particles_2', particles)
np.save('init_orientation_2', orientation)