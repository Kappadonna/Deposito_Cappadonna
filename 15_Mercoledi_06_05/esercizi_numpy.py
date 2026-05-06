import numpy as np

array = np.arange(10, 50)

print("Tipo di dati dell'array", array.dtype)

array_float = array.astype(float)

print("Tipo di dati dell'array", array_float.dtype)

print("Froma dell'array: ", array_float.shape)

print(array)

# Metodo numpy: 40 righe, salva un elemento per riga
np.savetxt("15_Mercoledi_06_05/dati.csv", array_float, delimiter=",")

# Metodo numpy: 40 colonne, salva tutto sulla stessa riga
np.savetxt("15_Mercoledi_06_05/dati.csv", [array_float], delimiter=",")

# Con funzione open
with open("15_Mercoledi_06_05/dati.csv", "w", encoding="utf-8") as file:
    for valore in array:
        file.write(f"{valore}\n") # write accetta solo stringhe
