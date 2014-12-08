from sklearn.svm import SVC
import numpy as np
import pickle
from sklearn.cross_validation import StratifiedKFold
from sklearn.grid_search import GridSearchCV

data = np.load("../sd.npy")
truth = np.load("../truth.npy")

print(len(data))

clf = SVC(class_weight="auto",kernel="linear",verbose=True,cache_size=1000)
clf.fit(data, truth)

print(clf.score(data,truth))

output=open("svm-linear.pkl",'wb')
pickle.dump(clf,output)
output.close()
