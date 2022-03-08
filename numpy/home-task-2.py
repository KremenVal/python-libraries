import numpy as np


a = np.array([
    [1, 6],
    [2, 8],
    [3, 11],
    [3, 10],
    [1, 7]
])

a_centered = np.subtract(a, np.mean(a, axis=0))
print(a_centered)
