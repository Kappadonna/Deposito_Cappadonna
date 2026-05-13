import numpy as np

arr = np.array([1, 2, 3])

arr2d = np.array([[1, 2, 3], [4, 5, 6]])

print("array unidimensionale")
print(arr)
print("\n array bidimensionale")
print(arr2d)

zeroarr = np.zeros((5, 5))

onearr = np.ones((2, 3))

print("\nzero array")
print(zeroarr)
print("\none array")
print(onearr)

print("\n shape dell'array unidimensionale")
print(arr.shape)
print("\n shappe dell'array bidimsnionale")
print(arr2d.shape)

print("\ndimensioni dell'array composto da zeri")
print(zeroarr.ndim)

print("\n numero totale di elementi dell'array composto da solo 1")
print(onearr.size)

print("\n dtype dell'array bidimensionale")
print(arr2d.dtype)
print("\n dtype dell'array di zeri")
print(zeroarr.dtype)

print("\n somma dei valore dell'array bidimensionale")
print(arr2d.sum())
print("\n somma dei valore dell'array unidimensionale")
print(arr.sum())


print("\nmedia dell'array bidimsnioanle")
print(arr2d.mean())
print("\nmedia dell'array unidimensionale")
print(arr.mean())


print("\n array unidimensionale, max e min")
print("max: " + str(arr.max()) + " - i: " + str(arr.argmax()))
print("min: " + str(arr.min()) + " - i: " + str(arr.argmin()))
print("\n array bidimensionale, max e min")
print("max: " + str(arr2d.max()) + " - i: " + str(arr2d.argmax()))
print("min: " + str(arr2d.min()) + " - i: " + str(arr2d.argmin()))
print("\n array di zeri, max e min")
print("max: " + str(zeroarr.max()) + " - i: " + str(zeroarr.argmax()))
print("min: " + str(zeroarr.min()) + " - i: " + str(zeroarr.argmin()))

rangearr = np.arange(10, 50)
print("\narray arange")
print(rangearr)

reshape_rangearr = rangearr.reshape((10, 4))
print("\n array reshaped")
print(reshape_rangearr)

array_interi = np.arange(10, 50)
print("\n Arrai con numeri interi")
print(array_interi)
print(array_interi.dtype)
array_float = array_interi.astype("float64")
print("\n Arrai con numeri decimali")
print(array_float)
print(array_float.dtype)


# indexing e slicing

arr = np.arange(1, 7)
print("\n array originale")
print(arr)
print("\n primo elemento dell'array")
print(arr[0])
print("\n secondo e terzo elemento dell'array")
print(arr[1:3])
print("\n elementi dell'array maggiori di 2")
print(arr[arr>2])


arr2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print("\narray bidimensionale")
print(arr2d)
print("\nseconda e terza riga dell'array bidimensioanle")
print(arr2d[1:3])
print("\nseconda e terza colonna dell'array bidimensionale")
print(arr2d[:, 1:3])

# funzioni

arr = np.linspace(0, 1, 5)
print(arr)
arr2, step = np.linspace(0, 10, 100, endpoint= False, retstep=True)
print("Array: ",arr2)
print("Step: ", step)

print("\n")
random_arr = np.random.rand(3, 3)
print(random_arr)
print("\n")
random_2 = np.random.randint(10, 100, (5, 5))
print(random_2)

print("\n")
print(np.random.choice(arr2, size = 6))
print("\n")
print(np.random.choice(np.random.randint(1, 100, 50), size = 6))


print("Somma", random_2.sum())
print("Deviazione standard", random_2.std())
print("Varianza", random_2.var())