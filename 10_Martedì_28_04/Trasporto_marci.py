from abc import ABC, abstractmethod

class VeicoloTrasporto:
    
    # metodo costruttore per inizializzare gli attributi del veicolo
    def __init__(self, targa, peso_massimo, carico_attuale = 0):
        self._targa = targa
        self._peso_massimo = peso_massimo
        self._carico_attuale = carico_attuale
    
    # metodo concreto per caricare il veicolo 
    def carica(self, peso):
        # controlla che il carico attuale più il nuovo peso non superi il peso massimo 
        if self._carico_attuale + peso <= self._peso_massimo:
            self._carico_attuale += peso
        else:
            print("Carico superiore al limite massimo.")
      
    # metodo concreto per scaricare il veicolo   
    def scarica(self, peso):
        # controlla che il carico attuale sia sufficiente per scaricare il peso richiesto
        if self._carico_attuale >= peso:
            self._carico_attuale -= peso
        else:
            print("Veicolo già scarico.")
            
    @abstractmethod
    # metodo astratto per calcolare il costo di manutenzione, deve essere implementato nelle classi figlie
    def costo_manutenzione(self):
        pass

        
    
    
class Camion(VeicoloTrasporto):
    
    # metodo costruttore per inizializzare gli attributi specifici del camion
    def __init__(self, targa, peso_massimo, carico_attuale, numero_assi):
        # chiama il costruttore della classe base per inizializzare gli attributi comuni
        super().__init__(targa, peso_massimo, carico_attuale)
        self._numero_assi = numero_assi
    
    def costo_manutenzione(self):
        # il costo di manutenzione del camion è calcolato in base al numero di assi e al peso massimo
        return self._numero_assi * 100 + self._peso_massimo 
    
    @property
    def peso_massimo(self):
        return self._peso_massimo
    
    @property
    def carico_attuale(self):
        return self._carico_attuale
       
    @carico_attuale.setter
    def carico_attuale(self, nuovo_carico_attuale):
        if 0 <= nuovo_carico_attuale <= self._peso_massimo:
            self._carico_attuale = nuovo_carico_attuale
        else:
            print("Valore non valido per il carico.")
    
class Furgone(VeicoloTrasporto):
    
    # metodo costruttore per inizializzare gli attributi specifici del furgone
    def __init__(self, targa, peso_massimo, carico_attuale, alimentazione):
        super().__init__(targa, peso_massimo, carico_attuale)
        self._alimentazione = alimentazione
        
    def costo_manutenzione(self):
        # il costo di manutenzione del furgone è calcolato in base al tipo di alimentazione
        if self._alimentazione == "elettrico":
            return 200
        elif self._alimentazione == "diesel":
            return 150
        else:
            raise ValueError("Tipo di alimentazione non valido")
        
class Motocarro(VeicoloTrasporto):
    
    # metodo costruttore per inizializzare gli attributi specifici del motocarro
    def __init__(self, targa, peso_massimo, carico_attuale, anni_servizio):
        super().__init__(targa, peso_massimo, carico_attuale)
        self._anni_servizio = anni_servizio
        
    def costo_manutenzione(self):
        # il costo di manutenzione del motocarro è calcolato in base agli anni di servizio
        return self._anni_servizio * 50
    

class GestoreFlotta:
    
    def __init__(self, veicoli = None):
        # inizializza la lista dei veicoli, se non viene fornita una lista, ne crea una vuota
        self._veicoli = veicoli if veicoli is not None else []
        
    def aggiungi_veicolo(self, veicolo: VeicoloTrasporto):
        # aggiunge un'istanza di classe VeicoloTrasporto (o una sua sottoclasse) alla lista dei veicoli
        self._veicoli.append(veicolo)
        print(f"{veicolo.__class__.__name__} con targa {veicolo._targa} aggiunto alla flotta.")
        
    def rimuovi_veicolo(self, targa):
        # filtra la lista dei veicoli e mantiene solo quelli che non hanno la targa specificata
        self._veicoli = [veicolo for veicolo in self._veicoli if veicolo._targa != targa]
        print(f"Veicolo con targa {targa} rimosso dalla flotta.")
        
    def costo_totale_manutenzione(self):
        costo_totale = 0
        # itera su tutti i veicoli nella flotta e somma il costo di manutenzione di ciascuno
        for veicolo in self._veicoli:
            costo_totale += veicolo.costo_manutenzione()
        return costo_totale
    
    def stampa_veicoli(self):
        # stampa le informazioni di ogni veicolo nella flotta
        for veicolo in self._veicoli:
            print(f"Veicolo: {veicolo.__class__.__name__}, Targa: {veicolo._targa}, Peso massimo: {veicolo._peso_massimo}, Carico attuale: {veicolo._carico_attuale}")
            

