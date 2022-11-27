import matplotlib.pyplot as plt
import SIR as sir
import numpy as np
from datetime import datetime

# Parameters
lattice = 100
nAgents = 1000
infection_rate = 0.01   # Initial infection_rate
move_prob = 0.8
Beta = np.linspace(0.1, 0.9, 9)      # Infection probability
Gamma = [0.01, 0.02]                # Recover probability

# Initialization
alpha_unicode = "\u03B1"
gamma_unicode = "\u03B3"
beta_unicode = "\u03B2"
mu_unicode = "\u03BC"
infected_overtime = []
recovered_overtime = []
susceptible_overtime = []
diseased_overtime = []


for i, gamma in enumerate(Gamma):
    nrRecovered_list = []
    for beta in Beta:
        timestep = 0
        susceptible, infected = sir.initialize_world(lattice, nAgents, infection_rate)
        recovered = []
        diseased = []
        while len(infected) > 0:
            sir.walk(susceptible, move_prob, lattice)
            sir.walk(infected, move_prob, lattice)
            sir.walk(recovered, move_prob, lattice)

            infected, susceptible = sir.check_infected(infected, susceptible, beta)
            recovered, infected = sir.recovery(infected, recovered, gamma)

            susceptible_overtime.append(len(susceptible))
            infected_overtime.append(len(infected))
            recovered_overtime.append(len(recovered))
            diseased_overtime.append(len(diseased))

            timestep += 1
            print(timestep)
            print(f'infected: {len(infected)}')
        nrRecovered_list.append(len(recovered))
    if gamma == 0.01:
        time_now = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        nrRecovered_array = np.array(nrRecovered_list)
        np.save(time_now + f'R_inf_gamma={Gamma[0]}', nrRecovered_array)
        plt.plot(Beta, nrRecovered_list, "o", color="blue", markersize=4)
    if gamma == 0.02:
        time_now = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        nrRecovered_array = np.array(nrRecovered_list)
        np.save(time_now + f'R_inf_gamma={Gamma[1]}', nrRecovered_array)
        plt.plot(Beta, nrRecovered_list, "o", color="green", markersize=4)


# Plot final recovered as a function of infection rate
plt.legend([f"{gamma_unicode}={Gamma[0]}", f"{gamma_unicode}={Gamma[1]}"])
plt.xlabel(f'{beta_unicode}')
plt.title(f"Final number of recovered agents as a function of the infection rate {beta_unicode}")
