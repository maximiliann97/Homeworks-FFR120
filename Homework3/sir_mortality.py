import matplotlib.pyplot as plt
import SIR as sir
import numpy as np

# Parameters
lattice = 100
nAgents = 1000
infection_rate = 0.01
move_prob = 0.8
beta = 0.6                           # Infection probability
gamma = [0.01, 0.02]                 # Recover probability
mu = np.linspace(0.001, 0.2, 20)     # Death probability

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


for i, g in enumerate(gamma):
    death_list = []
    for m in mu:
        timestep = 0
        recovered = []
        diseased = []
        susceptible, infected = sir.initialize_world(lattice, nAgents, infection_rate)
        while len(infected) > 0:
            sir.walk(susceptible, move_prob, lattice)
            sir.walk(infected, move_prob, lattice)
            sir.walk(recovered, move_prob, lattice)

            infected, susceptible = sir.check_infected(infected, susceptible, beta)
            recovered, infected = sir.recovery(infected, recovered, g)
            diseased, infected = sir.death(diseased, infected, m)

            susceptible_overtime.append(len(susceptible))
            infected_overtime.append(len(infected))
            recovered_overtime.append(len(recovered))
            diseased_overtime.append(len(diseased))

            timestep += 1
            print(timestep)
            print(f'infected: {len(infected)}')
        death_list.append(len(diseased))
    if i == 0:
        plt.plot(mu, death_list, "o", color="blue", markersize=4)
    if i == 1:
        plt.plot(mu, death_list, "o", color="green", markersize=4)


# Plot final deaths as a function of mortality rate
plt.legend([f"{gamma_unicode}={gamma[0]}", f"{gamma_unicode}={gamma[1]}"])
plt.xlabel(f'{mu_unicode}')
plt.title(f"Final number of dead agents as a function of the mortality rate {mu_unicode}")
plt.savefig(f'Final number of dead agents as a function of the mortality rate {mu_unicode}.png')
plt.show()