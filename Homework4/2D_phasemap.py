import PrisonerFunctions as fun
import matplotlib.pyplot as plt
import numpy as np
from statistics import variance
from tqdm import tqdm

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
            print(f'n = {n}, S = {s}, R = {r} {variance(s_omitted)}')
            if n != 0:
                if variance(s_omitted) < 15000:
                    big_data[n, i, j] = variance(s_omitted)
                else:
                    big_data[n, i, j] = 15000
            else:
                big_data[n, i, j] = variance(s_omitted)


np.save('big_data_restricted.npy', big_data)
x_min = np.min(R)
x_max = np.max(R)
y_min = np.min(S)
y_max = np.max(S)
extent = [x_min, x_max, y_min, y_max]
aspect = ((x_max-x_min)/len(R)) / ((y_max-y_min)/len(S))


for i in range(N+1):
    strat = np.flip(big_data[i, :, :], 0)
    plt.subplot(2, 4, i+1)
    plt.imshow(strat, cmap='jet', aspect=aspect, extent=extent)
    plt.gca()
    plt.xlabel('R')
    plt.ylabel('S')
    plt.title(rf'$\sigma^2_{i}$')
    plt.colorbar()
plt.show()

