# print("numpy example test")
import numpy as np

# a = np.array([2, 3, 4])
# print(a)

# print(a.dtype)
# b = np.array([1.2, 3.5, 5.1])
# print(b.dtype)

# c = np.array([[1, 2], [3, 4]])
# print(c)

# zeros = np.zeros((3, 4))
# print(zeros)
# ones = np.ones((2, 3), dtype=np.int16)
# print(ones)
# empty = np.empty((2, 3))
# print(empty)

# x = np.arange(10, 30, 5)
# print(x)
# y = np.linspace(0, 2, 9)
# print(y)

# x = np.linspace(0, 2 * np.pi, 100)
# print(x)

# print()
# print()
# print()

# y = np.sin(x)
# print(y)

# a = np.array([20, 30, 40, 50])
# print(a)

# b = np.arange(4)
# print(b)
# n = a - b
# print(n)
# b ** 2
# 10 * np.sin(a)

scores = np.array([
[55, 62, 71, 68],
[78, 85, 88, 90],
[45, 50, 48, 52],
[90, 92, 94, 96],
[60, 65, 70, 75]
])

# Shape of the arrar
s = scores
print(s.shape)

n = s.itemsize
print(n)

total = sum(s)
print(total)

