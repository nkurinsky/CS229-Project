from varplot import *
from sklearn.svm import LinearSVC
import numpy as np
import pickle

#inpfile="/Users/noah/Documents/Class Repositories/data/round1Standardized.fits"

data = np.load("sd.npy")
truth = np.load("truth.npy")

print(len(data))

clf = LinearSVC(loss="l1",class_weight="auto")
clf.fit(data,truth)

print(clf.score(data,truth))

output=open("svml1.pkl",'wb')

pickle.dump(clf,output)

output.close()
