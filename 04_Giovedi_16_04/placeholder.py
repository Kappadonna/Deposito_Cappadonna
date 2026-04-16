# esercizio 2
import random

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
    

""" def print_dispari(funzione):
    def wrapper():
        lista = funzione()
        
        for n in lista:
            if n%2 !=0:
                print(n)
    return wrapper  """  
            

""" def print_primi(funzione):
    def wrapper():
        lista = funzione()
        for n in lista:
            if is_prime(n):
                print(f"{n} è un numero primo")
            else:
                pass
    return wrapper            





lista_primi = print_primi(create_list)
lista_primi() """


""" def true_primi(funzione):
    def wrapper():
        l = funzione()
        lista = []
        for n in l:
            if is_prime(n):
                lista.append(True)
            else:
                lista.append(False)
        print(lista)
    return wrapper """

def create_list():
    l = int(input("Determina la lunghezza della lista da creare:"))
    lista = []
    for i in range(l):
        n = random.randint(1, l)
        lista.append(n)
    
    print(lista)    
    return lista


def sum_is_prime(funzione):
    def wrapper():
        lista = funzione()
        somma = 0
        for n in lista:
            somma += n
        if is_prime(somma):
            print(f"La somma è {somma}, ed è un numero primo")
        else:
            print(f"La somma è {somma}, ma non è un numero primo")
    return wrapper
    
somma_is_prime = sum_is_prime(create_list)
somma_is_prime()