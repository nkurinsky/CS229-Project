import numpy

def freqbins(x,nbins=10):
    xt = numpy.sort(numpy.array(x))
    inds = numpy.arange(0,len(xt),floor(len(xt)/nbins))
    print(inds)
    return xt[inds]

    
