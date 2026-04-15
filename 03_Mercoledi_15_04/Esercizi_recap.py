# Ciclo while
switch = True
sum = 0
while switch:
    numero = int(input("Inserici un numero: "))
    sum += numero
    if numero == 0:
        switch = False

print((f"La somma dei numeri inseriti è {sum}")) 
    

# Ciclo for 
parola = input("Inserisci una parola")

for c in parola:
    print(f"{c}") 
        

# Ciclo Range
numero = int(input("Scegli un numero: "))
passo = int(input("Scegli uno step: "))

for i in range(0, numero, passo):
    print(i)
    
# ---------------------------
# Esercizio completo slide 79
# ---------------------------

# Creare menu per scegliere esercizio
switch = True


while switch:
    scelta = int(input("Quale esercizio vuoi svolgere?\n 1 | 2 | 3 | 4 |"))
    match scelta:
        case 1:
            # Prendere input dell'utente e verificare che sia pari o dispari
            numero = int(input("Scegli un numero: "))
            if numero % 2 == 0:
                print(f"{numero}  pari")
            else:
                print(f"{numero} è dispari")
                
            # Chiede all'utente se vuole continuare con un altro esercizio                  
            continuare = input("Vuoi fare un altro esercizio?").lower()
            if continuare == "no":
                switch = False
                print("\nEsercitazione finita")                 
        case 2:
            
            # Prendere input dall'utente ed effettuare conto alla rovescia
            numero = int(input("Scegli un numero: "))
            for i in range(numero, -1, -1):
                print(i)
                
            # Chiede all'utente se vuole continuare con un altro esercizio                  
            continuare = input("Vuoi fare un altro esercizio?").lower()
            if continuare == "no":
                switch = False
                print("\nEsercitazione finita")                             
        case 3:
            lista = []
            
            # Richiedo all'utento di compilare la lista
            quantita = int(input("Quanti numeri vuoi aggiungere alla lista? "))
            for i in range(quantita):
                n = int(input("Quale numero vuoi aggiungere alla lista? "))
                lista.append(n)
            print(lista)
            
            print(f"Eseguo il quadrato dei seguenti numeri {lista}")
            for n in lista:
                print(n**2)
 
            # Chiede all'utente se vuole continuare con un altro esercizio                  
            continuare = input("Vuoi fare un altro esercizio?").lower()
            if continuare == "no":
                switch = False
                print("\nEsercitazione finita")                              
        case 4:
            
            # Inizializzo lista vuota
            lista = []
            
            # Richiedo all'utento di compilare la lista
            quantita = int(input("Quanti numeri vuoi aggiungere alla lista? "))
            for i in range(quantita):
                n = int(input("Quale numero vuoi aggiungere alla lista? "))
                lista.append(n)
            print(lista)
            
            # Se la lista è vuota, informa l'utente, altrimenti stampa massimo e numero di elementi
            if len(lista) == 0:
                print("Lista vuota")
            else:
             
            # Check per stampare numero massimo della lista    
                n_max = lista[0]
                for n in lista:
                    if n > n_max:
                        n_max = n                
                print(f"Il numero più grande della lista è {n_max}")   
                
            # Check per contare il numero di elementi nella lista
                contare = True
                n_elementi = []
                while contare:
                    for n in lista:
                        if n in n_elementi:
                            pass
                        else:
                            n_elementi.append(n)
                    contare = False                            
                print(f"Il numero di elementi diversi nella lista è {len(n_elementi)}")
            
            # Chiede all'utente se vuole continuare con un altro esercizio                
            continuare = input("Vuoi fare un altro esercizio?").lower()
            if continuare == "no":
                switch = False
                print("\nEsercitazione finita")  

                
                
# ---------------------------
# Esercizio completo slide 86
# ---------------------------
            
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
            
switch = True

while switch:
    n = int(input("Inserisci un numero: ")) 
    if n < 0:
        print("Prova con un numero positivo")
        pass
    else:      
        sum_pari = 0
        sum_dispari = 0
        numeri_pari = []
        numeri_dispari = []
        for i in range(1, n+1):  # Nel caso in cui si voglia escludere n dal conteggio, bisogna modificare con n
               
            if i % 2 == 0:
                sum_pari += i # Somma i numeri pari compresi tra 1 e n
                numeri_pari.append(i) # Aggiunge numeri pari compresi tra 1 e n ad una lista di soli numeri pari    

                
            elif i % 2 !=0:
                sum_dispari += i
                numeri_dispari.append(i) # Aggiunge numeri dispari compresi tra 1 e n ad una lista di soli numeri dispari

        print(f"I numeri pari compresi tra 1 e {n} sono {numeri_pari}, e la somma di questi numeri è {sum_pari}")                  
        print(f"I numeri dispari compresi tra 1 e {n} sono {numeri_dispari}, e la somma di questi numeri è {sum_dispari}")
              
        if is_prime(n): # Verifica che il numero sia primo o meno
            print(f"{n} è un numero primo")
        else:
            print(f"{n} non è un numero primo")          
               
        switch = False