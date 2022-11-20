import numpy as np
from scipy.spatial import Voronoi, ConvexHull


def PBC(particles, L):
    for _, particle in enumerate(particles):
        if particle[0] < -L/2:
            particle[0] = particle[0] + L
        elif particle[0] > L/2:
            particle[0] = particle[0] - L

        if particle[1] < -L/2:
            particle[1] = particle[1] + L
        elif particle[1] > L/2:
            particle[1] = particle[1] - L

    return particles


def generate_particle_positions(N, L):
    particles = np.random.rand(N, 2) * 2 * L - L/2
    theta = np.random.rand(N)*2*np.pi
    return [PBC(particles, L), theta]


def particles_in_radius(particles, r):
    particle_dict = dict()
    temp_list = []
    for i, _ in enumerate(particles):
        for j, _ in enumerate(particles):
            if i != j:
                if np.linalg.norm(particles[i]-particles[j]) < r:
                    temp_list.append(j)
        particle_dict[i] = temp_list
        temp_list = []

    return particle_dict


def get_velocity(theta, v=1):
    velocity = np.zeros([len(theta), 2])
    velocity[:, 0] = v*np.cos(theta)
    velocity[:, 1] = v*np.sin(theta)
    return velocity


def get_global_alignment(velocity, v=1):
    summation = np.sum(velocity, axis=0)/v
    coeff = 1/len(velocity[:, 0]) * np.linalg.norm(summation)
    return coeff


def voronoi_tessellation():
    voronoi_area = 1
    return voronoi_area


def get_global_clustering(particles, r):
    count = 0
    for index, particle in enumerate(particles):
        vor = Voronoi(particle)
        area = voronoi_tessellation()
        if area < np.pi*r**2:
            count += 1

    coeff = count/len(particles[:, 0])
    return coeff

