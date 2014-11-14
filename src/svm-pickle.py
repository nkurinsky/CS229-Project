from varplot import *
from sklearn.svm import LinearSVC
import numpy as np
import pickle

#inpfile="/Users/noah/Documents/Class Repositories/data/round1Standardized.fits"

data = np.load("sd.npy")
truth = np.load("truth.npy")

input=open("svml1.pkl",'rb')
clfl1 = pickle.load(input)
input.close()

input=open("svml2.pkl",'rb')
clfl2 = pickle.load(input)
input.close()

testdata = np.load("sd_test.npy")
testtruth = np.load("truth_test.npy")

print("l1")
print(clfl1.score(data,truth))
print(clfl1.score(testdata,testtruth))

s = np.where(truth == 2)[0]
st = np.where(testtruth == 2)[0]
g = np.where(truth == 1)[0]
gt = np.where(testtruth == 1)[0]
print("Stars")
print(clfl1.score(data[s],truth[s]))
print(clfl1.score(testdata[st],testtruth[st]))
print("Galaxies")
print(clfl1.score(data[g],truth[g]))
print(clfl1.score(testdata[gt],testtruth[gt]))

print("\nl2")
print(clfl2.score(data,truth))
print(clfl2.score(testdata,testtruth))
print("Stars")
print(clfl2.score(data[s],truth[s]))
print(clfl2.score(testdata[st],testtruth[st]))
print("Galaxies")
print(clfl2.score(data[g],truth[g]))
print(clfl2.score(testdata[gt],testtruth[gt]))


print("Galaxy Number")
print(len(g))
print(len(gt))
print("Star Number")
print(len(s))
print(len(st))
