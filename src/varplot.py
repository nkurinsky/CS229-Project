import pyfits
from pylab import *
import numpy

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
    if ("fwhm" in colname):
        return -5
    elif ("mag" in colname):
        return 32
    #elif ("chi2_detmodel" in colname):
    #    return 20000
    else:
        return max(x)
    
def minfilt(x,colname):
    if("Separation" in colname):
        return 0
    elif("fwhm" in colname):
        return -10
    elif ("mag" in colname):
        return 14
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
    
    figure()
    h,xh,yh=histogram2d(y[g],x[g],bins=100,normed=True)
    contourf(h,colors='b',levels=[1.0,0.5,0.1,0.05,0.01,0.005,0.001,0.0005],extent=[yh[0], yh[-1], xh[0], xh[-1]],label="Galaxies",alpha=0.2)
    h,xh,yh=histogram2d(y[s],x[s],bins=100,normed=True)
    cs = contourf(h,colors='r',levels=[1.0,0.5,0.1,0.05,0.01,0.005],extent=[yh[0], yh[-1], xh[0], xh[-1]],label="Stars",alpha=0.2)

    xlim(xmin,xmax)
    ylim(ymin,ymax)
    xlabel(xfield)
    ylabel(yfield)
    
    proxy = [Rectangle((0,0),1,1,fc = pc) 
             for pc in ['r','b']]
    
    legend(proxy,["Stars","Galaxies"],loc="upper right")
    
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
    
    figure()
    hist([x[g],x[s]],color=['b','r'],bins=40,normed=True,histtype='stepfilled',label=["Galaxies","Stars"],alpha=0.5,range=[xmin,xmax])
    xlim(xmin,xmax)
    ylim(0,0.2)
    xlabel(field)
    ylabel("Fraction")
    legend(loc='upper right')
    
    if(save):
        savefig("histplot_"+field+".png")
    else:
        show()

def trainplot(filename,xfield, yfield, save=False,usedpts=100000):
    ftable=getTable(filename,usedpts)
    varplot(ftable,xfield,yfield,save=save)

def hplot(field,save=False):
    mytab=getTable("../../data/training.fits")
    vhistplot(mytab,field,save=save)
