from pylab import *
import numpy as np

newtab=np.load("sd.npy")
truth=np.load("truth.npy")

n = size(newtab[0])

s = truth == 2
g = truth == 1

for i in range(0,n):
    figure(i)
    hist([newtab[:,i][g],newtab[:,i][s]],bins=45,range=[-7.5,7.5],normed=True,color=['b','r'],histtype='stepfilled',alpha=0.5)
    #hist(newtab[:,i][s],bins=100,range=[-10,10],normed=True,color='r')

show()
