from Veicolo import Automobile, Furgone

class Agenzia:
    
    # Mappa per identificare la classe corretta in base al tipo (stringa)
    MAPPA_TIPI = {
        "automobile": Automobile,
        "furgone": Furgone,
        }
    
    # costruttore con nome, flotta e storico_noleggi
    def __init__(self, nome):
        self.nome = nome
        self.flotta = []
        self.storico_noleggi = []
    
    # metodi per gestire la flotta e i noleggi    
    def aggiungi_veicolo(self, veicolo):
        self.flotta.append(veicolo)
        print(f"Veicolo {veicolo.targa} aggiunto alla flotta.")
        return True
    
    # rimuove un veicolo dalla flotta in base alla targa
    def rimuovi_veicolo(self, targa):
        for veicolo in self.flotta:
            if veicolo.targa == targa:
                self.flotta.remove(veicolo)
                print(f"Veicolo {targa} rimosso dalla flotta.")
                return True
        print(f"Veicolo {targa} non trovato nella flotta.")
        return False
    
    # cerca un veicolo per targa e restituisce l'oggetto o None se non trovato
    def cerca_veicolo(self, targa):
        for veicolo in self.flotta:
            if veicolo.targa == targa:
                return veicolo
        return None
    
    # modifica prezzo e/o disponibilità di un veicolo esistente
    def modifica_veicolo(self, targa, nuovo_prezzo = None, nuova_disponibilita = None):
        veicolo = self.cerca_veicolo(targa)
        if veicolo:
            if nuovo_prezzo is not None:
                veicolo.prezzo_giornaliero = nuovo_prezzo
            if nuova_disponibilita is not None:
                veicolo.disponibile = nuova_disponibilita
            print(f"Veicolo {targa} modificato.")
            return True
        print(f"Veicolo {targa} non trovato nella flotta.")
        return False
    
    # noleggia un veicolo se disponibile, aggiorna lo storico e la flotta
    def noleggia_veicolo(self, targa, cliente, giorni):
            veicolo = self.cerca_veicolo(targa)
            if veicolo and veicolo.disponibile:
                costo = veicolo.calcola_costo(giorni)
                veicolo.disponibile = False
                self.storico_noleggi.append({
                    "targa": targa, 
                    "cliente": cliente, 
                    "giorni": giorni, 
                    "costo": costo
                })
                print(f"Veicolo {targa} noleggiato a {cliente} per {giorni} giorni. Costo totale: €{costo}")
                return True
            print(f"Veicolo {targa} non disponibile per il noleggio.")
            return False
    
    # restituisce un veicolo e aggiorna la disponibilità
    def restituisci_veicolo(self, targa):
        veicolo = self.cerca_veicolo(targa)
        if veicolo and not veicolo.disponibile:
            veicolo.disponibile = True
            print(f"Veicolo {targa} restituito e ora disponibile.")
            return True
        print(f"Veicolo {targa} non trovato o già disponibile.")
        return False
    
    # visualizza la flotta attuale con descrizione dettagliata
    def visualizza_flotta(self):
        if not self.flotta:
            print("La flotta è vuota.")
        else:
            print("Flotta attuale:")
            for veicolo in self.flotta:
                print(veicolo.descrizione())
    
    # visualizza lo storico dei noleggi con dettagli sui veicoli            
    def visualizza_storico_noleggi(self):
        if not self.storico_noleggi:
            print("Nessun noleggio registrato.")
        else:
            print("Storico noleggi:")
            for noleggio in self.storico_noleggi:
                veicolo = self.cerca_veicolo(noleggio['targa'])
                print(f"Cliente: {noleggio['cliente']}, Veicolo: {veicolo.descrizione() if veicolo else 'Sconosciuto'}, Giorni: {noleggio['giorni']}, Costo: €{noleggio['costo']}")
    
    # analizza la flotta filtrando per tipo (automobile o furgone)            
    def analizza_per_tipo(self, tipo):
        classe = self.MAPPA_TIPI.get(tipo.lower())
        if classe is None:
            print(f"Tipo '{tipo}' non riconosciuto")
            return
        trovati = [veicolo for veicolo in self.flotta if isinstance(veicolo, classe)]
        for veicolo in trovati:
            print(veicolo.descrizione())
            
