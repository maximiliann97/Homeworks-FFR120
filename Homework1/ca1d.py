# import libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.animation as manimation; manimation.writers.list()
def create_parent(length: int):
    parent = np.random.randint(2, size=length)
    return parent


def update(rule_set, left, center, right):
    if left == 1 and center == 1 and right == 1:
        new_cell = rule_set[0]
    elif left == 1 and center == 1 and right == 0:
        new_cell = rule_set[1]
    elif left == 1 and center == 0 and right == 1:
        new_cell = rule_set[2]
    elif left == 1 and center == 0 and right == 0:
        new_cell = rule_set[3]
    elif left == 0 and center == 1 and right == 1:
        new_cell = rule_set[4]
    elif left == 0 and center == 1 and right == 0:
        new_cell = rule_set[5]
    elif left == 0 and center == 0 and right == 1:
        new_cell = rule_set[6]
    elif left == 0 and center == 0 and right == 0:
        new_cell = rule_set[7]

    return new_cell


def next_generation(cellular_automaton, rule):
    rule_set = np.binary_repr(rule, width=8)
    next_gen = np.zeros(len(cellular_automaton))
    for i in range(len(cellular_automaton)):
        left_neighbour = cellular_automaton[i-1]
        center = cellular_automaton[i]
        if i < len(cellular_automaton) - 1:
            right_neighbour = cellular_automaton[i+1]
        else:
            right_neighbour = cellular_automaton[0]

        next_gen[i] = update(rule_set, left_neighbour, center, right_neighbour)

    return next_gen


def run_ca1d(parent_length, rule, number_of_generations):
    generation_matrix = np.zeros([number_of_generations+1, parent_length])
    parent = create_parent(parent_length)
    generation_matrix[0, :] = parent
    next_gen = parent
    for j in range(number_of_generations):
        next_gen = next_generation(next_gen, rule)
        generation_matrix[j+1, :] = next_gen

    return generation_matrix



rule = 90  # select the update rule
parent_length = 100  # number of cells in one row
generations = 63  # number of time steps
x = run_ca1d(parent_length, rule, generations)


fig = plt.figure(figsize=(10, 10))

ax = plt.axes()
ax.set_axis_off()

ax.imshow(x, interpolation='none',cmap='RdPu')
plt.savefig('cellular_automaton.png', dpi=300, bbox_inches='tight')

steps_to_show = 100  # number of steps to show in the animation window
iterations_per_frame = 1  # how many steps to show per frame
frames = int(generations // iterations_per_frame)  # number of frames in the animation
interval = 50  # interval in ms between consecutive frames

fig = plt.figure(figsize=(10, 10))

ax = plt.axes()
ax.set_axis_off()


def animate(i):
    ax.clear()  # clear the plot
    ax.set_axis_off()  # disable axis

    Y = np.zeros((steps_to_show, parent_length), dtype=np.int8)  # initialize with all zeros
    upper_boundary = (i + 1) * iterations_per_frame  # window upper boundary
    lower_boundary = 0 if upper_boundary <= steps_to_show else upper_boundary - steps_to_show  # window lower bound.
    for t in range(lower_boundary, upper_boundary):  # assign the values
        Y[t - lower_boundary, :] = x[t, :]

    img = ax.imshow(Y, interpolation='none', cmap='RdPu')
    plt.gcf().text(0.15, 0.1, 'by Maximilian Salén', fontsize=18, fontfamily='Verdana')
    return [img]


# call the animator
anim = animation.FuncAnimation(fig, animate, frames=frames, interval=50, blit=True)
anim.save('elementary_cellular_automaton.gif', writer='imagemagick')