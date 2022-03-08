import numpy as np


a = np.array([
    [1, 6],
    [2, 8],
    [3, 11],
    [3, 10],
    [1, 7]
])

a_centered = np.subtract(a, np.mean(a, axis=0))
a_centered_transpose = a_centered.transpose()
a_centered_sp = np.dot(a_centered_transpose[0], a_centered_transpose[1])
print(a_centered_sp / (a_centered.shape[0] - 1))
