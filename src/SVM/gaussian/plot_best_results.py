import numpy as np
from pylab import *

[x,y,train,test,galaxies,stars,ratio]=np.loadtxt("abbreviated_results.txt",unpack=True)

gvals = [10.0,100.0,1000.0]
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
    ylabel("1-(Error)")
    title("Gaussian SVM Optimization, Test v Train")
    legend(loc="lower left",title="C",ncol=3)
    ylim(0.8,1.0)
    xlim(0.01,0.000001)

ind = 0
figure(2)
for gval in gvals:
    color = colors[ind]
    ind = ind+1
    pts = x == gval
    xpts = y[pts]
    spts = stars[pts]
    gpts = galaxies[pts]
    plot(xpts,spts,'--',label=str(gval)+", S",color=color)
    plot(xpts,gpts,'-',label=str(gval)+", G",color=color)
    xscale('log')
    xlabel("Gamma")
    ylabel("1-(Error)")
    title("Gaussian SVM Optimization for Classes")
    legend(loc="lower left",title="C",ncol=3)
    ylim(0.7,1.00)
    xlim(0.01,0.000001)                                                                    
    
show()
