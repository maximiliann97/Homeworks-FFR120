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
eta = 0.01
R = 20
iterations = 10000
H = [0, 2, 25]
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
mean_global = []
mean_clustering = []


velocity = functions.get_velocity(orientations, v)
orientation_list = [orientations]
particle_list = [particles]

for h in H:
    particle_list = []
    orientation_list = []
    particles = np.load('init_particles_8.8.2.npy')
    orientations = np.load('init_orientation_8.8.2.npy')
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
    if h == 0 or h == 2 or h == 25:
        global_list.append(global_alignment)
        clustering_list.append(clustering)
    mean_global.append(np.mean(global_alignment))
    mean_clustering.append(np.mean(clustering))


#functions.plot_voronoi(particles_10000_h[1], L)
#plt.title(f'Configuration after {10000} iterations. R={R}, noise={eta}, N={N}, h={2}')

#functions.plot_voronoi(particles_10000_h[2], L)
#plt.title(f'Configuration after {10000} iterations. R={R}, noise={eta}, N={N}, h={25}')


fig3, ax4 = plt.subplots()
ax4.scatter(H, mean_global, label='Global alignment')
ax4.scatter(H, mean_clustering, label='Global clustering')
ax4.legend([r'$\psi$', r'$c$'])
plt.xlabel('h')
plt.ylabel(r'$\psi$, $c$')
plt.title(f'Iterations={iterations}. Parameters: R={R}, noise={eta}, N={N}')
plt.show()