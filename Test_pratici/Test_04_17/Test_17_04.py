# Operazioni

# somma

def somma():
    print("Hai selezionato somma.")
    numeri = []
    somma = 0
    q = int(input("Quanti numeri vuoi sommare tra loro? ")) # fa selezionare quantità di numeri da inserirenell'operazione all'utente 
    for i in range(q):                                      
        n = int(input("Seleziona un numero da inserire nella somma: ")) # fa scegliere i numeri all'utente
        numeri.append(n)
    for i in numeri:
        somma += i
        res = (somma, numeri) # crea tupla con risultato e dati utilizzati
    return res

# sottrazione

def sottrazione():
    print("Hai selezionato sottrazione.")
    numeri = []
    sottrazione = 0
    q = int(input("Quanti numeri vuoi sottrarre tra loro? "))  # fa selezionare quantità di numeri da inserirenell'operazione all'utente
    for i in range(q):                                        
        n = int(input("Seleziona un numero da inserire nella sottrazione: ")) # fa scegliere i numeri all'utente
        numeri.append(n)
        if i == 0:
            sottrazione = n
        else:
            sottrazione -= n
    res = (sottrazione, numeri) # crea tupla con risultato e dati utilizzati
    return res
        
# moltiplicazione

def moltiplicazione():
    print("Hai selezionato moltiplicazione.")
    numeri = []
    prodotto = 1
    q = int(input("Quanti numeri vuoi moltiplicare tra loro? "))  # fa selezionare quantità di numeri da inserirenell'operazione all'utente
    for i in range(q):                                            
        n = int(input("Seleziona un numero da inserire nella moltiplicazione: ")) # fa scegliere i numeri all'utente
        numeri.append(n)
    for i in numeri:
        prodotto *= i
    res = (prodotto, numeri) # crea tupla con risultato e dati utilizzati
    return res

# divisione

def divisione():
    print("Hai selezionato divisione.")
    numeri = []
    n1 = int(input("Inserisci il primo numero: ")) # fa selezionare dividendo
    numeri.append(n1)
    while True:
        n2 = int(input("Inserisci il secondo numero: ")) # fa selezionare divisore
        if n2 == 0:                                      # se divisore = 0 fa inserire un altro numero
            print("Non puoi dividere per 0, riprova.") 
        else:
            numeri.append(n2)
            break
    
    divisione = numeri[0] / numeri[1]
    res =(divisione, numeri) # crea tupla con risultato e dati utilizzati
    return res
        
# divisione intera

def divisione_intera():
    print("Hai selezionato divisione_intera.")
    numeri = []
    n1 = int(input("Inserisci il primo numero: ")) # fa selezionare dividendo
    numeri.append(n1) 
    while True:
        n2 = int(input("Inserisci il secondo numero: ")) # fa selezionare divisore
        if n2 == 0:                                      # se divisore = 0 fa inserire un altro numero
            print("Non puoi dividere per 0, riprova.") 
        else:
            numeri.append(n2)
            break
    
    divisione_intera = numeri[0] // numeri[1]
    res = (divisione_intera, numeri) # crea tupla con risultato e dati utilizzati
    return res

# MENU     
accounts = []
id_count = 0

on = True

