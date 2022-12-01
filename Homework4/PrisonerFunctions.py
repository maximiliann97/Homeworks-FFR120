import numpy as np
from math import inf


def years(n, m, N, R, S, P):
    T = 0
    years_in_prison = 0

    if n == 0:
        player_A = [1]*N

    else:
        player_A = [0]*n + [1]*(N-n)

    if m == 0:
        player_B = [1]*N

    else:
        player_B = [0]*m + [1]*(N-m)

    for i in range(N):
        if player_A[i] == 0 and player_B[i] == 0:
            years_in_prison = years_in_prison + R

        if player_A[i] == 0 and player_B[i] == 1:
            years_in_prison = years_in_prison + S
            player_A = [0]*(i+1) + [1]*(N-i+1)

        if player_A[i] == 1 and player_B[i] == 0:
            years_in_prison = years_in_prison + T
            player_B = [0]*(i+1) + [1]*(N-i+1)

        if player_A[i] == 1 and player_B[i] == 1:
            years_in_prison = years_in_prison + P

    return years_in_prison


def initialize_strategies(L, nDefectors):
    lattice = np.zeros([L, L]).astype(int)
    if nDefectors == 1:
        lattice[L//2, L//2] = 1
    return lattice


def competition(lattice, N, R, S, P):
    L = len(lattice)
    comp_lattice = np.zeros([L, L])
    for i in range(L):
        for j in range(L):
            if j - 1 == -1:
                left = years(lattice[i, j], lattice[i, j], N, R, S , P)
            else:
                left = years(lattice[i, j-1], lattice[i, j], N, R, S, P)

            if j + 2 == L + 1:
                right = years(lattice[i, j], lattice[i, j], N, R, S, P)
            else:
                right = years(lattice[i, j+1], lattice[i, j], N, R, S, P)

            if i + 2 == L + 1:
                down = years(lattice[i, j], lattice[i, j], N, R, S, P)
            else:
                down = years(lattice[i+1, j], lattice[i, j], N, R, S, P)

            if i - 1 == -1:
                up = years(lattice[i, j], lattice[i, j], N, R, S, P)
            else:
                up = years(lattice[i-1, j], lattice[i, j], N, R, S, P)
            comp_lattice[i, j] = left + right + down + up

    return comp_lattice


def revision(comp_lattice, lattice):
    L = len(comp_lattice)

    for i in range(L):
        for j in range(L):
            if j - 1 == -1:
                left = inf
            else:
                left = comp_lattice[i, j-1]

            if i + 2 == L + 1:
                right = inf
            else:
                right = comp_lattice[i+1, j]

            if i + 2 == L + 1:
                down = inf
            else:
                down = comp_lattice[i, j+1]

            if i - 1 == -1:
                up = inf
            else:
                up = comp_lattice[i, j-1]

            if comp_lattice[i, j] < left:
                
