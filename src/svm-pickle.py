from varplot import *
from sklearn.svm import LinearSVC
import numpy as np
import pickle

#inpfile="/Users/noah/Documents/Class Repositories/data/round1Standardized.fits"

data = np.load("sd.npy")
truth = np.load("truth.npy")

input=open("data.pkl",'rb')
clf = pickle.load(input)
input.close()

print(clf.score(data,truth))
