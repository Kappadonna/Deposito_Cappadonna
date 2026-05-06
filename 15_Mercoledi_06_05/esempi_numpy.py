import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [3, 5, 1, 7, 2]])

arr2d = np.array([[1, 2, 3], [3, 4, 5]])

print("Forma dell'array: ", arr.shape) # (2, 5)
print("Dimensioni dell'array: ", arr.ndim) # 2
print("Tipo di dati: ", arr.dtype) # int64
print("Numero degli elementi: ", arr.size) # 10
print("Somma degli elementi: ", arr.sum()) #33
print("Media degli elementi: ", arr.mean()) # 3.3
print("Valore massimo: ", arr.max()) # 7
print("Indice del valore: ", arr.argmax()) # 8 (0 indexed)

# specificare tipo dei dati
arr_1d= np.array([1, 5, 4], dtype = 'int32')
print(arr_1d.dtype)

arr_arange = np.arange(6)
print(arr_arange)
reshaped_arr = arr_arange.reshape((2, 3))
print(reshaped_arr)