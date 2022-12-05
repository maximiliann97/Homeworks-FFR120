import PrisonerFunctions as fun
import matplotlib.pyplot as plt
import numpy as np
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
R = 0.9
S = 1.5
P = 1
L = 30
mu = 0.01

nDefec = "Any"
timesteps = 200

# Initialization
lattice = fun.initialize_strategies(L, nDefec, N)
strat_mat = np.zeros([N+1, timesteps])

for t in trange(timesteps):
    comp_lattice = fun.competition(lattice, N, R, S, P)
    updated_lattice = fun.revision(comp_lattice, lattice)
    lattice = np.copy(updated_lattice)
    lattice = fun.mutation(lattice, mu, N)

    for n in range(N+1):
        occurrence = np.count_nonzero(lattice == n) / (L*L)
        strat_mat[n, t] = occurrence


# Plots
plt.subplot(1, 2, 2)
plt.imshow(lattice, cmap='Set1', aspect='equal')
plt.colorbar()
plt.ylabel(f't={timesteps}')
plt.title(f'R = {R}')


time = np.linspace(0, timesteps+1, timesteps)
plt.subplot(1, 2, 1)
colours = ['tab:red', 'tab:blue', 'tab:green', 'tab:purple', 'yellow', 'tab:brown', 'tab:pink', 'tab:grey']

for i in range(N+1):
    plt.plot(time, strat_mat[i, :], colours[i])

plt.ylabel('Population fraction')
plt.xlabel('Time')
plt.show()


