import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys


def simulation(files):
    allX = []
    allY = []
    for trace in files:
        with open(trace) as f:
            x = []
            y = []
            allX.append(x)
            allY.append(y)
            for pair in f:
                (a, b) = pair.split(',')
                x.append(int(a))
                y.append(int(b))

    # print(allX)

    fig, ax = plt.subplots()
    ax.set_xlim(0, 600)
    ax.set_ylim(0, 600)

    lines = [plt.plot([], [], linewidth=3.0)[0] for i in range(len(allX))]
    xDatas = []
    yDatas = []
    for i in range(len(allX)):
        xDatas.append([])
        yDatas.append([])

    def init():
        for ln in lines:
            ln.set_data([], [])
        return lines

    def update(frame):
        # print(frame)
        for x in range(len(xDatas)):
            xdata = xDatas[x]
            ydata = yDatas[x]
            xdata.append(allX[x][frame])
            if len(xdata) > 20:
                xdata.pop(0)
            ydata.append(allY[x][frame])
            if len(ydata) > 20:
                ydata.pop(0)
            lines[x].set_data(xdata, ydata)
        return lines

    ani = FuncAnimation(fig, update, frames=len(allX[0]),
                        init_func=init, blit=True, interval=10, repeat=False)
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 simulate.py <trace_file1> <trace_file2>.....")
    else:
        trace_files = sys.argv[1:]
        simulation(trace_files)
