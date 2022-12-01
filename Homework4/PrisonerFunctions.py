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
    lattice = np.zeros([L, L])
    if nDefectors == 1:
        lattice[L//2, L//2] = 1
    return lattice


def competition(lattice, N, R, S, P):

    for i in lattice:
        for j in lattice:
            if 0 < j < len(lattice):
                right = years(lattice[i, j+1], lattice[i, j], N, R, S, P)
                left = years(lattice[i, j-1], lattice[i, j], N, R, S, P)
            elif j == 0:
                left = inf
            else:
                right = inf

            if 0 < i < len(lattice):
                up = years(lattice[i+1, j], lattice[i, j], N, R, S, P)
                down = years(lattice[i-1, j], lattice[i, j], N, R, S, P)
            elif i == 0:
                down = inf
            else:
                up = inf

            if right < lattice[i, j]:
                lattice[i, j] = 1
            if left < lattice[i, j]:
                lattice[i, j] = 1
            if up < lattice[i, j]:
                lattice[i, j] = 1
            if down < lattice[i, j]:
                lattice[i, j] = 1

    return lattice