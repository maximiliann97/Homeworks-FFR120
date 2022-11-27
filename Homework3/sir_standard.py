import matplotlib.pyplot as plt
import SIR as sir

# Parameters
lattice = 100
nAgents = 1000
infection_rate = 0.01   # Initial infection_rate
move_prob = 0.8
beta = 0.25            # Infection probability
gamma = 0.01         # Recover probability
alpha = None          # Re-susceptible probability
mu = None             # Mortality probability

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
susceptible, infected = sir.initialize_world(lattice, nAgents, infection_rate)
recovered = []
diseased = []
infected_population = []


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

sir.plot_sir(susceptible_overtime, infected_overtime, recovered_overtime, diseased_overtime, gamma, move_prob, beta, mu, alpha)
plt.show()