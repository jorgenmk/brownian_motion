import sys, math, time, datetime
import numpy as np
from matplotlib import pyplot as plt
from pylab import *

st = 100.0
runs = 1000
my = 0.045
iterations = 10000
variance = 0.3
delta_t = 1.0/iterations
counter = 0
barrier = 65

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

start = datetime.datetime.now()
for times in range(runs):
    
    # Start from st every run
    st_next = st

    # Setup normalized random values
    e = np.random.randn(1,iterations)[0]
    
    broke = False
    data = []
    for dt_c in range(iterations):
        st_next = (st_next)*(math.e)**((my-0.5*(variance**2))*(delta_t)+(variance*e[dt_c]*math.sqrt(delta_t)))
        data.append(st_next)
                
        if st_next < barrier:
            broke = True
            break
    #plot_data(data, times)     
    if broke:
        counter += 1
end = datetime.datetime.now() - start
print "Broke", counter,"/",runs, "time(s)"
print "Time:", end
print "Rate:", counter*100.0/runs
print "Simulations/sec:", runs/end.total_seconds()


