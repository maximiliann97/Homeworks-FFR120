import PrisonerFunctions as fun
import matplotlib.pyplot as plt
import numpy as np


# Parameters
N = 7
R = 0.5
S = 1.5
P = 1
L = 10
nDefec = 1


lattice = fun.initialize_strategies(L, nDefec)
comp_lattice = fun.competition(lattice, N, R, S, P)

print(comp_lattice)