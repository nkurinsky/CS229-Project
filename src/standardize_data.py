import pyfits
from numpy import *
import math

f = pyfits.open("../Data/round1/round1_training_set.fits")
tbdata = f[1].data
tbcols = f[1].columns
#print tbcols
interesting_cols = ['flux_radius_g', 'fwhm_world_g',
                    'x2win_world_g', 'xywin_world_g',
                    'y2win_world_g',
                    'flux_auto_g',
                    'flux_model_g', 'flux_detmodel_g',
                    'mag_auto_g', 'mag_model_g',
                    'mag_detmodel_g', 'mag_psf_g',
                    'mag_aper_3_g', 'mag_aper_4_g',
                    'mag_aper_11_g', 'mu_eff_model_g',
                    'mu_mean_model_g', 'mu_max_model_g',
                    'mu_max_g', 'zeropoint_g',
                    'flags_g', 'flags_detmodel_g',
                    'flags_model_g', 'flags_weight_g',
                    'chi2_detmodel_g', 'chi2_model_g',
                    'niter_detmodel_g', 'niter_model_g',
                    'chi2_psf_g', 'niter_psf_g',
                    'nlowweight_iso_g']
truth_col = 'mu_class_acs'
truth = tbdata[truth_col]
#print (tbdata[truth_col])[tbdata[truth_col]==2]

#print tbdata[interesting_cols[4]]

#number of training examples
m = min(len(tbdata[truth_col]), 50)

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

#print interesting_cols
#print tbcols[interesting_cols]

#make means 0 and variances 1 for PCA
standardized_data = [[0.0 for i in range(0, n)] for j in range(0, m)]
mu = [0.0 for key in interesting_cols]
sigmasq = [0.0 for key in interesting_cols]

for j in range(0, n):
    col = interesting_cols[j]
    col_data = tbdata[col]
    for i in range(0, m):
        mu[j] += (1.0/m) * col_data[i]
        
for i in range(0, m):
    for j in range(0, n):
        col = interesting_cols[j]
        standardized_data[i][j] = tbdata[col][i]-mu[j]
        
for j in range(0, n):
    for i in range(0, m):
        sigmasq[j] += (1.0/m) * standardized_data[i][j]**2

for j in range(0, n):
    for i in range(0, m):
        standardized_data[i][j] /= sqrt(sigmasq[j])

tbhdu = pyfits.BinTableHDU.from_columns(pyfits.ColDefs(
   [pyfits.Column(name=interesting_cols[j], format='D', array=array(standardized_data[:][j])) for j in range(0, n)]))
tbhdu.writeto('../Data/modified/round1Standardized.fits', clobber=True)