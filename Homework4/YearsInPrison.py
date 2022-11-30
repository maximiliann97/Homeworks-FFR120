import numpy as np


def years(n, m, N, R, S, P):
    T = 0
    years_in_prison = [0, 0]
    player_A = [0]*n + [1]*(N-n)
    player_B = [0]*m + [1]*(N-m)

    for i in range(N):
        if player_A[i] == 0 and player_B[i] == 0:
            continue
        elif player_A[i] == 0 and player_B[i] == 1:
            player_A = np.where(player_A == 0, player_A, 1)
        elif player_A[i] == 1 and player_B[i] == 0:
            player_B = np.where(player_B == 0, player_B, 1)
        else:
            continue

    for i in range(N):
        if player_A[i] == 0 and player_B[i] == 0:
            years_in_prison[0] = years_in_prison[0] + R
            years_in_prison[1] = years_in_prison[1] + R
        if player_A[i] == 0 and player_B[i] == 1:
            years_in_prison[0] = years_in_prison[0] + S
            years_in_prison[1] = years_in_prison[1] + T
        if player_A[i] == 1 and player_B[i] == 0:
            years_in_prison[0] = years_in_prison[0] + T
            years_in_prison[1] = years_in_prison[1] + S
        if player_A[i] == 1 and player_B[i] == 1:
            years_in_prison[0] = years_in_prison[0] + P
            years_in_prison[1] = years_in_prison[1] + P
    return years_in_prison


m = 3
n = 5
N = 10
R = 0.5
S = 1.5
P = 1
print(years(n, m, N, R, S, P))