g = GestoreFlotta()

c = Camion("AB123CD", 10000, 5000, 4)
f = Furgone("EF456GH", 3000, 1500, "elettrico")
m = Motocarro("IJ789KL", 500, 200, 5)

c.carica(2000)
f.carica(1000)
m.carica(100)
c.scarica(500)

g.aggiungi_veicolo(c)
g.aggiungi_veicolo(f)
g.aggiungi_veicolo(m)

g.stampa_veicoli()
print(f"Costo totale manutenzione: €{g.costo_totale_manutenzione()}")

g.rimuovi_veicolo("IJ789KL")
g.stampa_veicoli()
print(f"Costo totale manutenzione: €{g.costo_totale_manutenzione()}")

    
    
gestione = True
# inizializza istanza gestore flotta
g = GestoreFlotta()


while gestione:
    # fa scegliere all'utente l'azione da svolgere
    scelta = input("Scegli un'opzione: 1 per aggiungere un veicolo | 2 caricare o scaricare veicolo | 3 per rimuovere un veicolo | 4 per visualizzare i veicoli e il costo totale di manutenzione | 5 per uscire")

    match scelta:
        # chiede all'utente che tipo di veicolo vuole aggiungere
        case "1":
            # fa compilare le informazioni all'utente
            tipo_veicolo = input("Scegli il tipo di veicolo da aggiungere: 1 per Camion | 2 per Furgone | 3 per Motocarro")
            targa = input("Inserisci la targa del veicolo: ")
            peso_massimo = float(input("Inserisci il peso massimo del veicolo: "))
            carico_attuale = float(input("Inserisci il carico attuale del veicolo: "))
            
            # costruisce istanza in base alla tipologia scelta, ulteriore input in base all'istanza da creare
            if tipo_veicolo == "1":
                numero_assi = int(input("Inserisci il numero di assi del camion: "))
                veicolo = Camion(targa, peso_massimo, carico_attuale, numero_assi)
                
            elif tipo_veicolo == "2":
                alimentazione = input("Inserisci il tipo di alimentazione del furgone (elettrico/diesel): ")
                veicolo = Furgone(targa, peso_massimo, carico_attuale, alimentazione)
                
            elif tipo_veicolo == "3":
                anni_servizio = int(input("Inserisci gli anni di servizio del motocarro: "))
                veicolo = Motocarro(targa, peso_massimo, carico_attuale, anni_servizio)
                
            else:
                print("Tipo di veicolo non valido.")
                continue
            
            # aggiunge istanza veicolo al gestore flotta 
            g.aggiungi_veicolo(veicolo)
            
        case "2":
            # richiede targa del veicolo da caricare/scaricare
            targa = input("Inserisci la targa del veicolo:")
            # richiede l'azione da svolgere
            azione = input("caricare | scaricare")
            # chiede quanti kg devono essere caricati/scaricati
            kg = int(input("Quanto kg vuoi caricare/scaricare?"))
            
            if azione.lower() == "caricare":
                # itera sui veicolo presenti nella flotta, se c'è un match con la targa, carica o scarica la somma definita
                for veicolo in g._veicoli:
                    if veicolo._targa == targa:
                        veicolo.carica(kg)
                        
            else: # azione.lower() == "scaricare"
                for veicolo in g._veicoli:
                    if veicolo._targa == targa:
                        veicolo.scarica(kg)                
                
        case "3":
            # rimuove veicolo con la targa inserita dall'utente dal gestore della flotta
            targa = input("Inserisci la targa del veicolo da rimuovere:")
            g.rimuovi_veicolo(targa)
            
        case "4":
            # stampa informazioni dei veicoli presenti nel gestore della flotta
            g.stampa_veicoli()
            print(f"Costo totale manutenzione: €{g.costo_totale_manutenzione()}")
            
        case "5":
            # fine gestione, esce dal while loop
            gestione = False
            print("Uscita dal sistema di gestione della flotta.")
            
        case _:
            print("Scelta non valida. Riprova.")
        
