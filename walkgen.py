"""
notes
    500x500 grid
    start within 15(?) radius circle (snap inwards) of 249,249
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

def adjust(degree):
  global x
  global y
  degree = degree % 360
  if degree >= 338 or degree < 22:
      y += 3    
  elif degree >=22 and degree < 67:
      x -= 2
      y += 2
  elif degree >=67 and degree < 112:
      x -= 3
  elif degree >=112 and degree < 157:
      x -= 2
      y -= 2
  elif degree >=157 and degree < 202:
      y -= 3
  elif degree >=202 and degree < 247:
      x += 2
      y -= 2
  elif degree >=247 and degree < 338:
      x += 3
  else:
      x += 2
      y += 2
      
def simulation(dHeading, dStrength, delay, out_file):
    global canvasDim
    global simLen
    global x
    global y
    
    ticks = 0
    f = open(out_file, "w")
  
    while (ticks < simLen):
        if ticks > delay and dStrength > 0:
            adjust((random.randint(1, dStrength)) + dHeading - (dStrength/2))
        else:
            adjust(random.randint(1, 360))
        f.write(x,y)
        ticks += 1
    f.close()

# out file name, x drift, y drift, delay
if __name__ == "__main__":
    global canvasDim
    global simLen
    global x
    global y

    if len(sys.argv) != 5:
        print("Usage: python3 walkgen.py <outfile> <dHeading> <dStrength> <delay>")
    else:
        out_file = sys.argv[1]
        dHeading = int(sys.argv[2])
        dStrength = int(sys.argv[3])
        delay = int(sys.argv[4])

        canvasDim = 600
        simLen = 200
        x = 299
        y = 299
        print("Starting simulation with dHeading =", dHeading, "dStrength =", dStrength, "and delay =", delay)
        simulation(dHeading, dStrength, delay, out_file)
        print("Simulation complete! Results outputted in", out_file)