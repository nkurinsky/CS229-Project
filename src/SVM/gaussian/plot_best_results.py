import numpy as np
from pylab import *

[x,y,train,test,stars,galaxies]=np.loadtxt("full_results.txt",unpack=True)

gvals = [0.1,1.0,10.0]
colors = ['k','b','r','g','c','m']

ind = 0
figure(1)
for gval in gvals:
    color = colors[ind]
    ind = ind+1
    pts = x == gval
    xpts = y[pts]
    ypts = train[pts]
    ytpts = test[pts]
    plot(xpts,ypts,'--',label=str(gval)+", Train",color=color)
    plot(xpts,ytpts,'-',label=str(gval)+", Test",color=color)
    xscale('log')
    xlabel("Gamma")
    ylabel("1-(Training Error)")
    title("Gaussian SVM Optimization, Test v Train")
    legend(loc="lower left",title="C")
    ylim(0.4,1.1)
    xlim(10.0,0.001)

ind = 0
figure(2)
for gval in gvals:
    color = colors[ind]
    ind = ind+1
    pts = x == gval
    xpts = y[pts]
    spts = stars[pts]
    gpts = galaxies[pts]
    plot(xpts,spts,'--',label=str(gval)+", Stars",color=color)
    plot(xpts,gpts,'-',label=str(gval)+", Galaxies",color=color)
    xscale('log')
    xlabel("Gamma")
    ylabel("1-(Training Error)")
    title("Gaussian SVM Optimization for Classes")
    legend(loc="lower left",title="C")
    ylim(0.4,1.1)
    xlim(10.0,0.001)                                                                    
    
show()
