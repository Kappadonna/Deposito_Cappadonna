import numpy as np
import csv

# Numpy array 1D con numeri random tra 10 e 50
np.random.seed(123)
a = np.random.randint(10, 50, 20)

print(a)
print(a.shape)
print(a.dtype)

# Primi 10 elementi dell'array (0 ->9)
print("Primi 10 elementi dell'array (0 ->9)")
a_2 = a[:10]
print(a_2)

# Ultimi 5 elementi dell'array
print("Ultimi 5 elementi dell'array")
a_3 = a[-5:]
print(a_3)

# Elementi compresi tra indice 5 incluso e 15 escluso
print("Elementi compresi tra indice 5 incluso e 15 escluso")
a_4 = a[5:15]
print(a_4)

# Array con elementi con indice multiplo di tre
print("Array con elementi con indice multiplo di tre")
a_5 = a[2::3]
print(a_5)

# Array originale con valori = 99 per elementi con indice tra 5 incluso e 10 escluso
print("Array originale con valori = 99 per elementi con indice tra 5 incluso e 10 escluso")
a_6 = a.copy()
a_6[5:10] = 99
print(a_6)


# Creazione file csv
with open("15_Mercoledi_06_05/slicing_array.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["a"] + list(a))
    writer.writerow(["a_2"] + list(a_2))
    writer.writerow(["a_3"] + list(a_3))
    writer.writerow(["a_4"] + list(a_4))
    writer.writerow(["a_5"] + list(a_5))
    writer.writerow(["a_6"] + list(a_6))
    

# Lista di array su cui iterare        
arrays = [a, a_2, a_3, a_4, a_5, a_6]

with open("15_Mercoledi_06_05/slicing_array.txt", "w", encoding="utf-8") as file:
    for i, array in enumerate(arrays):
        file.write(f"Array {i}: ")
        file.write(",".join(map(str, array)))
        file.write("\n")