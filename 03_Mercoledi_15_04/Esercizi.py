# Esercizio 1

contare = True

while contare:
    numero = int(input("Scegli un numero da 1 a 10:"))

    print("Conto alla rovescia in corso")
    for i in range(numero, -1, -1):   
        print(i)
        numero -=1
    continuare = input("Vuoi provare con un altro numero? ").lower()
    match continuare:
        case "no":
            contare = False
        case "si":
            pass
        case _:
            print("Risposta non valida, esco dal loop")
            contare = False
           
        
# Esercizio 2

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Controlla i divisori fino alla radice quadrata di n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True



numeri_primi = []
while len(numeri_primi) < 5:
    numero = int(input("Inserisci un numero: "))
    if is_prime(numero) == True:
        print(f"{numero} è un numero primo!")
        numeri_primi.append(numero)
    else:
        print(f"{numero} non è un numero primo")
        
print(numeri_primi)
