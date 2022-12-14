import PrisonerFunctions as fun
import matplotlib.pyplot as plt
import numpy as np
from tqdm import trange
from statistics import variance

"""
Number of defectors: 1, 2, 3, 4
Also there is L*L-1 for 1 cooperator + only defectors
L*L-9 = Cluster of cooperators
5050 = About 50 50 cooperators and defectors randomly initialized
"Any": Allows any strategy to be initialized over the grid
"""

# Parameters
N = 7
R = 0.07125
S = 1.25
P = 1
L = 30
mu = 0.01

nDefec = "Any"
timesteps = 500

# Initialization
lattice = fun.initialize_strategies(L, nDefec, N)
strat_mat = np.zeros([N+1, timesteps])

for t in trange(timesteps):
    comp_lattice = fun.competition(lattice, N, R, S, P)
    updated_lattice = fun.revision(comp_lattice, lattice)
    lattice_copy = np.copy(updated_lattice)
    lattice = fun.mutation_2(lattice_copy, mu, N)

    for n in range(N+1):
        occurrence = np.count_nonzero(lattice == n)
        strat_mat[n, t] = occurrence

for n in range(N + 1):
    s_omitted = strat_mat[n, :][100:timesteps]
    print(f'n={n}, R={S}, S={S}, var={variance(s_omitted)}')



# Plots
time = np.linspace(0, timesteps+1, timesteps)
plt.subplot(1, 2, 1)
jet = plt.get_cmap('jet_r')
jet_8_colors = jet(np.linspace(0, 1, 8))

for i in range(N+1):
    plt.plot(time, strat_mat[i, :], color=jet_8_colors[i])
plt.ylabel('Population fraction')
plt.xlabel('Time')


strategies = range(0, 8)
nColours = 8
plt.subplot(1, 2, 2)
cmap = plt.get_cmap('jet_r')
im = plt.imshow(lattice, cmap=cmap, aspect='equal', origin='lower')
plt.axis('off')
fun.colorbar_index(nColours, cmap=cmap)
plt.ylabel(f't={timesteps}')
plt.title(f'R = {R}')
plt.show()


