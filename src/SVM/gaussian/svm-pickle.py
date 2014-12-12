from sklearn.svm import LinearSVC
import numpy as np
import pickle

pklfile="svm-c100.0-g0.01.pkl"

data = np.load("sd.npy")
truth = np.load("truth.npy")

input=open(pklfile,'rb')
clf = pickle.load(input)
input.close()

testdata = np.load("sd_test.npy")
testtruth = np.load("truth_test.npy")

numpts
decdata = testdata[1:1000]
print(len(decdata))
print(shape(decdata))

#s = np.where(truth == 2)[0]
#st = np.where(testtruth == 2)[0]
#g = np.where(truth == 1)[0]
#gt = np.where(testtruth == 1)[0]
#print("Stars")
#print(clfl1.score(data[s],truth[s]))
#print(clfl1.score(testdata[st],testtruth[st]))
#print("Galaxies")
#print(clfl1.score(data[g],truth[g]))
#print(clfl1.score(testdata[gt],testtruth[gt]))
