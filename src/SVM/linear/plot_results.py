import numpy as np
from pylab import *

[x,y]=np.loadtxt("results.txt",unpack=True)

xpts = x
ypts = y
plot(xpts,ypts)
xscale('log')
xlabel("C")
ylabel("1-(Training Error)")
title("Linear Kernel L1 SVM")
ylim(0.88,0.91)
xlim(0.001,1.0)

show()
