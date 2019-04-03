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

    fig, ax = plt.subplots()
    ax.set_xlim(0, 600)
    ax.set_ylim(0, 600)

    lines = [plt.plot([], [], linewidth=3.0)[0] for i in range(len(allX))]
    xDatas = []
    yDatas = []
    
    for i in range(len(allX)):
        xDatas.append([])
        yDatas.append([])

    radius = 30
    circle = plt.Circle((300, 300), radius, fill=False)

    ax.add_artist(circle)

    def get_centroid(x, y):
        return (sum(x) / len(x), sum(y) / len(y))

    def in_circle(cx, cy, r, zipped):
        return [(z[0] - cx) ** 2 + (z[1] - cy) ** 2 < r ** 2 for z in zipped]

    def init():
        for ln in lines:
            ln.set_data([], [])
        shapes = lines.copy()
        shapes.append(circle)
        return shapes

    def update(frame):
        # print(frame)
        for i in range(len(xDatas)):
            xdata = xDatas[i]
            ydata = yDatas[i]
            xdata.append(allX[i][frame])
            if len(xdata) > 20:
                xdata.pop(0)
            ydata.append(allY[i][frame])
            if len(ydata) > 20:
                ydata.pop(0)
            lines[i].set_data(xdata, ydata)
        
        xPoints = []
        yPoints = []
        for x in allX:
            xPoints.append(x[frame])
        for y in allY:
            yPoints.append(y[frame])
        center = get_centroid(xPoints, yPoints)
        # print(center)
        circle.center = center
        zipped = list(zip(xPoints, yPoints))
        # print(zipped)
        # print(circle.center)
        contains = in_circle(center[0], center[1], radius, zipped)
        print(contains)
        shapes = lines.copy()
        shapes.append(circle)
        return shapes

    ani = FuncAnimation(fig, update, frames=len(allX[0]),
                        init_func=init, blit=True, interval=50, repeat=False)

    fig.set_size_inches(7, 7)
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 simulate.py <trace_file1> <trace_file2>.....")
    else:
        trace_files = sys.argv[1:]
        simulation(trace_files)
