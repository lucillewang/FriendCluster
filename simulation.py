import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from imageio import imread
import sys


def simulation(files, fixed_center):
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

    colors = ['red', 'blue', 'yellow', 'orange', 'white', 'cyan', 'magenta']

    lines = [plt.plot([], [], linewidth=3.0, color=colors[i])[0] for i in range(len(allX))]
    xDatas = []
    yDatas = []
    
    for i in range(len(allX)):
        xDatas.append([])
        yDatas.append([])

    radius = 60
    circle = plt.Circle((300, 300), radius, fill=False)

    ax.add_artist(circle)

    warning = plt.text(10, 0.5, '', fontsize=12)

    ax.add_artist(warning)

    def get_centroid(x, y):
        return (sum(x) / len(x), sum(y) / len(y))

    def in_circle(cx, cy, r, zipped):
        return [(z[0] - cx) ** 2 + (z[1] - cy) ** 2 < r ** 2 for z in zipped]

    def init():
        for ln in lines:
            ln.set_data([], [])
        shapes = lines.copy()
        shapes.append(circle)
        shapes.append(warning)
        return shapes

    def update(frame):
        # print(frame)
        for i in range(len(xDatas)):
            xdata = xDatas[i]
            ydata = yDatas[i]
            if frame == 0:
                xdata.clear()
                ydata.clear()
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
        if fixed_center:
            center = fixed_center
        else:
            center = get_centroid(xPoints, yPoints)
        # print(center)
        circle.center = center
        zipped = list(zip(xPoints, yPoints))
        # print(zipped)
        # print(circle.center)
        contains = in_circle(center[0], center[1], radius, zipped)
        # print(contains)
        
        s = ''
        for i in range(len(contains)):
            if not contains[i]:
                s += colors[i] + " is too far away!\n"
                circle.set_color("red")
        if s == '':
            circle.set_color("black")
        warning.set_text(s)

        shapes = lines.copy()
        shapes.append(circle)
        shapes.append(warning)
        return shapes

    ani = FuncAnimation(fig, update, frames=len(allX[0]),
                        init_func=init, blit=True, interval=50, repeat=True)

    fig.set_size_inches(7, 7)
    # plt.axis('off')

    green = imread('tech_green.jpg')
    plt.imshow(green, extent=[0.5, 599.5, -0.5, 599.5])
    # ax.set_facecolor('green')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 simulate.py (f center_x center_y) or (d) <trace_file1> <trace_file2>.....")
    else:
        fixed = sys.argv[1] == 'f'
        center = None
        if fixed:
            center = (int(sys.argv[2]), int(sys.argv[3]))
            trace_files = sys.argv[4:]
        else:
            trace_files = sys.argv[2:]
        simulation(trace_files, center)
