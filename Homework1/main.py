import GameOfLife as game
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from initStates import birth_random_config, still_life, oscillator, glider, special_oscillator
from QuestForNewGliders import initialize_grid

# Inits
state = special_oscillator(20,20)
condition = True
mod = False


def animate(frame):
    global state
    global condition
    global mod

    if frame > 0:
        state = game.update_state(state, condition, mod)
    plt.title(f"New oscillator, generation {frame}")
    plt.pcolormesh(state, edgecolors='k', linewidth=0.5)

    ax = plt.gca()
    ax.set_aspect('equal')


fig = plt.figure()
anim = animation.FuncAnimation(fig, animate, frames=30, interval=10)
anim.save('New oscillator.gif', writer='imagemagick', fps=1.5)


