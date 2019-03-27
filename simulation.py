import matplotlib.pyplot as plt
import numpy as np
import sys

def simulation(file):
    x = []
    y = []
    with open(file) as f:
        for pair in f:
            (a, b) = pair.split(',')
            x.append(int(a))
            y.append(int(b))

    colors = ['red']
    plot = plt.figure()

    x = np.array(x)
    y = np.array(y)

    plt.quiver(x[:-1], y[:-1], x[1:] - x[:-1], y[1:] - y[:-1], scale_units='xy', angles='xy', scale=1, color=colors[0])

    plt.show(plot)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 simulate.py <trace_file>")
    else:
        trace_file = sys.argv[1]
        simulation(trace_file)