import VicsekModelFunctions as functions
from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange

#########################################
# Initialization parameters
N = 100
L = 1000
v = 3
delta_t = 1
eta = 0.4
R = 20
iterations = 10000
H = [0]
#########################################

# Load
particles = np.load('init_particles_8_8.npy')
orientations = np.load('init_orientation_8_8.npy')

# Initial plot
vor = Voronoi(particles)
fig1 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-L/2, L/2])
plt.title(f'Initial configuration. Parameters: R={R}, noise={eta}, N={N}')

# Initialization
global_alignment = np.zeros(iterations)
clustering = np.zeros(iterations)
times = np.arange(iterations)
particles_1000_h = []
particles_10000_h = []
global_list = []
clustering_list = []

velocity = functions.get_velocity(orientations, v)
neighbours_indices = functions.particles_in_radius_2(particles, R, L)
for h in H:
    for i in trange(iterations):
        global_alignment[i] = functions.get_global_alignment(velocity, v)
        clustering[i] = functions.get_global_clustering(particles, R, L)

        neighbours_indices2 = np.copy(neighbours_indices)
        velocity2 = np.copy(velocity)
        particles2 = np.copy(particles)

        for d in range(-h):
            neighbours_indices2 = functions.particles_in_radius_2(particles2, R, L)
            orientations = functions.update_orientation_2(orientations, neighbours_indices2, eta, delta_t)
            velocity2 = functions.get_velocity(orientations, v)
            particles2 = functions.update_positions(particles2, velocity2, delta_t, L)
        neighbours_indices2 = functions.particles_in_radius_2(particles2, R, L)
        orientations = functions.update_orientation_2(orientations, neighbours_indices, eta, delta_t)
        velocity = functions.get_velocity(orientations, v)
        particles = functions.update_positions(particles, velocity, delta_t, L)

        if i + 1 == 1000:
            particles_1000_h.append(particles)
        if i + 1 == 10000:
            particles_10000_h.append(particles)




functions.plot_voronoi(particles_10000_h[0], L)
plt.title(f'Configuration after {10000} iterations. R={R}, noise={eta}, N={N}, h={H[0]}')

fig, ax = plt.subplots()
ax.plot(times, global_alignment, label='Global alignment')
ax.plot(times, clustering, label='Global clustering')
leg = ax.legend([r'$\psi$',r'$c$'])
plt.xlabel('t')
plt.ylabel(r'$\psi$, $c$')
plt.title(f'Iterations={iterations}. Parameters: R={R}, noise={eta}, N={N}, h={H[0]}')
plt.show()