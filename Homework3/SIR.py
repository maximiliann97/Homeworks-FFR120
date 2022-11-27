from Individual import Individual
import matplotlib.pyplot as plt
import numpy as np


def initialize_world(lattice, nAgents, infection_rate):
    nInfected = 0
    nSusceptible = 0
    for _ in range(nAgents):
        r = np.random.rand()
        if r < infection_rate:
            nInfected += 1
        else:
            nSusceptible += 1

    susceptible = [Individual("susceptible", lattice) for _ in range(nSusceptible)]
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


def walk(object_list, prob, lattice):
    for obj in object_list:
        random_walk(obj, prob, lattice)

"""
Spreading the disease in the neighbourhood

def check_infected(infected, susceptible, beta):
    for infectant in infected:
        r = np.random.rand()
        if r < beta:
            to_the_right = np.array([infectant.position[0] + 1, infectant.position[1]])
            to_the_left = np.array([infectant.position[0] - 1, infectant.position[1]])
            over = np.array([infectant.position[0], infectant.position[1] + 1])
            under = np.array([infectant.position[0], infectant.position[1] - 1])
            for s in susceptible:
                if np.array_equal(s.position, to_the_right) or np.array_equal(s.position, to_the_left) or \
                            np.array_equal(s.position, over) or np.array_equal(s.position, under)\
                            or np.array_equal(s.position, infectant.position):

                    s.update_state('infected')
                    infected.append(s)
                    susceptible.remove(s)
    return infected, susceptible
"""


def check_infected(infected, susceptible, beta):
    for infectant in infected:
        r = np.random.rand()
        if r < beta:
            for s in susceptible:
                if np.array_equal(s.position, infectant.position):
                    s.update_state("infected")
                    infected.append(s)
                    susceptible.remove(s)
    return infected, susceptible



def recovery(infected, recovered, gamma):
    for i in infected:
        r = np.random.rand()
        if r < gamma:
            i.update_state('recovered')
            recovered.append(i)
            infected.remove(i)
    return recovered, infected


def death(diseased, infected, mu):
    for i in infected:
        r = np.random.rand()
        if r < mu:
            i.update_state('diseased')
            diseased.append(i)
            infected.remove(i)
    return diseased, infected


def re_susceptible(susceptible, recovered, alpha):
    for s in susceptible:
        r = np.random.rand()
        if r < alpha:
            s.update_state("susceptible")
            susceptible.append(s)
            recovered.remove(s)
    return susceptible, recovered


def plot_sir(susceptible, infected, recovered, diseased, gamma, d, beta, mu=None, alpha=None):
    alpha_unicode = "\u03B1"
    gamma_unicode = "\u03B3"
    beta_unicode = "\u03B2"
    mu_unicode = "\u03BC"
    plt.plot(susceptible, color='blue')
    plt.plot(infected, color='orange')
    plt.plot(recovered, color='green')
    plt.plot(diseased, color='red')
    plt.legend(
        ["Susceptible", "Infected", "Recovered", "Diseased"])
    plt.ylabel('Number of Agents')
    plt.xlabel('t')
    plt.title(f'Parameters: {gamma_unicode}={gamma}, {beta_unicode}={beta}, d={d}, {alpha_unicode}={alpha}, {mu_unicode}={mu}')


def plot_lattice(infected, susceptible, recovered, diseased):
    x_infected = [obj.position[0] for obj in infected]
    y_infected = [obj.position[1] for obj in infected]

    x_susceptible = [obj.position[0] for obj in susceptible]
    y_susceptible = [obj.position[1] for obj in susceptible]

    x_recovered = [obj.position[0] for obj in recovered]
    y_recovered = [obj.position[1] for obj in recovered]

    x_diseased = [obj.position[0] for obj in diseased]
    y_diseased = [obj.position[1] for obj in diseased]

    plt.plot(x_infected, y_infected, "o", color="orange", markersize=4)
    plt.plot(x_susceptible, y_susceptible, "o", color="blue", markersize=4)
    plt.plot(x_recovered, y_recovered, "o", color="green", markersize=4)
    plt.plot(x_diseased, y_diseased, "x", color="red", markersize=4)
    plt.legend(
        ["Infected", "Susceptible", "Recovered", "Diseased"])
    plt.title(f"#Inf = {len(infected)} #Sus = {len(susceptible)} #Rec = {len(recovered)} #Dis = {len(diseased)}")
