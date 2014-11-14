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

pts = where((truth == 1) | (truth == 2))[0]
print(len(pts))
truth = truth[pts]

#number of training examples
m = len(truth)

#number of features in the above list
n = len(interesting_cols)

boring_cols = []
for j in range(0, n):
    boring = True
    coldata = tbdata[interesting_cols[j]][pts]
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
    tempdata = tbdata[interesting_cols[i]][pts]
    newcol = preprocessing.scale(tempdata)
    for j in range(0,m):
        standardized_data[j][i] = newcol[j]

print(len((array(standardized_data).transpose()[1])))

tbhdu = pyfits.BinTableHDU.from_columns(pyfits.ColDefs(
   [pyfits.Column(name=interesting_cols[j], format='D', array=array(standardized_data).transpose()[j]) for j in range(0, n)]))
print(len(tbhdu.data["fwhm_world_g"]))
truthhdu = pyfits.BinTableHDU.from_columns(pyfits.ColDefs(
    [pyfits.Column(name="truth", format='I', array=array(truth))]))

hdulist = pyfits.HDUList([f[0],tbhdu,truthhdu])
hdulist.writeto('../../data/round1Standardized.fits',clobber=True)

save("sd.npy", array(standardized_data))
save("truth.npy", array(truth))
