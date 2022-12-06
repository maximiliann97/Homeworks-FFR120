import PrisonerFunctions as fun
import matplotlib.pyplot as plt
import numpy as np
from statistics import variance
from tqdm import tqdm
from tqdm import trange

"""
Number of defectors: 1, 2, 3, 4
Also there is L*L-1 for 1 cooperator + only defectors
L*L-9 = Cluster of cooperators
5050 = About 50 50 cooperators and defectors randomly initialized
"Any": Allows any strategy to be initialized over the grid
"""

# Parameters
N = 7
R = np.linspace(0.01, 0.99, 33)
S = np.linspace(1, 3, 33)
# R = [0.35, 0.5, 0.6, 0.7, 0.8, 0.9]
# S = [1.5, 2]
P = 1
L = 30
mu = 0.01

nDefec = "Any"
timesteps = 500

# Initialization
lattice = fun.initialize_strategies(L, nDefec, N)

strat_mat = np.zeros([N+1, timesteps])
omitted_steps = np.zeros([8, 400])
big_data = np.zeros([N+1, len(S), len(R)])

for i, s in enumerate(tqdm(S)):
    for j, r in enumerate(tqdm(R)):
        for t in range(timesteps):
            comp_lattice = fun.competition(lattice, N, r, s, P)
            updated_lattice = fun.revision(comp_lattice, lattice)
            lattice_copy = np.copy(updated_lattice)
            lattice = fun.mutation_2(lattice_copy, mu, N)

            for n in range(N+1):
                occurrence = np.count_nonzero(lattice == n)
                strat_mat[n, t] = occurrence
        for n in range(N+1):
            s_omitted = strat_mat[n, :][100:timesteps]
            big_data[n, i, j] = variance(s_omitted)


x_min = np.min(R)
x_max = np.max(R)
y_min = np.min(S)
y_max = np.max(S)


for i in range(N+1):
    strat = np.flip(big_data[i, :, :], 0)
    plt.subplot(2, 4, i+1)
    plt.imshow(strat, cmap='jet', extent=[x_min, x_max, y_min, y_max])
    plt.xlabel('R')
    plt.ylabel('S')
    plt.title(f'sigma_{i}')
    plt.colorbar()
plt.show()

