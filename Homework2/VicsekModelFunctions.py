import numpy as np



def generate_particles(N, L):
    particles = np.random.randint(0, L, [N, 2])
    for index, particle in enumerate(particles):
        delta_rx = np.random.rand()
        delta_ry = np.random.rand()
        particle[index]
    return particles