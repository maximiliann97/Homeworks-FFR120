import numpy as np


def get_alive_neighbours(state, i, j, condition=False):
    alive_count = 0
    if not condition:
        padded_state = np.pad(state, [(1, 1), (1, 1)])
    elif condition:
        right_col = state[:, [len(state) - 1]]
        padded_state = np.hstack([right_col, state])

        bot_row = padded_state[len(state) - 1, :]
        padded_state = np.vstack([bot_row, padded_state])

        left_col = padded_state[:, [1]]
        padded_state = np.hstack([padded_state, left_col])

        top_row = padded_state[1, :]
        padded_state = np.vstack([padded_state, top_row])
    else:
        raise Exception("Only true or false for condition")

    if padded_state[i][j] == 1:
        alive_count += 1
    if padded_state[i][j+1] == 1:
        alive_count += 1
    if padded_state[i][j+2] == 1:
        alive_count += 1
    if padded_state[i+1][j] == 1:
        alive_count += 1
    if padded_state[i+1][j+2] == 1:
        alive_count += 1
    if padded_state[i+2][j] == 1:
        alive_count += 1
    if padded_state[i+2][j+1] == 1:
        alive_count += 1
    if padded_state[i+2][j+2] == 1:
        alive_count += 1

    return alive_count


def update_cell(cell, number_of_alive_neighbours, mod):
    if not mod:
        if cell == 1:
            if number_of_alive_neighbours != 2 and number_of_alive_neighbours != 3:
                cell = 0

        elif cell == 0:
            if number_of_alive_neighbours == 3:
                cell = 1

    elif mod:
        if cell == 1:
            if number_of_alive_neighbours > 6 or number_of_alive_neighbours < 4:
                cell = 0

        elif cell == 0:
            if number_of_alive_neighbours == 5:
                cell = 1
    else:
        raise Exception('Mod must be false or true')

    return cell


def update_state(state, condition, mod):
    temp_state = np.zeros((len(state), len(state)))
    for i in range(len(state)):
        for j in range(len(state)):
            cell = state[i][j]
            number_of_alive_neighbours = get_alive_neighbours(state, i, j, condition)
            temp_cell = update_cell(cell, number_of_alive_neighbours, mod)
            temp_state[i][j] = temp_cell
    return temp_state



