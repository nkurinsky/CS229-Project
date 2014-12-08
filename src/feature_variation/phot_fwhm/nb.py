from varplot import *
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import pickle
from freqhist import *

data = np.load("sd.npy")
testdata = np.load("sd_test.npy")
truth = np.load("truth.npy")

for i in range(0,len(data[1,:])):
    print(i)
    bins = freqbins(data[:,i],nbins=3)
    for j in range(0,len(data[:,i])):
        data[j,i]= binnum(data[j,i],bins)
    for j in range(0,len(testdata[:,i])):
        testdata[j,i]= binnum(testdata[j,i],bins)

np.save("sd_nb.npy",data)
np.save("sd_test_nb.npy",testdata)

print(data[:,1])
clf = MultinomialNB()
clf.fit(data,truth)

print(clf.score(data,truth))

output=open("nb.pkl",'wb')

pickle.dump(clf,output)

output.close()
