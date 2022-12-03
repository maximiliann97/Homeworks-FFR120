import PrisonerFunctions as fun
import matplotlib.pyplot as plt
import numpy as np
from tqdm import trange

# Parameters
N = 7
R = 0.85
S = 1.5
P = 1
L = 5
mu = 0.01
nDefec = 2
timesteps = 1

lattice = fun.initialize_strategies(L, nDefec, N)
plt.imshow(lattice, cmap='RdYlBu')

for t in trange(timesteps):
    comp_lattice = fun.competition(lattice, N, R, S, P)
    updated_lattice = fun.revision(comp_lattice, lattice)
    lattice = updated_lattice
    # lattice = fun.mutation(lattice, mu, N)


#plt.imshow(lattice, cmap='RdYlBu')
plt.ylabel(f't={timesteps}')
plt.title(f'{nDefec} initial defectors')
plt.show()
