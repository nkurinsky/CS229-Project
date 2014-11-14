import pyfits
from numpy import *
import warnings
import math
from sklearn import preprocessing
warnings.filterwarnings('ignore')

f = pyfits.open("../../data/training.fits")
tbdata = f[1].data
tbcols = f[1].data.columns.names

interesting_cols=[]

for col in tbcols:
    if not ("err" in col) and not("acs" in col) and not("threshold" in col):
        if ("mag_auto" in col) or ("fwhm_world" in col) or ("mu_" in col) or ("chi2_" in col):
            interesting_cols.append(col)

print interesting_cols

truth_col = 'mu_class_acs'
truth = tbdata[truth_col]

#number of training examples
m = len(tbdata[truth_col])

#number of features in the above list
n = len(interesting_cols)

boring_cols = []
for j in range(0, n):
    boring = True
    coldata = tbdata[interesting_cols[j]]
    for i in range(0, m):
        if coldata[i]!=0:
            boring = False
            break
    if boring:
        boring_cols.append(interesting_cols[j])
for j in boring_cols:
    interesting_cols.remove(j)
    n-=1

#make means 0 and variances 1 for PCA
standardized_data = [[0.0 for i in range(0, n)] for j in range(0, m)]

for i in range(0,n):
    newcol = preprocessing.scale(tbdata[interesting_cols[i]])
    for j in range(0,m):
        standardized_data[j][i] = newcol[j]
    print(std(newcol))
    print(mean(newcol))


tbhdu = pyfits.BinTableHDU.from_columns(pyfits.ColDefs(
   [pyfits.Column(name=interesting_cols[j], format='D', array=array(standardized_data[:][j])) for j in range(0, n)]))
truthhdu = pyfits.BinTableHDU.from_columns(pyfits.ColDefs(
    [pyfits.Column(name="truth", format='I', array=array(truth))]))

hdulist = pyfits.HDUList([f[0],tbhdu,truthhdu])
hdulist.writeto('../../data/round1Standardized.fits',clobber=True)
