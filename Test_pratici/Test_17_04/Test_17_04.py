# Operazioni

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

# MENU     
accounts = []
id_count = 0

on = True

while on:
    risposta = input("Effettua log-in o registrazione: ")
    match risposta:
        case 'log-in':
            nome =input("Inserisci nome utente: ")
            pwd = input("Inserisci password: ")
            dati = accounts[id-1][3]
            risultati = accounts[id-1][4]
            id = int(input('Inserisci ID: '))
            if nome == accounts[id-1][0] and pwd == accounts[id-1][1]:
                        print(f'Benvenuto {nome}')
                        while True:
                            funzione = int(input("Che funzione vuoi svolgere? Premi 1 per effettuare operazioni, 2 per vedere dati o risultati, 3 per uscire: "))
                            match funzione:
                                case 1:
                                    if len(risultati) >= 4:
                                        print("Hai raggiunto il limite di 4 operazioni.")
                                    else:  
                                        operazione = int(input("Che operazione vuoi fare? Premi 1 per somma, 2 per sottrazione, 3 per moltiplicazione, 4 per divisione, 5 per divisione intera: ")) 
                                        match operazione:
                                            case 1:
                                                res = somma() 
                                                risultati.append(res[0])
                                                dati.append(res[1])
                                            case 2:
                                                res = sottrazione()
                                                risultati.append(res[0])
                                                dati.append(res[1])                                        
                                            case 3:
                                                res = moltiplicazione()
                                                risultati.append(res[0])
                                                dati.append(res[1])                                        
                                            case 4:
                                                res = divisione()
                                                risultati.append(res[0])
                                                dati.append(res[1])                                        
                                            case 5:
                                                res = divisione_intera()
                                                risultati.append(res[0])
                                                dati.append(res[1])                                        
                                            case _:
                                                print("Operazione non valida") 
                                case 2:
                                    valutazione = True
                                    while valutazione:
                                        visualizzazione = int(input("Cosa vuoi visualizzare? Premi 1 per visualizzare i dati, premi 2 per visualizzare il risultato, 3 per terminare: "))
                                        match visualizzazione:
                                            case 1:
                                                print(f"I dati utilizzati nelle operazioni sono: {dati}")
                                            case 2:
                                                print(f"I risultati delle operazioni svolte sono: {risultati}")
                                            case 3:
                                                print("Visualizzazione terminata")
                                                valutazione = False
                                            case _:
                                                print("Inserimento sbagliato, riprova")
                                case 3:
                                    break
        case "registrazione":
            profile = []
            
            while True:
                nome = input("Crea un nome utente: ")
                unico = True
                
                for account in accounts:
                    if account[0] == nome:                      # confronta con primo valore degli account creati e inseriti nella lista accounts
                        print("Nome utente non disponibile")    
                        unico = False                           # se esiste un nome utente uguale, ne fa creare un nuovo
                        break
                
                if unico:                                       # se non esiste lo crea
                    profile.append(nome)                        
                    break
            pwd = input("Crea una password: ")
            profile.append(pwd)
            id_count +=1
            id = id_count
            profile.append(id)
            profile.append([])  # crea lista per i dati utilizzati dall'utente
            profile.append([])  # crea la lista dei risultati ottenuti dall utente
            
            accounts.append(profile)
            print(f"Registrazione effettuate con nome utente: {nome}, password: {pwd}, id numero: {id}")
        
        case _:
            break
    
