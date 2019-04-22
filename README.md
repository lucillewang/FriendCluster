# FriendCluster
## Mobile Links
Mobile client: [FriendClusterClient](https://github.com/TrySickle/FriendClusterClient)  
Server: [FriendClusterServe](https://github.com/TrySickle/FriendClusterServer)

## Installation
Clone this repo  
Install python3 and pip  
pip install matplotlib numpy imagio

## Running Trace Generator
python3 walkgen.py \<outfile> \<dHeading> \<dStrength> \<delay>  
- outfile is the .txt file to write output to
- dHeading is the direction to walk in from 0 - 360 where 0 is north, proceeding counter-clockwise  
- dStrength, 0 is random, 100 is fully going towards the heading, between is probabilistic
- delay is how many ticks to randomly walk before following its heading

## Running Simulator
python3 simulate.py (f center_x center_y) or (d) \<trace_file1> \<trace_file2>.....  
- enter f and the center of the circle to create a fixed circle simulation
- enter d to have it dynamically move
- then enter all trace file names
