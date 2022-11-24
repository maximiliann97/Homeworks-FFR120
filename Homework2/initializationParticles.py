import numpy as np
from VicsekModelFunctions import generate_particle_positions, PBC
L = 150
N = 200
particles, orientation = generate_particle_positions(N, L)

np.save('init_particles_8.8.2', particles)
np.save('init_orientation_8.8.2', orientation)
