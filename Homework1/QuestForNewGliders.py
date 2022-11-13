import numpy as np
from initStates import birth_random_config, still_life, oscillator, glider, special_oscillator
from GameOfLife import update_state


def initialize_grid(N):
    A = birth_random_config(N, N)
    B = np.zeros([3*N, 3*N])

    nb = B.shape[0]
    na = A.shape[0]
    lower = (nb // 2) - (na // 2)
    upper = (nb // 2) + (na // 2)
    B[lower:upper, lower:upper] = A
    return B


def translation(state, s_x, s_y):
    state = np.roll(state, s_y, axis=0)
    state = np.roll(state, s_x, axis=1)
    return state


def check_state_spaceships(state1, state2):
    directions = np.array([
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
        [1, 1],
        [1, -1],
        [-1, 1],
        [-1, -1],
    ])

    for d in directions:
        if np.array_equal(state2, translation(state1, d[0], d[1])):
            print(f'Translated direction{d}')
            return True
    return False


def generations():
    nGenerations = 10000
    N = 10
    mod = False
    condition = True    # PBC
    state = initialize_grid(N) # Initial state  # Initial state
    state_list = [state]

    for i in range(nGenerations):
        updated_state = update_state(state, condition, mod)
        state = updated_state
        state_list.append(state)

    return state_list


state_list = generations()
state1 = state_list[0]
saved_spaceships = []
saved_oscillators = []

for i, _ in enumerate(state_list):
    for j, _ in enumerate(state_list):
        state1 = state_list[i]
        state2 = state_list[j]
        if i != j:
            if np.array_equal(state1, state2):
                saved_oscillators.append(state2)
            if check_state_spaceships(state1, state2):
                print(check_state_spaceships(state1, state2))
                saved_spaceships.append(state2)


