import numpy as np


def birth_random_config(nRows,nCols):
    state = np.random.choice([0, 1], (nRows, nCols))
    return state


def still_life(nRows, nCols, option):
    state = np.zeros([nRows, nCols])

    if option == 1:
        state[3:5, 3:5] = 1
    elif option == 2:
        state[1][2] = 1
        state[4][2] = 1
        state[2][1] = 1
        state[3][1] = 1
        state[2][3] = 1
        state[3][3] = 1
    elif option == 3:
        state[1][2] = 1
        state[2][1] = 1
        state[3][1] = 1
        state[4][2] = 1
        state[4][3] = 1
        state[2][3] = 1
        state[3][4] = 1
    elif option == 4:
        state[2][2] = 1
        state[3][1] = 1
        state[4][2] = 1
        state[4][3] = 1
        state[3][3] = 1
    elif option == 5:
        state[1][3] = 1
        state[2][2] = 1
        state[3][3] = 1
        state[2][4] = 1
    else:
        raise Exception('Input for option should be 1-5')
    return state


def oscillator(nRows, nCols, option):
    state = np.zeros([nRows, nCols])
    if option == 1:
        state[2][3] = 1
        state[3][3] = 1
        state[4][3] = 1
    elif option == 2:
        state[2][2] = 1
        state[2][3] = 1
        state[2][4] = 1
        state[3][3] = 1
        state[3][4] = 1
        state[3][5] = 1

    elif option == 3:
        state[1][1] = 1
        state[1][2] = 1
        state[2][1] = 1
        state[4][3] = 1
        state[4][4] = 1
        state[3][4] = 1
    else:
        raise Exception('Only input option 1-3')
    return state


def glider(nRows, nCols, orientation):
    state = np.zeros([nRows, nCols])
    if orientation == 1:
        state[2][6] = 1
        state[2][7] = 1
        state[2][8] = 1
        state[1][6] = 1
        state[0][7] = 1
    elif orientation == 2:
        state[6][1] = 1
        state[4][0] = 1
        state[4][1] = 1
        state[4][2] = 1
        state[5][2] = 1
    elif orientation == 3:
        state[8][8] = 1
        state[7][7] = 1
        state[6][7] = 1
        state[6][8] = 1
        state[6][9] = 1
    elif orientation == 4:
        state[1][0] = 1
        state[2][1] = 1
        state[2][2] = 1
        state[1][2] = 1
        state[0][2] = 1

    else:
        raise Exception('Must choose an orientation between 1-4')
    return state


def special_oscillator(nRows, nCols):
    state = np.zeros([nRows, nCols])
    state[4][4] = 1
    state[4][5] = 1
    state[4][6] = 1
    state[5][4] = 1
    state[5][5] = 1
    state[5][6] = 1
    state[6][4] = 1
    state[6][5] = 1
    state[6][6] = 1

    state[1][7] = 1
    state[1][8] = 1
    state[1][9] = 1
    state[2][7] = 1
    state[2][8] = 1
    state[2][9] = 1
    state[3][7] = 1
    state[3][8] = 1
    state[3][9] = 1

    return state
