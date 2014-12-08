import numpy as np
import pickle
from random import randrange, choice
from sklearn.neighbors import NearestNeighbors

data = np.load("sd.npy")
truth = np.load("truth.npy")

stars = data[np.where(truth == 2)[0]]
galaxies = data[np.where(truth == 1)[0]]

# number of features
n = data.shape[1]

# number of stars
T = stars.shape[0]

# amount of synthetic oversampling
N = 500

# number of nearest neighbors
k = 5

N = N/100

n_synthetic_samples = N * T

S = np.zeros(shape=(n_synthetic_samples, n))

neigh = NearestNeighbors(n_neighbors = k)
neigh.fit(stars)

for i in range(T):
    nn = neigh.kneighbors(stars[i], return_distance = False)
    for m in range(N):
        nn_index = choice(nn[0])
        
        # nn includes T[i] itself, we want a neighbor
        while nn_index == i:
            nn_index = choice(nn[0])
            
        diff = stars[nn_index] - stars[i]
        distance_along_diff_vector = np.random.uniform(low = 0.0, high = 1.0)
        S[m + i*N, :] = stars[i,:] + distance_along_diff_vector * diff[:]
        
newdata = np.concatenate((data, S))
newtruth = np.concatenate((truth, 2*np.ones(n_synthetic_samples)))

np.save("sd_smote.npy", np.array(newdata))
np.save("truth_smote.npy", np.array(newtruth))