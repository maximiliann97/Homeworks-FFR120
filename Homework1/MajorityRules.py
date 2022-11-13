import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


def initialize_board(nRows, nCols, p):
    state = np.zeros([nRows, nCols])
    for i in range(nRows):
        for j in range(nCols):
            random_number = np.random.rand()
            if random_number < p:
                state[i, j] = 1
    return state


