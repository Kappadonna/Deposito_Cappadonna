import numpy as np

array_interi = np.arange(10, 50)

print(array_interi.dtype)


array_float = array_interi.astype("float64")

print(array_float.dtype)



# pag 219

import numpy as np

# Numpy array 1D con numeri random tra 10 e 50
np.random.seed(123)
a = np.random.randint(10, 51, 20)

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


# pag 220

matrice = np.random.randint(1, 101, (6, 6))
print("\n Matrice 6x6 con numeri random da 1 a 100 (inclusi)")
print(matrice)

m_2 = matrice[1:5, 1:5]
print("\n Matrice 4x4 estratta dalla matrice originale")
print(m_2)

m_3 = np.flipud(m_2)
print("\n Matrice 4x4 invertita")
print(m_3)

print("\n Metodo alternativo")
m3 = m_2[::-1]
print(m3)

m_4 = np.diag(m_3)
print("\n Matrice 1D con numeri estratti dalla diagonale principale")
print(m_4)

m_5 = np.where(m_4 % 3 == 0, -1, m_4)
print("\n Matrice 1D con numeri multipli di 3 impostati a -1")
print(m_5)

print("\n Metodo alternativo")
m5 = m_4.copy()
m5[m5 % 3 == 0 ] = -1
print(m5)


# pag 226
print("-" * 30)
print("Esercizi pagine 226")
print("-" * 30)

print("\nArray con 12 elementi equidistanti tra 0 e 1")
arr, step = np.linspace(start=0, stop=1, num=12, retstep= True)
print(arr, step)

print("\nModifica shape in un 3x4")
arr_2 = arr.reshape((3, 4))
print(arr_2)

print("\nMatrice 3x4 con numer random tra 0 e 1")
arr_3 = np.random.rand(3, 4)
print(arr_3)

print("\nSomma array 2: ", arr_2.sum())

print("\nSomma array 3: ", arr_3.sum())

# pag 227

print("-" * 30)
print("Esercizi pagine 227")
print("-" * 30)


print("\n Array con 50 numeri equidistanti tra 0 e 10")
arr, step = np.linspace(start = 0, stop = 10, num = 50, retstep= True)
print(arr, step)

print("\n Array con 50 numeri casuali tra 0 e 10")
arr_2 = np.random.rand(50)
print(arr_2)

print("\n Array dato dalla somma dei due array precedenti")
arr_3 = arr + arr_2
print(arr_3)

print("\n valore dato dalla somma degli elementi maggiore di 5 dell'array precedente")
arr_4 = arr_3.copy()
arr_4 = arr_4[arr_4 > 5].sum()
print(arr_4)


def write_file(esercizio, array):
    
    azione = input("Che azione vuoi svolgere? Selezione a per aggiungere l'array al file, w per sovrascrivere l'intero file: [a, w] ").lower()
    if azione in ["a", "w"]:
        with open("numpy_arrays.txt", azione) as file:
            file.write(f"\nArray {esercizio}:\n")
            file.write(f"{array}")
        print(f"Array {esercizio} aggiunto con successo")
                
    else:
        raise ValueError("Valore non valido")
    
def main():
    print("-" * 30)
    print("Benvenuto nel creatore di array")
    print("-" * 30)
    while True:
        print("\nSeleziona il tipo di array da creare")
        print("\n1 -> Array con 12 elementi equidistanti tra 0 e 1")
        print("\n2 -> Array con 50 numeri casuali tra 0 e 10")
        print("\n3 -> Array dato dalla somma dei due array precedenti")
        print("\n4 -> Valore dato dalla somma degli elementi maggiore di 5 dell'array precedente")
        selezione = input("\n[ 1, 2, 3, 4] :")
        match selezione:
            case "1":
                print("\n Array con 50 numeri equidistanti tra 0 e 10")
                arr, step = np.linspace(start = 0, stop = 10, num = 50, retstep= True)
                print(arr, step)
                write_file(1, arr)
            case "2":
                print("\n Array con 50 numeri casuali tra 0 e 10")
                arr_2 = np.random.rand(50)
                print(arr_2)
                write_file(2, arr_2)
            case "3":
                print("\n Array dato dalla somma dei due array precedenti")
                arr = np.linspace(start = 0, stop = 10, num = 50)
                arr_2 = np.random.rand(50)
                arr_3 = arr + arr_2
                print(arr_3)
                write_file(3, arr_3)
            case "4":
                print("\n Array dato dalla somma dei due array precedenti")
                arr= np.linspace(start = 0, stop = 10, num = 50)
                arr_2 = np.random.rand(50)
                arr_3 = arr + arr_2
                arr_4 = arr_3.copy()
                arr_4 = arr_4[arr_4 > 5].sum()
                print(arr_4)
                write_file(4, arr_4)
            case "*":
                break
            case _:
                print("\nScelta non valida")
            

if __name__ == "__main__":
    main()