import matplotlib.pyplot as plt
import SIR as sir
import numpy as np
from datetime import datetime

# Parameters
lattice = 100
nAgents = 1000
infection_rate = 0.01   # Initial infection_rate
move_prob = 0.8
beta = 0.3               # Infection probability
gamma = 0.03             # Recover probability
alpha = 0.005            # Re-susceptible probability
mu = None

# Initialization
alpha_unicode = "\u03B1"
gamma_unicode = "\u03B3"
beta_unicode = "\u03B2"
mu_unicode = "\u03BC"
infected_overtime = []
recovered_overtime = []
susceptible_overtime = []
diseased_overtime = []
timestep = 0

recovered = []
diseased = []
susceptible, infected = sir.initialize_world(lattice, nAgents, infection_rate)


while len(infected) > 0 and timestep < 10000:
    sir.walk(susceptible, move_prob, lattice)
    sir.walk(infected, move_prob, lattice)
    sir.walk(recovered, move_prob, lattice)

    infected, susceptible = sir.check_infected(infected, susceptible, beta)
    recovered, infected = sir.recovery(infected, recovered, gamma)
    susceptible, recovered = sir.re_susceptible(susceptible, recovered, alpha)

    susceptible_overtime.append(len(susceptible))
    infected_overtime.append(len(infected))
    recovered_overtime.append(len(recovered))
    diseased_overtime.append(len(diseased))

    timestep += 1
    print(timestep)
    print(f'infected: {len(infected)}')

sir.plot_sir(susceptible_overtime, infected_overtime, recovered_overtime, diseased_overtime, gamma, move_prob, beta, mu, alpha)
plt.show()