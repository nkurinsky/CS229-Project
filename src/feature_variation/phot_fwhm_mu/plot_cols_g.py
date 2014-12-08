from varplot import *
import numpy

xfield='ra'
yfield='dec'

usedpts = 100000

hdus = pyfits.open("../../data/training.fits")
ftable=hdus[1].data
ftable=ftable[0:usedpts]

cols=ftable.columns.names
mycols=[]

for col in cols:
    if not ("err" in col) and ("_g" in col) and not("acs" in col) and not("niter" in col) and not("win_world" in col) and not ("flags_model" in col) and not ("flags_weight" in col):
        mycols.append(col)

npmycols = numpy.array(mycols)
endcol=len(mycols)-1
print(npmycols)
print(endcol)

for xfield in mycols:
    print(numpy.where(npmycols == xfield))
    startcol=numpy.where(npmycols == xfield)[0][0]+1
    for i in range(startcol,endcol):
        yfield = mycols[i]
        print("Plotting "+xfield+" versus "+yfield)
        varplot(ftable, xfield, yfield, save=True)
