# esercizio 1

def positive_number():
    negativo = True
    while negativo: # Fino a quando l'utente inserisci numeri negativi, chiedi di inserire un nuovo numero, dando un seggerimento
        n = int(input("Inserisci un numero: "))
        if n <= 0:
            print("Prova un numero positivo")
        else: # Se inserisce un numero positivo, esce dal while loop
            print(f"{n} è un numero valido")
            negativo = False

# esercizio 2
import random

def create_list():
    l = int(input("Determina la lunghezza della lista da creare:")) # richiede all'untente lunghezza della lista
    lista = []
    for i in range(l): 
        n = random.randint(1, l) # genera un numero random compreso tra 1 e l
        lista.append(n)          # aggiunge il numero alla lista
    
    print(lista)    
    return lista

# esercizio 3
def somma_elementi_pari(funzione):
    def wrapper():
        lista = funzione()          # genera una lista con la funzione 
        somma = 0                   # inizializza la somma a 0
        for n in lista:
            if n % 2 == 0:          # verifica che ogni numero nella lista sia pari     
                somma += n          # se pari lo aggiunge alla somma
        print(f"Somma numeri pari : {somma}")
    return wrapper

# esercizio 4

def stampa_elementi_dispari(funzione):
    def wrapper():
        lista = funzione()         # genera una lista con la funzione        
        for n in lista:            # per ogni numero della lista
            if n%2 !=0:            # verifica che sia dispari
                print(n)           # lo stampa
    return wrapper 


# Esercizio 5
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


def vero_falso_primi(funzione):
    def wrapper():
        l = funzione()              # genera una lista con la funzione 
        lista = []
        for n in l:                 # per ogni numero della lista
            if is_prime(n):         # verifica che sia primo
                lista.append(True)  # se primo aggiunge True alla nuova lista
            else:
                lista.append(False) # se non è primo aggiunge Falso alla nuova lista
        print(lista)
    return wrapper


# esercizio 6

def stampa_elementi_primi(funzione):
    def wrapper():
        lista = funzione()                      # genera una lista con la funzione 
        for n in lista:                         # per ogni numero della lista
            if is_prime(n):                     # verifica che ogni elemento della lista sia primo
                print(f"{n} è un numero primo") # se primo lo stampa
            else:
                pass
    return wrapper 

# Esercizio 7

def sum_is_prime(funzione):
    def wrapper():
        lista = funzione()                                          # per ogni numero della lista
        somma = 0                                                   # inizializza la somma a 0
        for n in lista:
            somma += n                                              # crea la somma degli elementi contenuti nella lista
        if is_prime(somma):                                         # verifica che sia un numero primo
            print(f"La somma è {somma}, ed è un numero primo")     
        else:
            print(f"La somma è {somma}, ma non è un numero primo")
    return wrapper
    




somma_pari = somma_elementi_pari(create_list)

stampa_dispari = stampa_elementi_dispari(create_list)

lista_primi = vero_falso_primi(create_list)

numeri_primi = stampa_elementi_primi(create_list)

somma_is_prime = sum_is_prime(create_list)

# Esercizio comompleto con menù

continuare = True

while continuare:
    esercizio = int(input("Quale esercizio vuoi scegliare? (Da 1 a 7)"))
    match esercizio:
        case 1:
            print("Verifica numero positivo")
            positive_number()
            # Far scegliere all'utente se continuare o meno
            scelta = input("Vuoi continuare ? si/no ")
            if scelta == "no":
                continuare = False
                print("Esercizio finito")
        case 2:
            print("Creazione lista di lunghezza determinata dall'utente")
            create_list()
            # Far scegliere all'utente se continuare o meno
            scelta = input("Vuoi continuare ? si/no ")
            if scelta == "no":
                continuare = False
                print("Esercizio finito")        
        case 3:
            print("Determina la somma dei numeri pari inclusi in una lista di lunghezza determinata dall'utente")
            somma_pari()
            # Far scegliere all'utente se continuare o meno
            scelta = input("Vuoi continuare ? si/no ")
            if scelta == "no":
                continuare = False
                print("Esercizio finito")        
        case 4:
            print("Stampa i numeri dispari inclusi in una lista di lunghezza determinata dall'utente")
            stampa_dispari()
            # Far scegliere all'utente se continuare o meno
            scelta = input("Vuoi continuare ? si/no ")
            if scelta == "no":
                continuare = False
                print("Esercizio finito")        
        case 5:
            print("Restituisce una lista di True / False a seconda del fatto che i numeri presenti in una lista di lunghezza determinata dall'utente siano primi o meno")
            lista_primi()
            # Far scegliere all'utente se continuare o meno
            scelta = input("Vuoi continuare ? si/no ")
            if scelta == "no":
                continuare = False
                print("Esercizio finito")        
        case 6:
            print("Stampa i numeri primi inclusi in una lista di lunghezza determinata dall'utente")
            numeri_primi()
            # Far scegliere all'utente se continuare o meno
            scelta = input("Vuoi continuare ? si/no ")
            if scelta == "no":
                continuare = False
                print("Esercizio finito")        
        case 7:
            print("Determina se la somma dei numeri inclusi in una lista di lunghezza determinata dall'utente sia un numero primo o meno")
            somma_is_prime()
            # Far scegliere all'utente se continuare o meno
            scelta = input("Vuoi continuare ? si/no ")
            if scelta == "no":
                continuare = False
                print("Esercizio finito")        
        case _:
            break
