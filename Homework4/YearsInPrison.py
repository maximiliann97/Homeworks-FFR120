import numpy as np


def years(n, m, N, R, S, P):
    T = 0
    years_in_prison = np.zeros([N, 2])
    player_A = [0]*n + [1]*(N-n)
    player_B = [0]*m + [1]*(N-m)

    for i in range(N):
        



    for i in range(N):
        if player_A[i] == 0 and player_B[i] == 0:
            years_in_prison[i, 1] = years_in_prison[i, 1] + R
            years_in_prison[i, 2] = years_in_prison[i, 2] + R
        if player_A[i] == 0 and player_B[i] == 1:
            years_in_prison[i, 1] = years_in_prison[i, 1] + S
            years_in_prison[i, 2] = years_in_prison[i, 2] + T
        if player_A[i] == 1 and player_B[i] == 0:
            years_in_prison[i, 1] = years_in_prison[i, 1] + T
            years_in_prison[i, 2] = years_in_prison[i, 2] + S
        if player_A[i] == 1 and player_B[i] == 1:
            years_in_prison[i, 1] = years_in_prison[i, 1] + P
            years_in_prison[i, 2] = years_in_prison[i, 2] + P
    return years_in_prison
