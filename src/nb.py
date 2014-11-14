from varplot import *
from sklearn.svm import LinearSVC
import numpy as np
import pickle

#inpfile="/Users/noah/Documents/Class Repositories/data/round1Standardized.fits"

data = np.load("sd.npy")
truth = np.load("truth.npy")

clf = LinearSVC()
clf.fit(data,truth)

print(clf.score(data,truth))

output=open("data.pkl",'wb')

pickle.dump(clf,output)

output.close()
