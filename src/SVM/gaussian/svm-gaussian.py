#!/usr/bin/env python

from sklearn.svm import SVC
import numpy as np
import pickle
import sys

if len(sys.argv) > 2:
    data = np.load("/farmshare/user_data/kurinsky/CS229-Project/src/sd.npy")
    truth = np.load("/farmshare/user_data/kurinsky/CS229-Project/src/truth.npy")
    
    C=float(sys.argv[1])
    gamma=float(sys.argv[2])
    print "C = "+str(C)
    print "Gamma = "+str(gamma)
    
    clf = SVC(class_weight="auto",kernel="rbf",verbose=False,cache_size=2000, shrinking=False, C=C, gamma=gamma)
    print(clf.fit(data, truth))
    print(clf.score(data,truth))
    
    output=open("svm-c"+str(C)+"-g"+str(gamma)+".pkl",'wb')
    pickle.dump(clf,output)
    output.close()
    
    testdata = np.load("/farmshare/user_data/kurinsky/CS229-Project/src/sd_test.npy")
    testtruth = np.load("/farmshare/user_data/kurinsky/CS229-Project/src/truth_test.npy")
    
    print(clf.score(testdata,testtruth))
    
    s = np.where(truth == 2)[0]
    st = np.where(testtruth == 2)[0]
    g = np.where(truth == 1)[0]
    gt = np.where(testtruth == 1)[0]
    print("Stars")
    print(clf.score(data[s],truth[s]))
    print(clf.score(testdata[st],testtruth[st]))
    print("Galaxies")
    print(clf.score(data[g],truth[g]))
    print(clf.score(testdata[gt],testtruth[gt]))
else:
    print("Enter svm-gaussian C gamma")
