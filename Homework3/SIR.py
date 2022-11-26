from Individual import Individual
import numpy as np


def initialize_world(lattice, nAgents, infection_rate):
    nInfected = 0
    nSuspectible = 0
    for _ in range(nAgents):
        r = np.random.rand()
        if r < infection_rate:
            nInfected += 1
        else:
            nSuspectible += 1

    susceptible = [Individual("susceptible", lattice) for _ in range(nSuspectible)]
    infected = [Individual("infected", lattice) for _ in range(nInfected)]

    return susceptible, infected


def random_walk(individual, move_prob, lattice):
    r = np.random.randn()
    if r < move_prob:
        d = np.random.randint(4)
        if d == 0:
            individual.move('up', lattice)
        if d == 1:
            individual.move('down', lattice)
        if d == 2:
            individual.move('right', lattice)
        if d == 3:
            individual.move('left', lattice)


def check_infected(infected, susceptible, beta):
    for infectant in infected:
        right = infectant.position[0] + 1
        left = infectant.position[0] - 1
        up = infectant.position[1] + 1
        down = infectant.position[1] - 1
        proximity = [right, left, up, down]
        for s in susceptible:
            if s.position[0] == proximity[0] or s.position[0] == proximity[1] or s.position[1] == proximity[2] or s.position[1] == proximity[3]:
                r = np.random.randn()
                if r < beta:
                    s.update_state('infected')
                    infected.append(s)
                    susceptible.remove(s)
    return infected, susceptible


def recovery(infected, recovered, gamma):
    for i in infected:
        r = np.random.randn()
        if r < gamma:
            i.update_state('recovered')
            recovered.append(i)
            infected.remove(i)
    return recovered, infected


def plot_sir(susceptible, infected, recovered, timestep):
    