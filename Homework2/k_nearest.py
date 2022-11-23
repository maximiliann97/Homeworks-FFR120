import VicsekModelFunctions as functions
from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange

#########################################
# Initialization parameters
N = 100
L = 100
v = 1
delta_t = 1
eta = 0.1
R = 1
iterations = 10000
k = 5
#########################################

particles = np.load('init_particles.npy')
orientations = np.load('init_orientation.npy')

functions.plot_voronoi(particles, L)
plt.xlim([-L/2, L/2])
plt.title(f'Initial configuration. Parameters: R={R}, noise={eta}, N={N}')


times = np.arange(iterations)
orientations = functions.update_orientation_knearest(particles, orientations, eta, delta_t, R, L, k)

for i in trange(iterations):
    velocity = functions.get_velocity(orientations, v)
    particles = functions.update_positions(particles, velocity, delta_t, L)
    orientations = functions.update_orientation_knearest(particles, orientations, eta, delta_t, R, L, k)



functions.plot_voronoi(particles, L)
plt.title(f'Configuration after {iterations} iterations, R={R}, noise={eta}, N={N}, k={k}')
plt.show()