from varplot import *
import sklearn
import numpy as np

inpfile="/Users/noah/Documents/Class Repositories/data/round1Standardized.fits"

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
