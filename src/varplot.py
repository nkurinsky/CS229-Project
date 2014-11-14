import pyfits
from pylab import *
import numpy

def getTable(filename,usedpts=-1):
    hdus = pyfits.open(filename)
    if(usedpts == -1):
        return hdus[1].data
    else:
        return hdus[1].data[1:usedpts]

def colnames(ftable):
    return ftable.columns.names

def maxfilt(x,colname):
    if ("fwhm" in colname):
        return 0.004
    elif ("mag" in colname):
        return 35
    else:
        return max(x)
    
def minfilt(x,colname):
    if("Separation" in colname):
        return 0
    else:
        return min(x)

def varplot(fitsTable, xfield, yfield, save=False): 
    
    x = fitsTable[xfield]
    y = fitsTable[yfield]
    labels = fitsTable['mu_class_acs']
    
    s = labels == 2
    g = labels == 1
    
    xmin = minfilt(x,xfield)
    xmax = maxfilt(x,xfield)
    ymin = minfilt(y,yfield)
    ymax = maxfilt(y,yfield)
    
    figure(figsize=[18,9])
    
    subplot(121)
    scatter(x[g],y[g],s=1,color='b')
    xlim(xmin,xmax)
    ylim(ymin,ymax)
    xlabel(xfield)
    ylabel(yfield)
    title("Galaxies")
    
    subplot(122)
    scatter(x[s],y[s],s=1,color='r')
    xlim(xmin,xmax)
    ylim(ymin,ymax)
    xlabel(xfield)
    ylabel(yfield)
    title("Stars")
    
    if(save):
        savefig("varplot_"+xfield+"_"+yfield+".png")
    else:
        show()

def trainplot(filename,xfield, yfield, save=False,usedpts=100000):
    ftable=getTable(filename,usedpts)
    varplot(ftable,xfield,yfield,save=save)
