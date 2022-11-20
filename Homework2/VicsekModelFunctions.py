import numpy as np



def generate_particles(N, L):
    particles = np.random.randint(0, L, [N, 2])
    for _, particle in enumerate(particles):
        delta_rx = np.random.rand()
        delta_ry = np.random.rand()
        particle[0] = particle[0] + delta_rx
        particle[1] = particle[1] + delta_rx
    return particles


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


def particles_in_radius(particles, L, r):
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



def get_global_alignment(velocity):
    