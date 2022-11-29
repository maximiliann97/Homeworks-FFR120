import matplotlib.pyplot as plt
import SIR as sir
import numpy as np
from datetime import datetime
from tqdm import tqdm

# Parameters
lattice = 100
nAgents = 1000
infection_rate = 0.01               # Initial infection_rate
move_prob = 0.8
Beta = np.linspace(0.1, 1, 10)        # Infection probability
# Gamma = [0.01, 0.02]                # Recover probability
Q = np.linspace(1, 100, 30)
# Initialization
alpha_unicode = "\u03B1"
gamma_unicode = "\u03B3"
beta_unicode = "\u03B2"
mu_unicode = "\u03BC"
infected_overtime = []
recovered_overtime = []
susceptible_overtime = []
diseased_overtime = []

for q in tqdm(Q):
    nrRecovered_list = []
    for beta in tqdm(Beta):
        timestep = 0
        susceptible, infected = sir.initialize_world(lattice, nAgents, infection_rate)
        recovered = []
        diseased = []
        gamma = beta/q
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
        nrRecovered_list.append(len(recovered))
    time_now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    nrRecovered_array = np.array(nrRecovered_list)
    #np.save('arrays/' + time_now + f' R_inf,beta_over_gamma,Q={q}', nrRecovered_array)
    np.savetxt('arrays/' + time_now + f' R_inf,beta_over_gamma,Q={q}.csv', nrRecovered_array, delimiter=",")
