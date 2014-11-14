from varplot import *
from sklearn.svm import LinearSVC
import numpy as np
import pickle

#inpfile="/Users/noah/Documents/Class Repositories/data/round1Standardized.fits"

data = np.load("sd.npy")
truth = np.load("truth.npy")

print(len(data))

"""
data = getTable(inpfile)
tdat = getTruth(inpfile)

print(len(data["fwhm_world_g"]))
print(len(tdat["truth"]))

#number of training examples
m = len(tdat["truth"])

#number of features in the above list
n = len(data.columns.names)

standardized_data = [[0.0 for i in range(0, n)] for j in range(0, m)]
for i in range(0,n):
    print(i)
    for j in range(0,m):
        standardized_data[j][i] = data[data.columns.names[i]][j]

np.save("sd.npy", np.array(standardized_data))
"""

clf = LinearSVC()
clf.fit(data,truth)

print(clf.score(data,truth))

output=open("data.pkl",'wb')

pickle.dump(clf,output)

output.close()
