""" # Funzioni

def saluta(nome):
    print("Hello, ", nome)
    
saluta("Gianluca")

def somma(a, b):
    res = a + b
    print("La somma è:", res)
    
somma(4312, 41)

def quadrato(numero):
    return numero * numero

res = quadrato(4)
print(res)

res2 = somma(3, 5)

print(res2) # Restituisce None se si prova a printare una funzione che non ha return

def saluta2(nome:str, messaggio = "Ciao"):
    print(f"{messaggio} {nome}")
    
saluta2("Mario")
saluta2("Luigi", messaggio = "Buongiorno")


# Generatori

def fibonacci(n):
    a, b = 0, 1
    
    while a < n:
        yield a
        a, b = b, a+b
        

l = list(fibonacci(20))
print(l)

for x in fibonacci(20):
    print(x) """
    
# Decoratori

def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione della funzione")
        funzione()
        print("Dopo l'esecuzione della funzione")
    return wrapper

@decoratore
def saluta():
    print("Ciao Gianluca")

saluta()