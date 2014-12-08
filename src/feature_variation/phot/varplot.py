import pyfits
from pylab import *
import numpy
from matplotlib.pyplot import hist2d

def getTable(filename,usedpts=-1):
    hdus = pyfits.open(filename)
    if(usedpts == -1):
        return hdus[1].data
    else:
        return hdus[1].data[1:usedpts]

def getTruth(filename,usedpts=-1):
    hdus = pyfits.open(filename)
    if(usedpts == -1):
        return hdus[2].data
    else:
        return hdus[2].data[1:usedpts]

def colnames(ftable):
    return ftable.columns.names

def maxfilt(x,colname):
    #if ("fwhm" in colname):
    #    return 0.004
    if ("mag" in colname):
        return 35
    #elif ("chi2_detmodel" in colname):
    #    return 20000
    else:
        return max(x)
    
def minfilt(x,colname):
    if("Separation" in colname):
        return 0
    else:
        return min(x)

def varlog(x,colname):
    if ("chi2" in colname) or ("fwhm" in colname) or ("radius" in colname):
        zi = (x == 0)
        zin = (x > 0)
        x[zi] = min(x[zin])
        return log(abs(x))
    else:
        return x

def varplot(fitsTable, xfield, yfield, save=False): 
    
    x = fitsTable[xfield]
    y = fitsTable[yfield]
    labels = fitsTable['mu_class_acs']
    
    x=varlog(x,xfield)
    y=varlog(y,yfield)

    s = labels == 2
    g = labels == 1
    
    xmin = minfilt(x,xfield)
    xmax = maxfilt(x,xfield)
    ymin = minfilt(y,yfield)
    ymax = maxfilt(y,yfield)
    
    figure(figsize=[18,9])
    
    subplot(121)
    #scatter(x[g],y[g],s=1,color='b')
    hist2d(x[g],y[g])
    xlim(xmin,xmax)
    ylim(ymin,ymax)
    xlabel(xfield)
    ylabel(yfield)
    title("Galaxies")
    
    subplot(122)
    #scatter(x[s],y[s],s=1,color='r')
    hist2d(x[s],y[s])
    xlim(xmin,xmax)
    ylim(ymin,ymax)
    xlabel(xfield)
    ylabel(yfield)
    title("Stars")
    
    if(save):
        savefig("varplot_"+xfield+"_"+yfield+".png")
    else:
        show()

def vhistplot(fitsTable, field, save=False): 
    
    x = fitsTable[field]
    if("chi2" in field):
        zi = (x == 0)
        zin = (x > 0)
        x[zi] = min(x[zin])
        x = log(x)
    labels = fitsTable['mu_class_acs']
    
    s = labels == 2
    g = labels == 1
    
    xmin = minfilt(x,field)
    xmax = maxfilt(x,field)
    
    figure(figsize=[18,9])
    
    subplot(121)
    hist(x[g],color='b',bins=40,log=True,range=[xmin,xmax],normed=True)
    xlim(xmin,xmax)
    xlabel(field)
    ylabel("Fraction")
    title("Galaxies")
    
    subplot(122)
    hist(x[s],color='r',bins=40,log=True,range=[xmin,xmax],normed=True)
    xlim(xmin,xmax)
    xlabel(field)
    ylabel("Fraction")
    title("Stars")
    
    if(save):
        savefig("histplot_"+xfield+"_"+yfield+".png")
    else:
        show()

def trainplot(filename,xfield, yfield, save=False,usedpts=100000):
    ftable=getTable(filename,usedpts)
    varplot(ftable,xfield,yfield,save=save)
