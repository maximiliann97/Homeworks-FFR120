import numpy as np
from scipy.spatial import Voronoi, ConvexHull


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
        x_distance = np.abs(particles[i, 0] - particles[:, 0])
        y_distance = np.abs(particles[i, 1] - particles[:, 1])
        min_x_distance = np.minimum(x_distance, L-x_distance)
        min_y_distance = np.minimum(y_distance, L - y_distance)
        distance = np.sqrt(min_x_distance**2 + min_y_distance**2)
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


def get_global_alignment(velocity, v=1):
    summation = np.sum(velocity, axis=0)
    global_coeff = np.linalg.norm(summation)/(v*len(velocity))
    return global_coeff



def get_global_clustering(particles, R):
    count = 0
    N = len(particles)
    vor = Voronoi(particles)
    for index, _ in enumerate(particles):
        iPoly = vor.point_region[index]
        iCorners = vor.regions[iPoly]
        poly_corners = vor.vertices[iCorners]
        area = poly_area(poly_corners)
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
        updated_orientation[index] = average + eta/2 * W[index] * delta_t
    return updated_orientation


def update_positions(particles, velocity, delta_t, L):
    updated_pos = PBC(particles + velocity * delta_t, L)
    return updated_pos

