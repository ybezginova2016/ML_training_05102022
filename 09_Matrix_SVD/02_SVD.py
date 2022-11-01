import numpy as np
from scipy.linalg import svd
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)
# Perform the decomposition.
U, s, VT = svd(A)
print("\nU\n", U)
print("\ns\n", s)
print("\nVT\n", VT)
# Create the m x n Sigma matrix.
Sigma = np.diag(s)
Sigma = np.zeros((A.shape[0], A.shape[1]))
Sigma[:A.shape[1], :A.shape[1]] = np.diag(s)
print("\nSigma matrix\n", Sigma)
# Reconstruct the original matrix.
B = U.dot(Sigma.dot(VT))
print("\nReconstructed matrix\n", B)
print()
