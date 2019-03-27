import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys


def simulation(file):
    x = []
    y = []
    with open(file) as f:
        for pair in f:
            (a, b) = pair.split(',')
            x.append(int(a))
            y.append(int(b))

    fig, ax = plt.subplots()


    xdata, ydata = [], []
    ln, = plt.plot([], [], 'ro')

    frames = zip(x, y)
    def init():
        ax.set_xlim(0, 600)
        ax.set_ylim(0, 600)
        return ln,


    def update(frame):
        xdata.append(frame[0])
        if len(xdata) > 20:
            xdata.pop(0)
        ydata.append(frame[1])
        if len(ydata) > 20:
            ydata.pop(0)
        ln.set_data(xdata, ydata)
        return ln,


    ani = FuncAnimation(fig, update, frames=frames,
                        init_func=init, blit=True, interval=10)
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 simulate.py <trace_file>")
    else:
        trace_file = sys.argv[1]
        simulation(trace_file)
