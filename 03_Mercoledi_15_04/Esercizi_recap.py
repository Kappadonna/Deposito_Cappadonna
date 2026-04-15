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
    
# ------------------
# Esercizio completo
# ------------------

# Creare menu per scegliere esercizio
switch = True


while switch:
    scelta = int(input("Quale esercizio vuoi svolgere?\n 1 | 2 | 3 | 4 |"))
    match scelta:
        case 1:
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
            numero = int(input("Scegli un numero: "))
            for i in range(numero, -1, -1):
                print(i)
                
            # Chiede all'utente se vuole continuare con un altro esercizio                  
            continuare = input("Vuoi fare un altro esercizio?").lower()
            if continuare == "no":
                switch = False
                print("\nEsercitazione finita")                             
        case 3:
            lista = [213, 42, 543, 5, 62, 10]
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
                n_elementi = 0
                while contare:
                    for n in lista:
                        n_elementi +=1
                    contare = False                            
                print(f"Il numero di elementi nella lista è {n_elementi}")
            
            # Chiede all'utente se vuole continuare con un altro esercizio                
            continuare = input("Vuoi fare un altro esercizio?").lower()
            if continuare == "no":
                switch = False
                print("\nEsercitazione finita")  

                
                

            