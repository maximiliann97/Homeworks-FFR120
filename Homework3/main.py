import matplotlib.pyplot as plt
import SIR as sir
import numpy as np

# Parameters
lattice = 100
nAgents = 1000
infection_rate = 0.01
move_prob = 0.8
Beta = [0.6]
#, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]    # Infection probability
gamma = [0.01]    # Recover probability
mu = np.linspace(0.01, 0.2, 5)     # Death probability
alpha = None    # Re-susceptible probability

# Initialization
alpha_unicode = "\u03B1"
gamma_unicode = "\u03B3"
beta_unicode = "\u03B2"
mu_unicode = "\u03BC"
infected_overtime = []
recovered_overtime = []
susceptible_overtime = []
diseased_overtime = []
R_list = []
death_list = []
timestep = 0

# recovered = []
# diseased = []
# susceptible, infected = sir.initialize_world(lattice, nAgents, infection_rate)

# sir.plot_lattice(infected, susceptible, recovered, diseased)
# plt.show()
for m in mu:
    timestep = 0
    recovered = []
    diseased = []
    susceptible, infected = sir.initialize_world(lattice, nAgents, infection_rate)
    for g in gamma:
        for beta in Beta:
            while len(infected) > 0:
                sir.walk(susceptible, move_prob, lattice)
                sir.walk(infected, move_prob, lattice)
                sir.walk(recovered, move_prob, lattice)

                infected, susceptible = sir.check_infected(infected, susceptible, beta)
                recovered, infected = sir.recovery(infected, recovered, g)
                diseased, infected = sir.death(diseased, infected, m)         # Uncomment dependent on exercise
                # susceptible, recovered = sir.re_susceptible(susceptible, recovered, alpha)   # Uncomment dependent on exercise

                susceptible_overtime.append(len(susceptible))
                infected_overtime.append(len(infected))
                recovered_overtime.append(len(recovered))
                diseased_overtime.append(len(diseased))

                timestep += 1
                print(timestep)
                print(f'infected: {len(infected)}')
            R_list.append(len(recovered))
    death_list.append(len(diseased))


#sir.plot_sir(susceptible_overtime, infected_overtime, recovered_overtime, diseased_overtime, gamma[0], move_prob, Beta[0], alpha, mu)
#sir.plot_R_beta(R_list, Beta, gamma)


# Plot final deaths as a function of mortality rate
plt.plot(mu, death_list, "o", color="blue", markersize=4)
plt.legend(
    [f"{gamma_unicode}={gamma}"])
plt.xlabel(f'{mu_unicode}')
plt.title(f"Final number of dead agents as a function of the mortality rate {mu_unicode}")
plt.show()
