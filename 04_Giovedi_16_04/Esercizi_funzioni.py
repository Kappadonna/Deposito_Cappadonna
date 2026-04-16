# Indovina il numero

import random

def generate_number():
    n = random.randint(1, 100)
    return n

def guess_number(numero):
    guessed = False
    while not guessed:
        n = int(input("Indovina il numero (o invia senza scrivere nulla per uscire): "))
        if n == numero:
            print("You guessed right! Congratulations")
            guessed = True
        elif n < numero:
            print("Try an higher number")
        elif n > numero:
            print("Try a lower number")
        else:
            break
        
# n = generate_number()
# print(n)
# guess_number(n)

# Sequenza di fibonacci fino a N

def fibonacci(numero):
    a = 0
    b = 1
    fib_list = [a, b]
    for i in range (numero):
        c = a + b
        # Impostare nuovi valori da a e b
        a = b
        b = c
        if c < numero:
            fib_list.append(c)
    return fib_list   

# n = int(input("Inserisci un numero"))
# print(fibonacci(n))


""" esercizio = int(input("Quale esercizio vuoi svolgere? 1 | 2"))
match esercizio:
    case 1:
        n = generate_number()
        print(n)
        guess_number(n)
            
    case 2:
        n = int(input("Inserisci un numero"))
        print(fibonacci(n))
    case _:
        print("Scelta non valida") """

   
continuare = True
while continuare:     
    esercizio = int(input("Quale esercizio vuoi svolgere? 1 | 2 | "))
    match esercizio:
        case 1:
            n = generate_number()
            print(n)
            guess_number(n)
            
            # Far scegliere all'utente se continuare o meno
            scelta = input("Vuoi continuare ? si/no")
            if scelta == "no":
                continuare = False
                print("Esercizio finito")
            else:
                continue    
        case 2:
            n = int(input("Inserisci un numero"))
            print(fibonacci(n))
            
            # Far scegliere all'utente se continuare o meno
            scelta = input("Vuoi continuare ? si/no")
            if scelta == "no":
                continuare = False
                print("Esercizio finito")
            else:
                continue  
            
        case _:
            print("Scelta non valida")
            continuare = False