import sys, math, time
import numpy as np
from matplotlib import pyplot as plt
from pylab import *

st = 100.0
runs = 10
my = 0.45
iterations = 10000
variance = 0.3
delta_t = 0.0001
counter = 0
barrier = 15

def plot_data(data, name):
    x = range(len(data))
    plot(x, data)
    xlabel('iteration')
    ylabel('stock price')
    title('About as simple as it gets, folks')
    grid(True)
    axhline(y=barrier, label="Barrier")
    savefig("test-{}.png".format(name))
    clf()
    #show()

for times in range(runs):
    
    # Start from st every run
    st_next = st

    # Setup normalized random values
    e = np.random.randn(1,iterations)[0]
    
    broke = False
    data = []
    for dt_c in range(iterations):
        st_next = (st_next)*(math.e)**((my-(0.5*variance)**2)*(delta_t)+(e[dt_c]*math.sqrt(delta_t)))
        data.append(st_next)
                
        if st_next < barrier:
            broke = True
            break
    plot_data(data, times)     
    if broke:
        counter += 1

print "Broke", counter,"/",runs, "time(s)"


