import pyfits
from numpy import *
import warnings
import math
from sklearn import preprocessing
warnings.filterwarnings('ignore')

f = pyfits.open("../../../../data/training.fits")
tbdata = f[1].data
tbcols = f[1].data.columns.names

interesting_cols=[]

for col in tbcols:
    if not ("err" in col) and not("acs" in col) and not("threshold" in col):
        if ("mag_auto" in col) or ("mag_detmodel" in col):
            interesting_cols.append(col)

for i in range(0,len(interesting_cols),5):
    printstring=""
    for j in range(0,5):
        printstring=printstring+interesting_cols[i+j]+" "
    print printstring 

truth_col = 'mu_class_acs'
truth = tbdata[truth_col]

pts = where((truth == 1) | (truth == 2))[0]
print(len(pts))
truth = truth[pts]

#number of training examples
m = len(truth)

#number of features in the above list
n = len(interesting_cols)

#make means 0 and variances 1 for PCA
standardized_data = [[0.0 for i in range(0, n)] for j in range(0, m)]

for i in range(0,n):
    colname=interesting_cols[i]
    tempdata = tbdata[colname][pts]
    if ("chi2" in colname) or ("fwhm" in colname):
        print "Logging "+colname
        zi = (tempdata == 0)
        zin = (tempdata > 0)
        tempdata[zi] = min(tempdata[zin])
        tempdata = log10(abs(tempdata))

    newcol = preprocessing.scale(tempdata)
    for j in range(0,m):
        standardized_data[j][i] = newcol[j]

print(len((array(standardized_data).transpose()[1])))

save("sd.npy", array(standardized_data))
save("truth.npy", array(truth))
