from pylab import *
import numpy as np

newtab=np.load("sd.npy")

n = size(newtab[0])

for i in range(0,n):
    figure(i)
    hist(newtab[:,i],bins=100,range=[-10,10],normed=True)

show()