while on:
    risposta = input("Effettua log-in o registrazione: ") # quando il programma è in esecuzione chiede log-in o registrazione
    match risposta:
        case 'log-in': # in caso di login
            
            nome =input("Inserisci nome utente: ") # fa inserire nome
            pwd = input("Inserisci password: ")    # fa inserire password
            id = int(input('Inserisci ID: '))      # da inserire id
            dati = accounts[id-1][3]               # crea lista vuota in cui inserire i dati
            risultati = accounts[id-1][4]          # crea lista vuota in cui inserire i risultati

            if nome == accounts[id-1][0] and pwd == accounts[id-1][1]: # verifica validità dati inseriti
                        print(f'Benvenuto {nome}')
                        while True: # fin quando si è loggati, chiede all'utente cosa di vuole svolgere
                            funzione = int(input("Che funzione vuoi svolgere? Premi 1 per effettuare operazioni, 2 per vedere dati o risultati, 3 per uscire: "))
                            match funzione: 
                                case 1: # se l'utente seleziona operazioni
                                    if len(risultati) >= 4: # verifica che non ne abbia già fatte più di 4 in precedenza 
                                        print("Hai raggiunto il limite di 4 operazioni.")
                                    else:   # chiede all'utente quale operazione vuole svolgere
                                        operazione = int(input("Che operazione vuoi fare? Premi 1 per somma, 2 per sottrazione, 3 per moltiplicazione, 4 per divisione, 5 per divisione intera: ")) 
                                        match operazione:
                                            case 1:
                                                res = somma()            # assegna il risultato della funzione alla variabile
                                                risultati.append(res[0]) # aggiunge primo valore della tupla alla lista dei risultati
                                                dati.append(res[1])      # aggiunge secondo valore della tupla alla lista dei dati
                                            case 2:
                                                res = sottrazione()       # assegna il risultato della funzione alla variabile
                                                risultati.append(res[0])  # aggiunge primo valore della tupla alla lista dei risultati
                                                dati.append(res[1])       # aggiunge secondo valore della tupla alla lista dei dati                                  
                                            case 3:
                                                res = moltiplicazione()  # assegna il risultato della funzione alla variabile
                                                risultati.append(res[0]) # aggiunge primo valore della tupla alla lista dei risultati
                                                dati.append(res[1])      # aggiunge secondo valore della tupla alla lista dei dati                                 
                                            case 4:
                                                res = divisione()        # assegna il risultato della funzione alla variabile
                                                risultati.append(res[0]) # aggiunge primo valore della tupla alla lista dei risultati
                                                dati.append(res[1])      # aggiunge secondo valore della tupla alla lista dei dati                                  
                                            case 5:
                                                res = divisione_intera() # assegna il risultato della funzione alla variabile
                                                risultati.append(res[0]) # aggiunge primo valore della tupla alla lista dei risultati
                                                dati.append(res[1])      # aggiunge secondo valore della tupla alla lista dei dati                                  
                                            case _:
                                                print("Operazione non valida") 
                                case 2:
                                    valutazione = True                                                          # necessario per dare la possibilità di tornare al menu di scelta operazione / visualizzazione
                                    while valutazione:
                                        visualizzazione = int(input("Cosa vuoi visualizzare? Premi 1 per visualizzare i dati, premi 2 per visualizzare il risultato, 3 per terminare: "))
                                        match visualizzazione:
                                            case 1:
                                                print(f"I dati utilizzati nelle operazioni sono: {dati}")       # stampa i risultati delle operazini svolte dall'utente
                                            case 2:
                                                print(f"I risultati delle operazioni svolte sono: {risultati}") # stampa i risultati dell'operazione svolta dall'utente
                                            case 3:
                                                print("Visualizzazione terminata")                              # fa tornare indeintro al menù di scelta operazione/visualizzazione
                                                valutazione = False
                                            case _:
                                                print("Inserimento sbagliato, riprova")                         # Se inserimento sbagliato da la possibilità all'utente di digitare nuovamente 
                                case 3:
                                    break
        case "registrazione":
            profile = []                                        # inizializza profilo utente come lista vuota
            
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
            pwd = input("Crea una password: ")                  # fa creare la password all'utente
            profile.append(pwd)
            id_count +=1
            id = id_count                                       # crea id in modo progressivo
            profile.append(id)
            profile.append([])                                  # crea lista per i dati utilizzati dall'utente
            profile.append([])                                  # crea la lista dei risultati ottenuti dall utente
            
            accounts.append(profile)                            # aggiunge alla lista degli account il profilo creato
            print(f"Registrazione effettuate con nome utente: {nome}, password: {pwd}, id numero: {id}")
        
        case _:
            break
    
