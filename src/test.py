import pyfits
from svmutil import *
from numpy import *
import warnings
import math
warnings.filterwarnings('error')

f = pyfits.open("../Data/modified/round1Standardized.fits")
tbdata = f[1].data

truth_col = 'mu_class_acs'
truth = tbdata[truth_col]

#number of training examples
m = min(len(tbdata[truth_col]), 50)

#number of features in the above list
n = len(interesting_cols)
        
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