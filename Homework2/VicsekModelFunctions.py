import numpy as np
from scipy.spatial import Voronoi, ConvexHull, voronoi_plot_2d
import matplotlib.pyplot as plt
import math


def generate_particle_positions(N, L, displacement=None):
    particles = np.random.rand(N, 2) * L - L/2
    orientations = np.random.rand(N)*2*np.pi
    if displacement:
        particles[:, 0] = particles[:, 0] + displacement
        particles[:, 1] = particles[:, 1] + displacement
    particles = PBC(particles, L)
    return [particles, orientations]


def PBC(particles, L):
    for index, particle in enumerate(particles):
        x = particle[0]
        y = particle[1]

        if x < -L/2:
            particles[index, 0] = x + L
        elif x > L/2:
            particles[index, 0] = x - L

        if y < -L/2:
            particles[index, 1] = y + L
        elif y > L/2:
            particles[index, 1] = y - L

    return particles


def particles_in_radius(particles, R, L):
    N = len(particles)
    particle_indices = []
    for i in range(N):
        x_dist = np.abs(particles[i, 0] - particles[:, 0])
        y_dist = np.abs(particles[i, 1] - particles[:, 1])
        min_x_dist = np.minimum(x_dist, L-x_dist)
        min_y_dist = np.minimum(y_dist, L - y_dist)
        distance = np.sqrt(min_x_dist**2 + min_y_dist**2)
        indices = np.where(distance < R)
        particle_indices.append(indices)
    return particle_indices


def get_velocity(orientations, v=1):
    N = len(orientations)
    velocity = np.zeros((N, 2))
    for i in range(N):
        theta = orientations[i]
        velocity[i, 0] = v*np.cos(theta)
        velocity[i, 1] = v*np.sin(theta)
    return velocity


def get_global_alignment(velocity, v):
    summation = np.sum(velocity, axis=0)
    global_coeff = np.linalg.norm(summation)/(v*len(velocity))
    return global_coeff


def get_global_clustering(particles, R, L):
    count = 0
    N = len(particles)
    replica = replicas(particles, L)
    expanded_particles = np.copy(particles)

    for j in range(len(replica)):
        expanded_particles = np.append(expanded_particles, replica[j], axis=0)

    vor = Voronoi(expanded_particles)
    for index, _ in enumerate(particles):
        iPoly = vor.point_region[index]
        iCorners = vor.regions[iPoly]
        poly_vertices = vor.vertices[iCorners]
        area = poly_area(poly_vertices)
        if area < np.pi*R**2:
            count += 1
    clust_coeff = count/N
    return clust_coeff


def poly_area(corners):
    x = corners[:, 0]
    y = corners[:, 1]
    area = 0.5*np.abs(np.dot(x, np.roll(y, 1))-np.dot(y, np.roll(x, 1)))
    return area


def update_orientation(particles, orientations, eta, delta_t, R, L):
    N = len(orientations)
    W = np.random.uniform(-1/2, 1/2, N)
    neighbours_of_particles = particles_in_radius(particles, R, L)
    updated_orientation = np.zeros(N)
    for index in range(N):
        neighbours = neighbours_of_particles[index][0]
        neighbours_orientation = orientations[neighbours]
        if len(neighbours_orientation) == 1:
            average = neighbours_orientation
        else:
            average = np.arctan(np.mean(np.sin(neighbours_orientation))/np.mean(np.cos(neighbours_orientation)))
        updated_orientation[index] = average + eta * W[index] * delta_t
    return updated_orientation


def update_positions(particles, velocity, delta_t, L):
    updated_pos = PBC(particles + velocity * delta_t, L)
    return updated_pos


