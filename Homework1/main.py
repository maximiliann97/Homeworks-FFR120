import GameOfLife as game
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from initStates import birth_random_config, still_life, oscillator, glider
from QuestForNewGliders import initialize_grid


state = initialize_grid(10)

def animate(frame):
    global state
    if frame > 0:
        state = game.update_state(state, condition=True)
    plt.title(f"10x10 random config in 30x30, generation {frame}")
    plt.pcolormesh(state, edgecolors='k', linewidth=1.5)

    ax = plt.gca()
    ax.set_aspect('equal')


fig = plt.figure()
anim = animation.FuncAnimation(fig, animate, frames=101, interval=10)
anim.save('10x10 Random config in center PBC.gif', writer='imagemagick', fps=1.5)


