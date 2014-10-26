from __future__ import division
import sys, math, time
import numpy as np
from matplotlib import pyplot as plt
from pylab import *
import threading
import Queue
import datetime

st = 100.0
runs = 10000
my = 0.45
iterations = 1000
variance = 0.3
delta_t = 0.001
counter = 0
barrier = 15

threads = 4

class Worker(threading.Thread):
    def __init__(self, input_q, output_q):
        super(Worker, self).__init__()
        self.input_q = input_q
        self.output_q = output_q
        self.daemon = True
        
    def run(self):
        while True:
            data = self.input_q.get()
            if data == None:
                break
            st_next = st
            for i in range(iterations):
                st_next = (st_next)*(math.e)**((my-(0.5*variance)**2)*(delta_t)+(data[i]*math.sqrt(delta_t)))
                if st_next < barrier:
                    self.output_q.put(False)
                    break
            self.output_q.put(st_next)

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

def main():
    start = datetime.datetime.now()
    input_q = Queue.Queue()
    output_q = Queue.Queue()
    
    thread_list = []
    
    for i in range(threads):
        thread_list.append(Worker(input_q, output_q))
    for t in thread_list:
        t.start()
        
    for i in range(runs):
        input_q.put(np.random.randn(1,iterations)[0])
    for i in range(threads):
        input_q.put(None)
    for t in thread_list:
        t.join()
    left = True
    broke = 0
    while left:
        try:
            data = output_q.get_nowait()
            if data == False:
                broke += 1
            else:
                print "Final value:",data
        except Queue.Empty:
            left = False
          
    print "Broke", broke,"/",runs, "time(s)"
    print "Barrier:", barrier
    print "Barrier hit rate:", broke*100/runs, "%"
    end = datetime.datetime.now() - start
    print "Time taken:", end
    print "Simulations/sec:", runs/end.total_seconds()



if __name__ == '__main__':
    main()

