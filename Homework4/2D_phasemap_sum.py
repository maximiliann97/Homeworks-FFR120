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
# R = np.linspace(0.01, 0.99, 33)
# S = np.linspace(1, 3, 33)
R = [0.3, 0.5, 0.8]
S = [1, 2, 3]
P = 1
L = 30
mu = 0.01
nDefec = "Any"
timesteps = 500
threshold = 10000

# Initialization
lattice = fun.initialize_strategies(L, nDefec, N)

strat_mat = np.zeros([N+1, timesteps])
omitted_steps = np.zeros([8, 400])
var_sum = 0
var_sum_mat = np.zeros([len(S), len(R)])

for i, s in enumerate(tqdm(S)):
    for j, r in enumerate(tqdm(R)):
        for t in range(timesteps):
            comp_lattice = fun.competition(lattice, N, r, s, P)
            updated_lattice = fun.revision(comp_lattice, lattice)
            lattice = np.copy(updated_lattice)
            lattice = fun.mutation_2(lattice, mu, N)

            for n in range(N+1):
                occurrence = np.count_nonzero(lattice == n)
                strat_mat[n, t] = occurrence
        for strategy, _ in enumerate(strat_mat):
            omitted_steps[strategy, :] = strat_mat[strategy, :][100:len(strat_mat[0, :])]
            s_omitted = strat_mat[strategy, :][100:len(strat_mat[0, :])]
            var_sum += variance(s_omitted)
        if var_sum > threshold:
            var_sum_mat[i, j] = 1
        var_sum = 0


x_min = np.min(R)
x_max = np.max(R)
y_min = np.min(S)
y_max = np.max(S)

var_sum_mat = np.flip(var_sum_mat, 0)
plt.imshow(var_sum_mat, cmap='Greys', extent=[x_min, x_max, y_min, y_max])
plt.xlabel('R')
plt.ylabel('S')
plt.colorbar()
plt.title(rf'$\sum_n\sigma^2_n > {threshold}$ ')
plt.show()
