from pylab import *
from sklearn.svm import LinearSVC
import numpy as np
import pickle

pklfile="svm-c100.0-g0.01.pkl"

data = np.load("../../sd.npy")
truth = np.load("../../truth.npy")

input=open(pklfile,'rb')
clf = pickle.load(input)
input.close()

testdata = np.load("../../sd_test.npy")
testtruth = np.load("../../truth_test.npy")

#tdata = data[0:numpts]
#ttruth = truth[0:numpts]
decdata = testdata
dectruth = testtruth

#tdists=clf.decision_function(tdata)
dists=clf.decision_function(decdata)

#s = np.where(ttruth == 2)[0]
sdt = np.where(dectruth == 2)[0]
#g = np.where(ttruth == 1)[0]
gdt = np.where(dectruth == 1)[0]

figure(1)
hist(dists[sdt],color='r',bins=200,normed=True,range=[-10,10],alpha=0.5,histtype='stepfilled',label="Stars")
hist(dists[gdt],color='b',bins=200,normed=True,range=[-10,10],alpha=0.5,histtype='stepfilled',label="Galaxies")
plot([0,0],[0,1.2],label="Class Separation",color='k')
legend(loc="upper right")
xlabel("Distance from Decision Boundary")
ylabel("Fraction of Samples")
title("Gaussian SVM Performance, C=100.0, gamma=0.01")

#figure(2)
#hist(tdists[s],color='r',bins=200,normed=True,range=[-10,10],alpha=0.5,histtype='stepfilled',label="Stars")
#hist(tdists[g],color='b',bins=200,normed=True,range=[-10,10],alpha=0.5,histtype='stepfilled',label="Galaxies")
#plot([0,0],[0,1.2],label="Class Separation")
#legend(loc="upper right")

show()
