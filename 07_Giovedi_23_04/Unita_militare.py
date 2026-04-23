class UnitaMilitare:
    
    def __init__(self, nome: str, numero_soldati: int): # definizione costruttore
        self.nome = nome
        self.numero_soldati = numero_soldati
        
    def __len__(self): 
        return self.numero_soldati # ritorna il numero di unità registrate
        
    def __str__(self):
        return f"L'unità militare {self.nome} ha {self.numero_soldati} soldati" # ritorna stringa di testo descrittiva
        
    def __eq__(self, other): 
        if not isinstance(other, UnitaMilitare): # verifica istanza UnitaMilitare con other, se sono istanze diverse, ritorna falso
            return False
        
        return self.nome == other.nome # se le istanze sono della stessa classe (UnitaMilitare) controlla nome istnaze per giudicare vero/falso
    
    def __repr__(self):
        return f"UnitaMilitare( nome = {self.nome}, numero_soldati = {self.numero_soldati})" # ritorna stringa di testo utile ai developer
        
    def muovi(self):
        print(f"L'unità militare {self.nome} si sta muovendo, passo.") # stampa stringa che indica movimento
    
    def attacca(self):
        print(f"Unità militare {self.nome} hai il permesso di attaccare, passo.") # stampa stringa che indica attacco
    
    def ritira(self):
        print(f"Unità militare {self.nome} ritirata! Ripeto, ritirata!! Passo.") # stampa stringa che indica ritirata
        
    
        
        
class Fanteria(UnitaMilitare): # sottoclasse UnitaMilitare
    
    def __init__(self, nome, numero_soldati, n_trincee = 0):
        super().__init__(nome, numero_soldati) # costruttore di UnitaMilitare
        self.n_trincee = n_trincee # attributo specifico della classe
        
    def costruisci_trincea(self):
        print("Costruzione trincea in corso") # stampa stringa che indica costruzione trincea
        self.n_trincee += 1 # aggiunge 1 al valore di trincee costruite (n_trincee)
        
    def __repr__(self): # aggiorna __repr__ per tenere in considerazione n_trincee
        return f"Fanteria( nome = {self.nome}, numero_soldati = {self.numero_soldati}, n_trincee = {self.n_trincee})" 
    
    def __eq__(self, other):
        if not isinstance(other, Fanteria): # verifica istanza Fanteria con other, se sono istanze diverse, ritorna falso
            return False
        
        return self.nome == other.nome  # se le istanze sono della stessa classe (Fanteria) controlla nome istnaze per giudicare vero/falso


class Artiglieria(UnitaMilitare):
    def __init__(self, nome, numero_soldati, n_calibrazioni = 0):
        super().__init__(nome, numero_soldati) # costruttore di UnitaMilitare
        self.n_calibrazioni = n_calibrazioni # attributo specifico della classe
        
    def calibrazione_artiglieria(self):
        print("Calibrazione artiglieria in corso") # stampa stringa che indica calibrazione artiglieria in corso
        self.n_calibrazioni +=1 # aggiunge 1 al valore di calibrazioni effettuate (n_calibrazioni)
    
    def __repr__(self): # aggiorna __repr__ per tenere in considerazione n_calibrazioni
        return f"Artiglieria( nome = {self.nome}, numero_soldati = {self.numero_soldati}, n_calibrazioni = {self.n_calibrazioni})"

    def __eq__(self, other):
        if not isinstance(other, Artiglieria): # verifica istanza Artiglieria con other, se sono istanze diverse, ritorna falso
            return False
        
        return self.nome == other.nome # se le istanze sono della stessa classe (Artiglieria) controlla nome istnaze per giudicare vero/falso


class Cavalleria(UnitaMilitare):
    
    def __init__(self, nome, numero_soldati, n_esplorazioni = 0):
        super().__init__(nome, numero_soldati) # costruttore di UnitaMilitare
        self.n_esplorazioni = n_esplorazioni # attributo specifico della classe
        
    def esplora_terreno(self):
        print("Esplorazione dell'area in corso") # stampa stringa che indica esplorazione dell'area in corso
        self.n_esplorazioni +=1 # aggiunge 1 al valore di numero esplorazioni (n_esplorazione)

    def __repr__(self): # aggiorna __repr__ per tenere in considerazione n_esplorazioni
        return f"Cavalleria( nome = {self.nome}, numero_soldati = {self.numero_soldati}, n_esplorazioni = {self.n_esplorazioni})"

    def __eq__(self, other):
        if not isinstance(other, Cavalleria): # verifica istanza Cavalleria con other, se sono istanze diverse, ritorna falso
            return False
        
        return self.nome == other.nome # se le istanze sono della stessa classe (Cavalleria) controlla nome istnaze per giudicare vero/falso
    
    
