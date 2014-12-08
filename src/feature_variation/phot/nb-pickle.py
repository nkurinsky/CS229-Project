from varplot import *
from sklearn.svm import LinearSVC
import numpy as np
import pickle

#inpfile="/Users/noah/Documents/Class Repositories/data/round1Standardized.fits"

data = np.load("sd_nb.npy")
truth = np.load("truth.npy")

input=open("nb.pkl",'rb')
clf = pickle.load(input)
input.close()

testdata = np.load("sd_test_nb.npy")
testtruth = np.load("truth_test.npy")

print("l1")
print(clf.score(data,truth))
print(clf.score(testdata,testtruth))

s = np.where(truth == 2)[0]
st = np.where(testtruth == 2)[0]
g = np.where(truth == 1)[0]
gt = np.where(testtruth == 1)[0]
print("Stars")
print(clf.score(data[s],truth[s]))
print(clf.score(testdata[st],testtruth[st]))
print("Galaxies")
print(clf.score(data[g],truth[g]))
print(clf.score(testdata[gt],testtruth[gt]))


