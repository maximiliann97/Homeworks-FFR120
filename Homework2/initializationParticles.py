import numpy as np
from VicsekModelFunctions import generate_particle_positions, PBC

L = 1000
N = 100
particles, orientation = generate_particle_positions(N, L)

np.save('init_particles_8_8', particles)
np.save('init_orientation_8_8', orientation)