matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

riga = matrice[0]
print(riga)

elemento = matrice[0][1]
print(elemento)

for riga in matrice:
    for elemento in riga:
        print(elemento)
        
        