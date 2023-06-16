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

    texts = []

    for x, y, z, label in zip(first[:, 0], first[:, 1], first[:, 2], ["sun",
                                                                      "mercury",
                                                                      "venus",
                                                                      "earth",
                                                                      "moon",
                                                                      "mars",
                                                                      "jupiter",
                                                                      "saturn",
                                                                      "uranus",
                                                                      "neptune"]):
        texts.append(ax.text(x, y, z, label))

    ani = animation.FuncAnimation(fig, update,
                                  frames=gen,
                                  fargs=(scatter_plot, texts, ax),
                                  repeat=True,
                                  interval=0.01)

    plt.show()


def update(frame, plot_sim, texts, axis):
    plot_sim._offsets3d = frame[:, :3].T
    for i, text in enumerate(texts):
        text.set_position(frame[i, :3])
