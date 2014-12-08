from varplot import *
from sklearn.svm import SVC
import numpy as np
import pickle

data = np.load("sd.npy")
truth = np.load("truth.npy")

print(len(data))

clf = SVC(class_weight="auto",kernel="rbf",gamma=1.0,verbose=True)
clf.fit(data,truth)

print(clf.score(data,truth))

output=open("svm-gauss.pkl",'wb')

pickle.dump(clf,output)

output.close()
