from Individual import Individual
import matplotlib.pyplot as plt
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
    r = np.random.rand()
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


def walk(list, prob, lattice):
    for object in list:
        random_walk(object, prob, lattice)


def check_infected(infected, susceptible, beta):
    for infectant in infected:
        r = np.random.rand()
        to_the_right = np.array([infectant.position[0] + 1, infectant.position[1]])
        to_the_left = np.array([infectant.position[0] - 1, infectant.position[1]])
        over = np.array([infectant.position[0], infectant.position[1] + 1])
        under = np.array([infectant.position[0], infectant.position[1] - 1])
        for s in susceptible:
            if np.array_equal(s.position, to_the_right) or np.array_equal(s.position, to_the_left) or \
                    np.array_equal(s.position, over) or np.array_equal(s.position, under):
                if r > beta:
                    s.update_state('infected')
                    infected.append(s)
                    susceptible.remove(s)
    return infected, susceptible


# def check_infected(infected, susceptible, beta):
#     for infectant in infected:
#         r = np.random.rand()
#         if r < beta:
#             for s in susceptible:
#                 if np.array_equal(s.position, infectant.position):
#                     s.update_state("infected")
#                     infected.append(s)
#                     susceptible.remove(s)
#     return infected, susceptible


def recovery(infected, recovered, gamma):
    for i in infected:
        r = np.random.rand()
        if r < gamma:
            i.update_state('recovered')
            recovered.append(i)
            infected.remove(i)
    return recovered, infected


def plot_sir(susceptible, infected, recovered, timestep):
    plt.plot(susceptible, color='blue')
    plt.plot(infected, color='orange')
    plt.plot(recovered, color='green')
    plt.legend(
        ["Susceptible", "Infected", "Recovered",])
    plt.show()