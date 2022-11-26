import matplotlib.pyplot as plt
import SIR as sir

# Parameters
lattice = 100
nAgents = 1000
infection_rate = 0.01
move_prob = 0.8
beta = 0.9
gamma = 0.01

# Initialization
infected_overtime = []
recovered_overtime = []
susceptible_overtime = []
timestep = 0
recovered = []
susceptible, infected = sir.initialize_world(lattice, nAgents, infection_rate)

while len(infected)>0:
    sir.walk(susceptible, move_prob, lattice)
    sir.walk(infected, move_prob, lattice)
    sir.walk(recovered, move_prob, lattice)
    infected, susceptible = sir.check_infected(infected, susceptible, beta)
    recovered, infected = sir.recovery(infected, recovered, gamma)

    susceptible_overtime.append(len(susceptible))
    infected_overtime.append(len(infected))
    recovered_overtime.append(len(recovered))
    timestep += 1
    print(timestep)
    print(f'infected: {len(infected)}')

sir.plot_sir(susceptible_overtime, infected_overtime, recovered_overtime, timestep)
