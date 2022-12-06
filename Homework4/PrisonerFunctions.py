import numpy as np


def years(m, n, N, R, S, P):
    T = 0
    years_in_prison = 0

    if m == 0:
        player_A = [0]*N
    else:
        player_A = [1]*m + [0]*(N-m)

    if n == 0:
        player_B = [0]*N
    else:
        player_B = [1]*n + [0]*(N-n)

    for i in range(N):
        if player_A[i] == 1 and player_B[i] == 1:   # Both cooperates
            years_in_prison = years_in_prison + R

        if player_A[i] == 0 and player_B[i] == 1:   # A defects, B cooperates
            years_in_prison = years_in_prison + T
            player_B = [1]*(i+1) + [0]*(N-i+1)

        if player_A[i] == 1 and player_B[i] == 0:   # A cooperates, B defects
            years_in_prison = years_in_prison + S
            player_A = [1]*(i+1) + [0]*(N-i+1)

        if player_A[i] == 0 and player_B[i] == 0:   # Both defects
            years_in_prison = years_in_prison + P

    return years_in_prison


def initialize_strategies(L, nDefectors, N):
    lattice = N * np.ones([L, L]).astype(int)

    if nDefectors == 1:
        lattice[L//2, L//2] = 0

    if nDefectors == 2:
        lattice[L // 3, 2*L // 3] = 0
        lattice[2*L // 3, L // 3] = 0

    if nDefectors == 3:
        lattice[L//2, L//2] = 0
        lattice[L // 4, 3*L // 4] = 0
        lattice[3*L // 4, L // 4] = 0

    if nDefectors == 4:
        lattice[L//5, 4*L//5] = 0
        lattice[2*L//5, 3*L//5] = 0
        lattice[3*L//5, 2*L//5] = 0
        lattice[4*L//5, L//5] = 0

    if nDefectors == L*L-1:
        lattice = np.zeros([L, L]).astype(int)
        lattice[L // 2, L // 2] = 1

    if nDefectors == L*L-9:
        lattice = np.zeros([L, L]).astype(int)
        lattice[(L // 2) - 1, (L // 2) - 1] = N
        lattice[(L // 2) - 1, (L // 2)] = N
        lattice[(L // 2) - 1, (L // 2) + 1] = N
        lattice[L // 2, L // 2 - 1] = N
        lattice[L // 2, L // 2] = N
        lattice[L // 2, L // 2 + 1] = N
        lattice[L // 2 + 1, L // 2 - 1] = N
        lattice[L // 2 + 1, L // 2] = N
        lattice[L // 2 + 1, L // 2 + 1] = N

    if nDefectors == 5050:
        lattice = np.zeros([L, L]).astype(int)
        for i in range(L):
            for j in range(L):
                if np.random.rand() < 0.5:
                    lattice[i, j] = N

    if nDefectors == "Any":
        lattice = np.zeros([L, L]).astype(int)
        for i in range(L):
            for j in range(L):
                lattice[i, j] = np.random.randint(N+1)

    return lattice


def competition(lattice, N, R, S, P):
    L = len(lattice)
    comp_lattice = np.zeros([L, L])
    for i in range(L):
        for j in range(L):
            if j - 1 == -1:
                left = years(lattice[i, j], lattice[i, L-1], N, R, S, P)
            else:
                left = years(lattice[i, j], lattice[i, j-1], N, R, S, P)

            if j + 2 == L + 1:
                right = years(lattice[i, j], lattice[i, 0], N, R, S, P)
            else:
                right = years(lattice[i, j], lattice[i, j+1], N, R, S, P)

            if i + 2 == L + 1:
                down = years(lattice[i, j], lattice[0, j], N, R, S, P)
            else:
                down = years(lattice[i, j], lattice[i+1, j], N, R, S, P)

            if i - 1 == -1:
                up = years(lattice[i, j], lattice[L-1, j], N, R, S, P)
            else:
                up = years(lattice[i, j], lattice[i-1, j], N, R, S, P)

            comp_lattice[i, j] = left + right + down + up

    return comp_lattice


def revision(comp_lattice, lattice):
    L = len(lattice)
    updated_lattice = np.copy(lattice)
    for i in range(L):
        for j in range(L):
            if j == 0:
                left = comp_lattice[i, L-1]
            else:
                left = comp_lattice[i, j-1]

            if j + 1 == L:
                right = comp_lattice[i, 0]
            else:
                right = comp_lattice[i, j+1]

            if i + 1 == L:
                down = comp_lattice[0, j]
            else:
                down = comp_lattice[i+1, j]

            if i == 0:
                up = comp_lattice[L-1, j]
            else:
                up = comp_lattice[i-1, j]

            self = comp_lattice[i, j]
            neighbours = np.array([self, left, right, down, up])
            index = np.argmin(neighbours)

            # indices = np.where(neighbours == neighbours.min())
            # indices = indices[0]
            """
            # if indices[0] == 0 and len(indices) != 5:
            #     indices = indices[1:len(indices)]
            #
            # if len(indices) == 2 or len(indices) == 3 or len(indices) == 4:
            """
            #
            # k = np.random.randint(0, len(indices))
            # index = indices[k]

            if index == 1:
                if j - 1 == -1:
                    updated_lattice[i, j] = lattice[i, L-1]
                else:
                    updated_lattice[i, j] = lattice[i, j-1]

            elif index == 2:
                if j + 2 == L + 1:
                    updated_lattice[i, j] = lattice[i, 0]
                else:
                    updated_lattice[i, j] = lattice[i, j+1]

            elif index == 3:
                if i + 2 == L + 1:
                    updated_lattice[i, j] = lattice[0, j]
                else:
                    updated_lattice[i, j] = lattice[i+1, j]

            elif index == 4:
                if i - 1 == -1:
                    updated_lattice[i, j] = lattice[L-1, j]
                else:
                    updated_lattice[i, j] = lattice[i-1, j]
            else:
                updated_lattice[i, j] = lattice[i, j]
    return updated_lattice


def mutation(lattice, mu, N):
    L = len(lattice)
    for i in range(L):
        for j in range(L):
            r = np.random.rand()
            if r < mu:
                if np.random.rand() < 0.5:
                    lattice[i, j] = 0
                else:
                    lattice[i, j] = N
    return lattice


def mutation_2(lattice, mu, N):
    L = len(lattice)
    for i in range(L):
        for j in range(L):
            r = np.random.rand()
            if r < mu:
                if np.random.rand() < 0.5:
                    lattice[i, j] = 0
                else:
                    lattice[i, j] = np.random.randint(N+1)
    return lattice

