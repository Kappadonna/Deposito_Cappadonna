import numpy as np

zero = np.zeros((3, 4))

print(zero)

print(zero.shape)

arr = np.arange(10)   # [0,1,2,...,9]
print(arr[2:7:2])

sd = np.std(arr)
print(sd)

normal = np.random.normal(2000, 500, 365)
print(normal.shape)
print(normal.mean())
print(normal.std())


arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)

arr = np.array([1, 2, 3])
print(arr.shape)

arr = np.array([[1],[2],[3]])
print(arr.shape)