import pyfits
from svmutil import *
from numpy import *
import warnings
import math
warnings.filterwarnings('error')

f = pyfits.open("../Data/round1/round1_test_set.fits")
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
m = min(len(tbdata[truth_col]), 1000)

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

print interesting_cols

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
        
x = [array(standardized_data[i]) for i in range(0, m)]
bigsigma = mat(zeros((n,n)))
for i in range(0, m):
    bigsigma += (1.0/m) * mat(outer(x[i],x[i]))
    
w, v = linalg.eig(bigsigma)
eigendirs = [0] * n
usedup = [False] * n
for direc in range(0,n):
    biggesteig = -1
    biggesteignum = -1
    for i in range(0,n):
        if (not usedup[i]) and w[i]>biggesteig:
            biggesteig = w[i]
            biggesteignum = i
    eigendirs[direc] = biggesteignum
    usedup[biggesteignum] = True
        
print v[:, eigendirs[0]]
#print w[eigendirs[0]]
#print w


#Compute components wrt this new basis, using k principal components
k=10


y=[array([dot(array(v[:,eigendirs[j]]).T, x[i])[0] for j in range(0, k)]) for i in range(0, m)]
#print y

#implement logistic regression with y being our feature matrix

#k features, plus intercept term
theta = array([0.0] * (k+1))

#sigmoid function
def g(z):
    if z<-100:
        return 0
    elif z>100:
        return 1
    return 1.0/(1.0+math.exp(-z))

def theta_dot_including_intercept(x):
    res = theta[0]
    for i in range(0, k):
        res += theta[i+1] * x[i]
    return res

def h(x):
    #the +1 is because the truth data labels are 1 and 2, not 0 and 1
    return g(theta_dot_including_intercept(x))+1

def prediction(x):
    if h(x)>=1.5:
        return 2
    return 1
    
#learning rate
alpha = 0.001

#tolerance
epsilon = 0.001 * m

while True:
    total_change = 0
    for i in range(0,m):
        for j in range(0,k+1):
#            print "maroo "+str(i)+" "+str(h(y[i]))+" "+str(j)
            if j==0:
                change = alpha * (truth[i]-h(y[i])) * 1
            else:
                change = alpha * (truth[i]-h(y[i])) * y[i][j-1]
#            print change
            theta[j] += change
            total_change += abs(change)
    if total_change < epsilon:
        break
#    print total_change

#number of misclassifications by our hypothesis
error_num = 0

for i in range(0, m):
    if not prediction(y[i])==truth[i]:
        error_num += 1

print error_num*1.0/m