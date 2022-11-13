import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from GameOfLife import get_alive_neighbours


def initialize_board(nRows, nCols, p):
    state = np.zeros([nRows, nCols])
    for i in range(nRows):
        for j in range(nCols):
            random_number = np.random.rand()
            if random_number < p:
                state[i, j] = 1
    return state


def update_vote(vote, number_of_neighbours_voting):
    if number_of_neighbours_voting < 4:
        vote = 0
    elif number_of_neighbours_voting > 4:
        vote = 1
    return vote


def update_board_state(state, condition):
    temp_state = np.zeros((len(state), len(state)))
    for i in range(len(state)):
        for j in range(len(state)):
            cell = state[i][j]
            number_of_neighbours_voting = get_alive_neighbours(state, i, j, condition)
            temp_cell = update_vote(cell, number_of_neighbours_voting)
            temp_state[i][j] = temp_cell
    return temp_state


p = 0.6
nRows = 100
nCols = 100
state = initialize_board(nRows, nCols, p)
condition = False


def animate(frame):
    global state
    global condition

    if frame > 0:
        state = update_board_state(state, condition)
    plt.title(f"Majority rule p={p} generation {frame}")
    plt.pcolormesh(state, edgecolors='k', linewidth=0.5)

    ax = plt.gca()
    ax.set_aspect('equal')


fig = plt.figure()
anim = animation.FuncAnimation(fig, animate, frames=30, interval=10)
anim.save(f'Majority p={p}.gif', writer='imagemagick', fps=1.5)