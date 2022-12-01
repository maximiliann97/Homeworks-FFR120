import PrisonerFunctions as fun
import matplotlib.pyplot as plt
import numpy as np


# Parameters
N = 7
R = 0.9
S = 1.5
P = 1
L = 30
nDefec = 1
timesteps = 20

init_lattice = fun.initialize_strategies(L, nDefec, N)
updated_lattice = init_lattice

for t in range(timesteps):
    comp_lattice = fun.competition(updated_lattice, N, R, S, P)
    updated_lattice = fun.revision(comp_lattice, updated_lattice)


plt.imshow(updated_lattice, cmap='RdYlBu')
plt.axis('off')
plt.ylabel(f't={timesteps}')
plt.title(f'{nDefec} initial defectors')
plt.show()