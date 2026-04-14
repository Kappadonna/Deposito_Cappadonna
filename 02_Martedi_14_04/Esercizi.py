# If-elif-else

# Esercizio 1
numero = int(input("Inserisci un numero positivo: "))

# Check prima condizione
if numero > 10:
    print(f"{numero} maggiore di 10, wow!")
    # Check seconda condizione
    if numero >100:
        print(f"{numero} è maggiore di 100, Wow!")
        # Check terza condizione
        if numero > 1000:
            print(f"{numero} maggiore di 1000, WOW!")
            

# Esericizio 2


l = [1, 2, 3, 4, 5]

print(l)
# Utente definisce l'azione da svolgere
azione = input("Cosa vuoi fare? aggiungi, modifica, elimina: ")

# Se l'utente digita 'aggiungi'
if azione == "aggiungi":
    numero = int(input("Che numero vuoi aggiungere alla fine della lista? "))
    # Aggiunge alla fine della lista il numero indicato dall'utente
    l.append(numero)
    print(l)
# Se l'utente digita 'modifica' 
elif azione == "modifica":
    indice = int(input("Inserisci l'indice nel quale vuole inserire il nuovo numero "))
    numero = int(input("Inserisci il numero da inserire "))
    # inserisce il numero all'indice specificato
    l.insert(indice, numero)
    print(l)
else:
    # se digita qualsiasi altra cosa (eventuali errori di battitura riamdano a questa condizione)
    numero = int(input("Quale numero vuoi eliminare dalla lista? "))
    # rimuove il numero dalla lista
    l.remove(numero)
    print(l)
    
    
# Esercizio 3

# Inizializzo liste per effettuare test su account già presente 
nomi = ["Gianluca"]
passwords = ["ciao"]
ids = [1]

# Inizializzo contatore id con 1 perche è gia presente un profilo di test
id = 1
answer = input("Hai già un account? si / no ")

# Se ha gia l'account, fa accedere l'utente
if  answer == "si":
    password = input("Inserisci password: ")
    id = int(input("Inserisci ID: "))
    if password == passwords[id-1]:
        print(f"Benvenuto {nomi[id-1]}")

# Se non ha l'account, lo fa registrare
else:
    nome = input("Inserisci nome: ")
    password = input("Inserisci password: ")
    id +=1
    # Aggiunge i valori creati alle liste definite fuori dall'if-else statement
    nomi.append(nome) 
    passwords.append(password)
    ids.append(id)
    # Stampa il riepilogo delle informazioni inserite
    print(f" Benvenuto {nomi[id-1]}, la tua password è : '{passwords[id-1]}', e il tuo id: '{ids[id-1]}' ")
        

