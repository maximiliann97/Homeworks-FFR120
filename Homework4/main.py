import PrisonerFunctions as fun
import matplotlib.pyplot as plt
import numpy as np
from tqdm import trange

"""
Number of defectors: 1, 2, 3, 4
Also there is L*L-1 for 1 cooperator + only defectors
L*L-9 = Cluster of cooperators
5050 = About 50 50 cooperators and defectors randomly initialized
"""

# Parameters
N = 7
R = 0.85
S = 1.5
P = 1
L = 7
mu = 0.01

nDefec = L*L-9
timesteps = 20

lattice = fun.initialize_strategies(L, nDefec, N)
plt.imshow(lattice, cmap='RdYlBu')

for t in trange(timesteps):
    comp_lattice = fun.competition(lattice, N, R, S, P)
    updated_lattice = fun.revision(comp_lattice, lattice)
    lattice = updated_lattice
    # lattice = fun.mutation(lattice, mu, N)

plt.imshow(lattice, cmap='RdYlBu')
plt.ylabel(f't={timesteps}')
plt.title(f'{nDefec} initial defectors')
plt.show()