def replicas(x, L):
    x_replica_right = np.copy(x)
    x_replica_right[:, 0] = x_replica_right[:, 0] + L

    x_replica_left = np.copy(x)
    x_replica_left[:, 0] = x_replica_left[:, 0] - L

    x_replica_up = np.copy(x)
    x_replica_up[:, 1] = x_replica_up[:, 1] + L

    x_replica_down = np.copy(x)
    x_replica_down[:, 1] = x_replica_down[:, 1] - L

    x_replica_diag1 = np.copy(x)
    x_replica_diag1[:, :] = x_replica_diag1[:, :] + L

    x_replica_diag2 = np.copy(x)
    x_replica_diag2[:, :] = x_replica_diag2[:, :] - L

    x_replica_diag3 = np.copy(x)
    x_replica_diag3[:, 0] = x_replica_diag3[:, 0] + L
    x_replica_diag3[:, 1] = x_replica_diag3[:, 1] - L

    x_replica_diag4 = np.copy(x)
    x_replica_diag4[:, 0] = x_replica_diag4[:, 0] - L
    x_replica_diag4[:, 1] = x_replica_diag4[:, 1] + L

    x_replica = [x_replica_down, x_replica_up, x_replica_right, x_replica_left,
             x_replica_diag1, x_replica_diag2, x_replica_diag3, x_replica_diag4]
    return x_replica


def plot_voronoi(particles, L):
    replica = replicas(particles, L)
    expanded_particles = np.copy(particles)

    for i in range(len(replica)):
        expanded_particles = np.append(expanded_particles, replica[i], axis=0)

    vor = Voronoi(expanded_particles)
    voronoi_plot_2d(vor, show_vertices=False)
    plt.xlim(- L / 2, L / 2)
    plt.ylim(- L / 2, L / 2)


def update_orientation_2(orientations, neighbours_of_particle, eta, delta_t):
    N = len(orientations)
    W = np.random.uniform(-1/2, 1/2, N)
    updated_orientation = np.zeros(N)
    for index in range(N):
        neighbours = neighbours_of_particle[index]
        neighbours_orientation = orientations[neighbours]
        neighbours_orientation = [neighbours_orientation]
        if len(neighbours_orientation) == 1:
            average = neighbours_orientation
        else:
            average = np.arctan(np.mean(np.sin(neighbours_orientation))/np.mean(np.cos(neighbours_orientation)))
        updated_orientation[index] = average + eta * W[index] * delta_t
    return updated_orientation


def particles_in_radius_2(particles, R, L):
    N = len(particles)
    particle_indices = []
    for i in range(N):
        x_dist = np.abs(particles[i, 0] - particles[:, 0])
        y_dist = np.abs(particles[i, 1] - particles[:, 1])
        min_x_dist = np.minimum(x_dist, L-x_dist)
        min_y_dist = np.minimum(y_dist, L - y_dist)
        distance = np.sqrt(min_x_dist**2 + min_y_dist**2)
        indices = np.where(distance < R)
        indices = indices[0][0]
        particle_indices.append(indices)
    return particle_indices


def k_nearest(particles, L, k):
    N = len(particles)
    particle_indices = []
    for i in range(N):
        x_dist = np.abs(particles[i, 0] - particles[:, 0])
        y_dist = np.abs(particles[i, 1] - particles[:, 1])
        min_x_dist = np.minimum(x_dist, L - x_dist)
        min_y_dist = np.minimum(y_dist, L - y_dist)
        distance = np.sqrt(min_x_dist**2 + min_y_dist**2)
        sorted_distance = np.argsort(distance)
        sorted_distance_indices = sorted_distance[0:k+1]
        particle_indices.append(sorted_distance_indices)
    return particle_indices

def update_orientation_knearest(particles, orientations, eta, delta_t, R, L, k, vision):
    N = len(orientations)
    W = np.random.uniform(-1/2, 1/2, N)
    neighbours_of_particles = k_nearest(particles, L, k, vision)
    updated_orientation = np.zeros(N)
    for index in range(N):
        neighbours = neighbours_of_particles[index]
        neighbours_orientation = orientations[neighbours]
        average = np.arctan(np.mean(np.sin(neighbours_orientation))/np.mean(np.cos(neighbours_orientation)))
        updated_orientation[index] = average + eta * W[index] * delta_t
    return updated_orientation