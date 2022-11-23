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
H = np.arange(26)
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
mean_global = []
mean_clustering = []

velocity = functions.get_velocity(orientations, v)
orientation_list = [orientations]
particle_list = [particles]


for h in H:
    particle_list = []
    orientation_list = []
    particles = np.load('init_particles_8_8.npy')
    orientations = np.load('init_orientation_8_8.npy')
    velocity = functions.get_velocity(orientations, v)
    orientation_list = [orientations]
    particle_list = [particles]
    for i in trange(iterations):
        if i > h > 0:
            global_alignment[i] = functions.get_global_alignment(velocity, v)
            clustering[i] = functions.get_global_clustering(particles, R, L)
            orientations = functions.update_orientation(particle_list[i-h], orientation_list[i-h], eta, delta_t, R, L)
            velocity = functions.get_velocity(orientation_list[i-h], v)
            particles = functions.update_positions(particles, velocity, delta_t, L)
        else:
            global_alignment[i] = functions.get_global_alignment(velocity, v)
            clustering[i] = functions.get_global_clustering(particles, R, L)
            orientations = functions.update_orientation(particles, orientations, eta, delta_t, R, L)
            velocity = functions.get_velocity(orientations, v)
            particles = functions.update_positions(particles, velocity, delta_t, L)

        orientation_list.append(orientations)
        particle_list.append(particles)
        if i + 1 == 1000:
            particles_1000_h.append(particles)
        if i + 1 == 10000:
            particles_10000_h.append(particles)
    mean_global.append(np.mean(global_alignment))
    mean_clustering.append(np.mean(clustering))


# Iterations 1000
functions.plot_voronoi(particles_1000_h[0], L)
plt.title(f'Configuration after {iterations} iterations. R={R}, noise={eta}, N={N}, h={0}')

functions.plot_voronoi(particles_1000_h[3], L)
plt.title(f'Configuration after {iterations} iterations. R={R}, noise={eta}, N={N}, h={2}')

functions.plot_voronoi(particles_1000_h[26], L)
plt.title(f'Configuration after {iterations} iterations. R={R}, noise={eta}, N={N}, h={25}')

functions.plot_voronoi(particles_10000_h[0], L)
plt.title(f'Configuration after {iterations} iterations. R={R}, noise={eta}, N={N}, h={0}')

functions.plot_voronoi(particles_10000_h[3], L)
plt.title(f'Configuration after {iterations} iterations. R={R}, noise={eta}, N={N}, h={2}')

functions.plot_voronoi(particles_10000_h[26], L)
plt.title(f'Configuration after {iterations} iterations. R={R}, noise={eta}, N={N}, h={25}')


fig, ax = plt.subplots()
ax.scatter(H, mean_global, label='Global alignment')
ax.scatter(H, mean_clustering, label='Global clustering')
leg = ax.legend([r'$\psi$', r'$c$'])
plt.xlabel('h')
plt.ylabel(r'$\psi$, $c$')
plt.title(f'Iterations={iterations}. Parameters: R={R}, noise={eta}, N={N}')
plt.show()