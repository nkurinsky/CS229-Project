from varplot import *
from sklearn.qda import QDA
import numpy as np
import pickle

data = np.load("sd.npy")
truth = np.load("truth.npy")

testdata = np.load("sd_test.npy")
testtruth = np.load("truth_test.npy")

print(len(data))

clf = QDA()
clf.fit(data,truth)

output=open("qda.pkl",'wb')

pickle.dump(clf,output)

output.close()

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