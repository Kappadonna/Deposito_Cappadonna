# somma

def somma():
    print("Hai selezionato somma.")
    numeri = []
    somma = 0
    q = int(input("Quanti numeri vuoi sommare tra loro? "))
    for i in range(q):
        n = int(input("Seleziona un numero da inserire nella somma: "))
        numeri.append(n)
    for i in numeri:
        somma += i
        res = (somma, numeri)
    return res


# sottrazione

def sottrazione():
    print("Hai selezionato sottrazione.")
    numeri = []
    sottrazione = 0
    q = int(input("Quanti numeri vuoi sottrarre tra loro? "))
    for i in range(q):
        n = int(input("Seleziona un numero da inserire nella sottrazione: "))
        numeri.append(n)
        if i == 0:
            sottrazione = n
        else:
            sottrazione -= n
    res = (sottrazione, numeri)
    return res
        
        
res = sottrazione()
print(res)

# moltiplicazione

def moltiplicazione():
    print("Hai selezionato moltiplicazione.")
    numeri = []
    prodotto = 1
    q = int(input("Quanti numeri vuoi moltiplicare tra loro? "))
    for i in range(q):
        n = int(input("Seleziona un numero da inserire nella moltiplicazione: "))
        numeri.append(n)
    for i in numeri:
        prodotto *= i
    res = (prodotto, numeri)
    return res

res = moltiplicazione()
print(res)

# divisione

def divisione():
    print("Hai selezionato divisione.")
    numeri = []
    n1 = int(input("Inserisci il primo numero: "))
    numeri.append(n1)
    while True:
        n2 = int(input("Inserisci il secondo numero: "))
        if n2 == 0:
            print("Non puoi dividere per 0, riprova.")
        else:
            numeri.append(n2)
            break
    
    divisione = numeri[0] / numeri[1]
    res =(divisione, numeri)
    return res

res = divisione()
print(res)   
        
# divisione intera

def divisione_intera():
    print("Hai selezionato divisione_intera.")
    numeri = []
    n1 = int(input("Inserisci il primo numero: "))
    numeri.append(n1)
    while True:
        n2 = int(input("Inserisci il secondo numero: "))
        if n2 == 0:
            print("Non puoi dividere per 0, riprova.")
        else:
            numeri.append(n2)
            break
    
    divisione_intera = numeri[0] // numeri[1]
    res = (divisione_intera, numeri)
    return res

res = divisione_intera()
print(res)
        
    