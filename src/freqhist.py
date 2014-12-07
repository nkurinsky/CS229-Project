import numpy

def freqbins(x,nbins=10):
    xt = numpy.sort(x)
    step=numpy.floor(len(xt)/nbins)
    inds = numpy.arange(0,len(xt),step,dtype=numpy.int64)
    return xt[inds]

def binnum(x,bins):
    xbin = 0
    pts = numpy.where(x > bins)[0]
    if(len(pts) > 0):
        xbin=pts[-1]
    return xbin
    

    
