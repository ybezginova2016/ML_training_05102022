#SciPy Lecture Notes https://scipy-lectures.org/

# With scipy.sparse we can get sparse matrices.
# Sparse matrices  are used when we want to save 2D array with zeros.
import numpy as np
from scipy import sparse

# Creating 2D array NumPy with 1s in main diaginak and 0s in other cells.
eye = np.eye(4)
print("NumPy array: \n{}".format(eye))

# NumPy --> SciPy (into sparse matrice) in CSR format
# Saving inly non-zero elements

sparse_matrix = sparse.csr_matrix(eye)
print("\nSciPy in CSR format: \n{}".format(sparse_matrix))

# Creating SciPy sparse matrix in COO format:
data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)

eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print("\nCOO format:\n{}".format(eye_coo))
