import PrisonerFunctions as fun
import matplotlib.pyplot as plt
import numpy as np
from tqdm import trange

# Parameters
N = 7
R = 0.9
S = 1.5
P = 1
L = 31
nDefec = 4
timesteps = 20

lattice = fun.initialize_strategies(L, nDefec, N)

for t in trange(timesteps):
    comp_lattice = fun.competition(lattice, N, R, S, P)
    updated_lattice = fun.revision(comp_lattice, lattice)
    lattice = updated_lattice


plt.imshow(lattice, cmap='RdYlBu')
plt.ylabel(f't={timesteps}')
plt.title(f'{nDefec} initial defectors')
plt.show()