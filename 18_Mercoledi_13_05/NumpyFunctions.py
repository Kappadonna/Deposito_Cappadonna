import numpy as np

dati = np.array([2, 4, 6, 8, 10])
print("Media: ", np.mean(dati))
print("Mediana", np.median(dati))
print("Std: ", np.std(dati))
print("Var: ", np.var(dati))


valori = np.array([0, 1, 2])
print("esp: ", np.exp(valori))
print("log: ", np.log(valori))

angoli = np.array([0, np.pi/2, np.pi])
print("Seno: ", np.sin(angoli))
print("Coseno: ", np.cos(angoli))
print("Tangente: ", np.tan(angoli))

matrice_1 = np.array([[1, 2], [3, 4]])
matrice_2 = np.array([[5, 6], [7, 8]])

print("Prodotto mat dot: ", np.dot(matrice_1, matrice_2))
print("Prodotto mat matmul: ", np.matmul(matrice_1, matrice_2))

print("Determinante : ", np.linalg.det(matrice_1))
print("Inversa :", np.linalg.inv(matrice_1))