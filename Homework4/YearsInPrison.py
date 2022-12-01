
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
