import GameOfLife as game
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from initStates import birth_random_config, still_life, oscillator, glider
from QuestForNewGliders import initialize_grid

# Inits
state = initialize_grid(20)
condition = True
mod = True


def animate(frame):
    global state
    global condition
    global mod

    if frame > 0:
        state = game.update_state(state, condition, mod)
    plt.title(f"20x20 6-4-5, generation {frame}")
    plt.pcolormesh(state, edgecolors='k', linewidth=1.5)

    ax = plt.gca()
    ax.set_aspect('equal')


fig = plt.figure()
anim = animation.FuncAnimation(fig, animate, frames=30, interval=10)
anim.save('Modified rules Extinction.gif', writer='imagemagick', fps=1.5)


