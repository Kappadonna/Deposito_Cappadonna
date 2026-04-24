class Persona:
    
    def __init__(self, nome:str, eta: int): 
        self.__nome = nome  # variabile privata
        self.__eta = eta    # variabile privata
        
    def presentazione(self):
        print(f"Ciao sono {self.__nome} e ho {self.__eta} anni")
        
    def get_nome(self):
        # metodo per estrarre nome
        return self.__nome 
    
    def get_eta(self):
        # metodo per estrarre eta
        return self.__eta 
    
    def set_nome(self, nuovo_nome):
        # metodo per moodificare nome
        self.__nome = nuovo_nome
        
    def set_eta(self, nuova_eta):
        # metodo per modificare eta
        self.__eta = nuova_eta    
    
class Studente(Persona):
    
    def __init__(self, nome, eta, voti = None):     
        super().__init__(nome, eta)
        # variabile privata, inizializzata come lista vuota se è non viene inserito nulla al momento della creazione dell'istanza 
        self.__voti = voti if voti is not None else [] 
        
        # Se non è lista, ritorna errore
        if not isinstance(self.__voti, list):
            raise TypeError("voti deve essere una lista")

        # Se i numeri inseriti nella lista non sono interi ritorna errore
        if not all(isinstance(v, int) for v in self.__voti):
            raise ValueError("tutti i voti devono essere interi")
        
    def media_voti(self):
        # Calcola la media dei voti
        media = sum(self.__voti) / len(self.__voti)
        return media
    
    def presentazione(self):
        print(f"Ciao sono {self.get_nome()} e ho {self.get_eta()} anni. Sono uno studente con la media {self.media_voti()}")
        
    def get_voti(self):
        # metodo per ritornare la lista dei voti
        return self.__voti
        
    def set_voti(self, lista_voti):
        # metodo per inserire lista con i voti in un secondo momento
        self.__voti = lista_voti
    
class Professore(Persona):
    
    def __init__(self, nome, eta, materia = None):
        super().__init__(nome, eta)
        self.__materia = materia # variabile privata
        
    def presentazione(self):
        print(f"Ciao sono {self.get_nome()} e ho {self.get_eta()} anni. Sono il professore di {self.get_materia()}")
        
    def get_materia(self):
        # metodo per ritornare la materia
        return self.__materia

    def set_materia(self, materia):
        # metodo per modificare o importare la materia in un secondo momento
        self.__materia = materia
           
        
aldo = Persona("Aldo", 40)

aldo.presentazione()
print(aldo.get_nome())
print(aldo.get_eta())

giovanni = Studente("Giovanni", 22, [18, 25, 26, 19, 19])
giovanni.presentazione()
print(giovanni.get_nome())
print(giovanni.get_eta())
        
giacomo = Professore("Giacomo", 50, "Filosofia")
giacomo.presentazione()
print(giacomo.get_nome())
print(giacomo.get_eta())
        

class Gestionale:
    
    def __init__(self, persone_registrate = None):
        self.persone_registrate = persone_registrate if persone_registrate is not None else {} # se viene dato valore, persone_registrate = valore, altrimenti inizializzato come dizionario vuoto
        
    def registra_persona(self, nickname):        
        # Quando si chiama il metodo, passare il nome che si vuole dare alla persona da creare
        # Richiedere all'utente il tipo di persona da creare e l'età
        selezione = input("Quale persona vuoi registrare? \n S per Studente\n P per Professore:")
        eta = int(input("Quante anni ha la persona da registrare? "))
        
        # Match / case per creare tipologia unità coerentemente alla decisione dell'utente
        match selezione.lower():
            case "s":
                persona = Studente(nickname, eta)
            case "p":
                persona = Professore(nickname, eta)
            case _:
                print("Inserimento non valido, riprova")
                return None        

        # aggiunge al dizionario come chiave il nome che abbiamo dato alla persona, come valore l'istanza creata tramite match / case
        self.persone_registrate[nickname] = persona
        
        # ritorna persona creata così da poterla utilizzare per effettuare metodi specifici
        return persona        
        
        
        
    def mostra_persone(self):
        # se dizionario vuoto, informa l'utente stampando una stringa
        if not self.persone_registrate:
            print("Non ci sono unità persone nel sistema.")
            return

        # se persone presenti nel gestionale, stampa informazioni sulle persone registrate
        print("\n--- ELENCO PERSONE REGISTRATE ---")
        # nickname è la chiave, persona (l'istanza di classe) il valore del dizionario
        for nickname, persona in self.persone_registrate.items():
            # type(unita).__name__ prende il nome della classe (Studente, Professore)
            tipo = type(persona).__name__
            print(f"{nickname} è di un {tipo} di {persona.get_eta()} anni.")
            
            
g = Gestionale()

s = g.registra_persona("Gianluca")
p = g.registra_persona("Edoardo")

g.mostra_persone()

s.set_voti([18, 30, 24, 23, 23, 19])
p.set_materia("Programmazione")

s.presentazione()
p.presentazione()