import VicsekModelFunctions as functions
from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np
import matplotlib.pyplot as plt

#########################################
# Initialization parameters
L = 100
N = 100
v = 1
delta_t = 1
eta = 0.01
R = 1
iterations = 10000
#########################################

particles = np.load('init_particles.npy')
orientations = np.load('init_orientation.npy')

vor = Voronoi(particles)
fig1 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-50, 50])
plt.title(f'Initial configuration. R={R}, noise={eta}, N={N}')


global_alignment = np.zeros(iterations)
clustering = np.zeros(iterations)
times = np.arange(iterations)

for i in range(iterations):
    orientations = functions.update_orientation(particles, orientations, eta, delta_t, R, L)
    velocity = functions.get_velocity(orientations, v)
    particles = functions.update_positions(particles, velocity, delta_t, L)
    global_alignment[i] = functions.get_global_alignment(velocity, v)
    clustering[i] = functions.get_global_clustering(particles, R)
    if i == 9:
        particles_10 = particles
    if i == 99:
        particles_100 = particles
    if i == 499:
        particles_500 = particles
    if i == 999:
        particles_1000 = particles


# Iterations = 10000
vor = Voronoi(particles)
fig2 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-L/2, L/2])
plt.ylim([-L/2, L/2])
plt.title(f'Configuration after {iterations} iterations. R={R}, noise={eta}, N={N}')

# Iterations = 10
vor = Voronoi(particles_10)
fig3 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-L/2, L/2])
plt.ylim([-L/2, L/2])
plt.title(f'Configuration after {10} iterations. R={R}, noise={eta}, N={N}')

# Iterations = 100
vor = Voronoi(particles_100)
fig4 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-L/2, L/2])
plt.ylim([-L/2, L/2])
plt.title(f'Configuration after {100} iterations. R={R}, noise={eta}, N={N}')

# Iterations = 500
vor = Voronoi(particles_500)
fig4 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-L/2, L/2])
plt.ylim([-L/2, L/2])
plt.title(f'Configuration after {500} iterations. R={R}, noise={eta}, N={N}')

# Iterations = 1000
vor = Voronoi(particles_1000)
fig5 = voronoi_plot_2d(vor, show_vertices=False)
plt.xlim([-L/2, L/2])
plt.ylim([-L/2, L/2])
plt.title(f'Configuration after {1000} iterations. R={R}, noise={eta}, N={N}')




fig, ax = plt.subplots()
ax.plot(times, global_alignment, label='Global alignment')
ax.plot(times, clustering, label='Global clustering')
leg = ax.legend()
plt.xlabel('t')
plt.ylabel('Clustering coefficient and alignment coefficient')
plt.title(f'Iterations={iterations}. R={R}, noise={eta}, N={N}')
plt.show()