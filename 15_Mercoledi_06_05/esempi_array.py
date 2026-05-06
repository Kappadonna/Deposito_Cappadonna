import numpy as np

arr = np.array([32, 41, 51, 45, 93])

# Indexing
print(arr[0])

# Sclicing
print(arr[1:3])

# Boolean indexing
print(arr[arr>42])

print(" Array multidimensionale")
arr_2d = np.array([[23, 41, 51], 
                   [45, 55, 62],
                   [23, 52, 11]])

# Slicing sulle righe
print(arr_2d[1:3])

# Slicing sulle colonne
print(arr_2d [:, 1:3])

# Slicing misto
print(arr_2d[1:3, 1:3])


# Slicing

arr = np.arange(10)

print(arr)

print(arr[2:7])

print(arr[1:8:2])

print(arr[:5])
print(arr[5:])

print(arr[-5:])
print(arr[:-5])

# Fancy indexing

arr = np.array([10, 20, 30, 40, 50])

# Utilizzando un array di indici
indeces = np.array([1, 3])
print(arr[indeces])

# Utilizzando una lista di indici
indeces = [0, 2, 4]
print(arr[indeces])