class SupportoLogistico(UnitaMilitare):
    
    def __init__(self, nome, numero_soldati, n_rifornimenti = 0):
        super().__init__(nome, numero_soldati) # costruttore di UnitaMilitare
        self.n_rifornimenti = n_rifornimenti # attributo specifico della classe
        
    def rifornisci_unita(self):
        print("Rifornimento unità in corso") # stampa stringa che indica rifornimenti in corso
        self.n_rifornimenti +=1 # aggiunge 1 al valore di rifornimenti effettuati (n_rifornimenti)
        
    def __repr__(self): # aggiorna __repr__ per tenere in considerazione n_rifornimenti
        return f"SupportoLogistico( nome = {self.nome}, numero_soldati = {self.numero_soldati}, n_rifornimenti = {self.n_rifornimenti})"
    
    def __eq__(self, other):
        if not isinstance(other, SupportoLogistico): # verifica istanza SupportoLogistico con other, se sono istanze diverse, ritorna falso
            return False
        
        return self.nome == other.nome  # se le istanze sono della stessa classe (SupportoLogistico) controlla nome istnaze per giudicare vero/falso
    

class Ricognizione(UnitaMilitare):
    
    def __init__(self, nome, numero_soldati, n_ricognizioni = 0):
        super().__init__(nome, numero_soldati) # costruttore di UnitaMilitare
        self.n_ricognizioni = n_ricognizioni # attributo specifico della classe
        
    def ricognizione_unita(self):
        print("Missione di sorveglianza in corso") # stampa stringa che indica ricognizione in corso
        self.n_ricognizioni +=1 # aggiunge 1 al valore di ricognizioni effettuate (n_ricognizione)

    def __repr__(self): # aggiorna __repr__ per tenere in cosniderazione n_ricognizioni
        return f"Ricognizione( nome = {self.nome}, numero_soldati = {self.numero_soldati}, n_ricognizioni = {self.n_ricognizioni})"

    def __eq__(self, other):
        if not isinstance(other, Ricognizione): # verifica istanza Ricognizione con other, se sono istanze diverse, ritorna falso
            return False
        
        return self.nome == other.nome  # se le istanze sono della stessa classe (Ricognizione) controlla nome istnaze per giudicare vero/falso
        
 
class ControlloMilitare:
    
    def __init__(self, unita_registrate = None):
        self.unita_registrate = unita_registrate if unita_registrate is not None else {} # se viene dato valore, unita_registrate = valore, altrimenti inizializzato come dizionario vuoto
        
    def registra_unita(self, nickname):
        
        # Quando si chiama il metodo, passare il nome che si vuole dare all'unità da creare
        # Richiedere all'utente il tipo di unità da creare e la quantità
        selezione = input("Quale unità vuoi registrare? \n A per Artiglieria\n F per Fanteria\n C per Cavalleria\n S per Supporto Logistico\n R per Ricognizione:  ")
        quantita = int(input("Quante unità vuoi registrare? "))
        
        # Match / case per creare tipologia unità coerentemente alla decisione dell'utente
        match selezione.lower():
            case "a":
                unita = Artiglieria(nickname, quantita)
            case "f":
                unita = Fanteria(nickname, quantita)
            case "c":
                unita = Cavalleria(nickname, quantita)
            case "s":
                unita = SupportoLogistico(nickname, quantita)
            case "r":
                unita = Ricognizione(nickname, quantita)
            case _:
                print("Inserimento non valido, riprova")
                return None        

        # aggiunge al dizionario come chiave il nome che abbiamo dato all'unita, come valore l'istanza creata tramite match / case
        self.unita_registrate[nickname] = unita
        
        # ritorna unità creata così da poterla utilizzare per effettuare metodi specifici
        return unita

    def mostra_unita(self):
        # se dizionario vuoto, informa l'utente stampando una stringa
        if not self.unita_registrate:
            print("Non ci sono unità registrate nel sistema.")
            return

        # se unità presenti nel registro, stampa informazioni sulle unità registrate
        print("\n--- ELENCO UNITÀ SOTTO CONTROLLO ---")
        # nickname è la chiave, unità (l'istanza di classe) il valore del dizionario
        for nickname, unita in self.unita_registrate.items():
            # type(unita).__name__ prende il nome della classe (Fanteria, Artiglieria, ecc.)
            tipo = type(unita).__name__
            print(f"L'unità '{nickname}' è di tipo {tipo} e conta {unita.numero_soldati} soldati.")
    
    # stampa le informazioni dei metodi speciali definiti nella classe UnitaMilitare    
    def dettagli_unita(self, unita):
        if unita:
            print(f"\nDETTAGLI: {unita}")
            print(f"Lunghezza (len): {len(unita)}")
            print(f"Rappresentazione (repr): {repr(unita)}")

      
""" 
alpha = Artiglieria("Alpha", 9)
beta = Fanteria("Beta", 8)
charlie = Cavalleria("Charlie", 10)
delta = SupportoLogistico("Delta", 3)
gamma = Ricognizione("Gamme", 2)
"""

controllo = ControlloMilitare()

alpha = controllo.registra_unita("alpha") # selezionare r per fare ricognizione
controllo.mostra_unita()
controllo.dettagli_unita(alpha)

alpha.ricognizione_unita()

beta = controllo.registra_unita("beta") # se
