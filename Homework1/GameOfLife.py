import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def birth_random_config(nRows,nCols):
    state = np.random.choice([0, 1], (nRows, nCols))
    return state


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


def update_cell(cell, number_of_alive_neighbours):
    if cell == 1:
        if number_of_alive_neighbours != 2 and number_of_alive_neighbours != 3:
            cell = 0

    elif cell == 0:
        if number_of_alive_neighbours == 3:
            cell = 1

    return cell


def update_state(state):
    temp_state = np.zeros((len(state), len(state)))
    for i in range(len(state)):
        for j in range(len(state)):
            cell = state[i][j]
            number_of_alive_neighbours = get_alive_neighbours(state, i, j, condition=True)
            temp_cell = update_cell(cell, number_of_alive_neighbours)
            temp_state[i][j] = temp_cell
    return temp_state



# def main():
#     nGenerations = 2
#     nRows = 5
#     nCols = 5
#     condition = True
#     state = birth_random_config(nRows, nCols)
#     state_list = [state]
#
#     for i in range(nGenerations):
#         updated_state = update_state(condition, state)
#         state = updated_state
#         state_list.append(state)
#
# main()
state = birth_random_config(10, 10)

def animate(frame):
    global state
    state = update_state(state)
    plt.title(f"10x10 Random config, generation {frame+1}")
    plt.imshow(state)

fig = plt.figure()
anim = animation.FuncAnimation(fig, animate, frames=20, interval=10)
anim.save('10x10 Random config PBC.gif', writer='imagemagick', fps=0.2)

