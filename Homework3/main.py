import matplotlib.pyplot as plt
import SIR as sir

# Parameters
lattice = 100
nAgents = 1000
infection_rate = 0.01
move_prob = 0.8
beta = 0.2
gamma = 0.01

# Initialization
timestep = 0
recovered = []
susceptible, infected = sir.initialize_world(lattice, nAgents, infection_rate)

while len(infected) > 0:
    for s in susceptible:
        sir.random_walk(s, move_prob, lattice)

    for i in infected:
        sir.random_walk(i, move_prob, lattice)

    for r in recovered:
        sir.random_walk(r, move_prob, lattice)

    infected, susceptible = sir.check_infected(infected, susceptible, beta)
    recovered, infected = sir.recovery(infected, recovered, gamma)
    timestep += 1