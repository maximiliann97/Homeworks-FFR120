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
# S = np.linspace(1, 3, 50)
S = [1, 1.5]
R = [0.5, 0.7, 0.9]
P = 1
L = 30
mu = 0.01

nDefec = "Any"
timesteps = 500

# Initialization
rows = len(R)*len(S)
iRow = 0
lattice = fun.initialize_strategies(L, nDefec, N)
strat_mat = np.zeros([N+1, timesteps])
omitted_steps = np.zeros([8, 400])
# var_mat_0 = np.zeros([len(S), len(R)])
# var_mat_1 = np.zeros([len(S), len(R)])
# var_mat_2 = np.zeros([len(S), len(R)])
# var_mat_3 = np.zeros([len(S), len(R)])
# var_mat_4 = np.zeros([len(S), len(R)])
# var_mat_5 = np.zeros([len(S), len(R)])
# var_mat_6 = np.zeros([len(S), len(R)])
# var_mat_7 = np.zeros([len(S), len(R)])

big_data = np.zeros([N+1, len(S), len(R)])

for i, s in enumerate(tqdm(S)):
    for j, r in enumerate(tqdm(R)):
        for t in range(timesteps):
            comp_lattice = fun.competition(lattice, N, r, s, P)
            updated_lattice = fun.revision(comp_lattice, lattice)
            lattice = np.copy(updated_lattice)
            lattice = fun.mutation(lattice, mu, N)

            for n in range(N+1):
                occurrence = np.count_nonzero(lattice == n)
                strat_mat[n, t] = occurrence
        for strategy, _ in enumerate(strat_mat):
            omitted_steps[strategy, :] = strat_mat[strategy, :][100:len(strat_mat[0, :])]
            s_omitted = strat_mat[strategy, :][100:len(strat_mat[0, :])]
            big_data[strategy, i, j] = variance(s_omitted)


#             if strategy == 0:
#                 var_mat_0[i, j] = variance(s_omitted)
#             elif strategy == 1:
#                 var_mat_1[i, j] = variance(s_omitted)
#             elif strategy == 2:
#                 var_mat_2[i, j] = variance(s_omitted)
#             elif strategy == 3:
#                 var_mat_3[i, j] = variance(s_omitted)
#             elif strategy == 4:
#                 var_mat_4[i, j] = variance(s_omitted)
#             elif strategy == 5:
#                 var_mat_5[i, j] = variance(s_omitted)
#             elif strategy == 6:
#                 var_mat_6[i, j] = variance(s_omitted)
#             else:
#                 var_mat_7[i, j] = variance(s_omitted)
#
# var_strat_list = [var_mat_0, var_mat_1, var_mat_2, var_mat_3, var_mat_4, var_mat_5, var_mat_6, var_mat_7]


x_min = R[0]
x_max = R[len(R)-1]
y_min = S[0]
y_max = S[len(S)-1]

for i in range(N+1):
    strat = np.flip(big_data[i, :, :], 0)
    plt.subplot(2, 4, i+1)
    plt.imshow(strat, cmap='jet', extent=[x_min, x_max, y_min, y_max])
    plt.xlabel('R')
    plt.ylabel('S')
    plt.title(f'sigma_{i}')
    plt.colorbar()
plt.show()

