"""
notes
    600x600 grid
    start within 15(?) radius circle (snap inwards) of 299,299
    fixed sim length (how many cycles to get useful data?)

params: file name, xDrift, yDrift, delay

walk
    random xy+- equally weighted, chance to wait for number of seconds
    if simtime past delay, inc. drift params

writeout
"""
import sys
import math
import random

#global defs
global canvasDim
global simLen
global x
global y

def simulation(infile, outfile, top, left, bottom, right):
    global canvasDim
    global simLen

    dH = top-bottom;
    dW = right-left;

    
    fo = open(outfile, "w")
    with open(infile) as f:
      for pair in f:
          (a, b) = pair.split(',')
          a = (top- float(a)) /dH * 600
          b = (right- float(b)) / dW * 600
          fo.write(str(int(a)) + "," + str(int(b)) + "\n")
    f.close()
# out file name, x drift, y drift, delay
if __name__ == "__main__":
    global canvasDim
    global simLen
    global x
    global y

    if len(sys.argv) == 7:
        infile = sys.argv[1]
        outfile = sys.argv[2]
        top = float(sys.argv[3])
        left = float(sys.argv[4])
        bottom = float(sys.argv[5])
        right = float(sys.argv[6])

        canvasDim = 600

        simulation(infile, outfile, top, left, bottom, right)
        print("Simulation complete! Results outputted in", outfile)
    if len(sys.argv) == 3:
        infile = sys.argv[1]
        outfile = sys.argv[2]
        top = 33.774000
        left = -84.396678
        bottom = 33.775495
        right = -84.398446

        canvasDim = 600

        simulation(infile, outfile, top, left, bottom, right)
        print("Simulation complete! Results outputted in", outfile)

    else:
        print("Usage: python3 coordinateNormailzer.py <infile> <outfile> <top> <left> <bottom> <right> or \npython3 coordinateNormailzer.py <infile> <outfile>")
