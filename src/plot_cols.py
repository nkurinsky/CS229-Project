from varplot import *
import numpy

usedpts = 100000
ftable=getTable("training.fits",usedpts)
cols=ftable.columns.names

mycols=[]

for col in cols:
    if not ("err" in col) and not("acs" in col):
        if ("mag_auto" in col) or ("fwhm_world" in col):
            mycols.append(col)

npmycols = numpy.array(mycols)
endcol=len(mycols)-1
print(npmycols)

for xfield in mycols:
    startcol=numpy.where(npmycols == xfield)[0][0]+1
    for i in range(startcol,endcol):
        yfield = mycols[i]
        print("Plotting "+xfield+" versus "+yfield)
        varplot(ftable, xfield, yfield, save=True)
