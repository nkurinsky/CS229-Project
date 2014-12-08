import pyfits
from numpy import *
import warnings
from math import *
from sklearn import preprocessing
warnings.filterwarnings('ignore')

f = pyfits.open("../data/round1/round1_training_set.fits")
tbdata = f[1].data
tbcols = f[1].data.columns.names

#degrees, use small-angle approx
interesting_cols=["ra","dec"]

truth_col = 'mu_class_acs'
truth = tbdata[truth_col]

pts = where((truth == 1) | (truth == 2))[0]
truth = truth[pts]

#number of training examples
m = len(truth)

#number of features in the above list
n = len(interesting_cols)

#make means 0 and variances 1 for PCA
standardized_data = [0.0 for j in range(0, m)]

def deg_to_rad(deg): return math.pi * deg/180.0
def dist(ra1,dec1,ra2,dec2): return acos(sin(dec1)*sin(dec2)+cos(dec1)*cos(dec2)*cos(ra1-ra2))

radata = map(deg_to_rad, tbdata["ra"][pts])
decdata = map(deg_to_rad, tbdata["dec"][pts])
for j in range(0,m):
    smallest_angular_dist = -1
    print j
    for k in range(0,m):
        if k==j:
            continue
        angular_dist = dist(radata[j],decdata[j],radata[k],decdata[k])
        if angular_dist < smallest_angular_dist or smallest_angular_dist == -1:
            smallest_angular_dist = angular_dist
    standardized_data[j] = smallest_angular_dist
newcol = preprocessing.scale(standardized_data)

save("angular_dist.npy", array(newcol))