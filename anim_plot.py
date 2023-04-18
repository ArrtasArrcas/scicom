from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np


def plotting(series):
    gen = (i for i in series)

    first = next(gen)
    #print (first)

    fig = plt.figure()
    ax = plt.axes(projection="3d")

    scatter_plot = ax.scatter(first[:, 0], first[:, 1], first[:, 2])

    ani = animation.FuncAnimation(fig, update,
                                  frames=gen,
                                  fargs=(scatter_plot, ax),
                                  repeat=True,
                                  interval=0.05)

    plt.show()


def update(frame, plot_sim, axis):
    plot_sim._offsets3d = frame[:, :3].T