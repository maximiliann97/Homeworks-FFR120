import matplotlib.pyplot as plt
import SIR as sir

# Parameters
lattice = 100
nAgents = 1000
infection_rate = 0.01
move_prob = 0.8
Beta = [0.6]
gamma = 0.01
mu = 0.05

# Initialization
infected_overtime = []
recovered_overtime = []
susceptible_overtime = []
diseased_overtime = []
R_list = []
timestep = 0
recovered = []
diseased = []
susceptible, infected = sir.initialize_world(lattice, nAgents, infection_rate)

for beta in Beta:
    while len(infected) > 0:
        sir.walk(susceptible, move_prob, lattice)
        sir.walk(infected, move_prob, lattice)
        sir.walk(recovered, move_prob, lattice)
        infected, susceptible = sir.check_infected(infected, susceptible, beta)
        recovered, infected = sir.recovery(infected, recovered, gamma)
        diseased, infected = sir.death(diseased, infected, mu)

        susceptible_overtime.append(len(susceptible))
        infected_overtime.append(len(infected))
        recovered_overtime.append(len(recovered))
        diseased_overtime.append(len(diseased))

        timestep += 1
        print(timestep)
        print(f'infected: {len(infected)}')
    R_list.append(len(recovered)/len(susceptible))

sir.plot_sir(susceptible_overtime, infected_overtime, recovered_overtime, diseased_overtime, timestep)
plt.show()
