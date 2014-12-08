from varplot import *
from sklearn.linear_model import SGDClassifier
import numpy as np
import pickle

#inpfile="/Users/noah/Documents/Class Repositories/data/round1Standardized.fits"

data = np.load("sd.npy")
truth = np.load("truth.npy")

print(len(data))

clf = SGDClassifier(loss="log",class_weight="auto")
clf.fit(data,truth)

testdata = np.load("sd_test.npy")
testtruth = np.load("truth_test.npy")

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

output=open("lr.pkl",'wb')

pickle.dump(clf,output)

output.close()
