from sklearn.svm import SVC
import numpy as np
import pickle
from sklearn.cross_validation import StratifiedKFold
from sklearn.grid_search import GridSearchCV

data = np.load("../sd.npy")
truth = np.load("../truth.npy")

print(len(data))

gamma_range = 10.0 ** np.arange(-5, 5)
r_range= np.arange(-2.0,2.0)
param_grid = dict(gamma=gamma_range,coef0=r_range)
cv = StratifiedKFold(y=truth, n_folds=3)
clf = GridSearchCV(SVC(class_weight="auto",kernel="sigmoid",verbose=True,cache_size=1000), param_grid=param_grid, cv=cv, verbose=10)
clf.fit(data, truth)

print(clf.score(data,truth))

output=open("svm-sigmoid.pkl",'wb')
pickle.dump(clf,output)
output.close()
