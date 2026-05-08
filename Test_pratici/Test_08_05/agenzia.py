class Agenzia:
    
    def __init__(self, nome):
        self.nome = nome
        self.flotta = []
        self.storico_noleggi = []
        
    def aggiungi_veicolo(self, veicolo):
        self.flotta.append(veicolo)
        print(f"Veicolo {veicolo.targa} aggiunto alla flotta.")
        # return True
    
    def rimuovi_veicolo(self, targa):
        for veicolo in self.flotta:
            if veicolo.targa == targa:
                self.flotta.remove(veicolo)
                print(f"Veicolo {targa} rimosso dalla flotta.")
                return True
        print(f"Veicolo {targa} non trovato nella flotta.")
        return False
    
    def cerca_veicolo(self, targa):
        for veicolo in self.flotta:
            if veicolo.targa == targa:
                return veicolo
        return None
    
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
    
    def noleggia_veicolo(self, targa, cliente, giorni):
        veicolo = self.cerca_veicolo(targa)
        if veicolo and veicolo.disponibile:
            costo = veicolo.calcola_costo(giorni)
            veicolo.disponibile = False
            self.storico_noleggi.append({"cliente": cliente, "veicolo": veicolo, "giorni": giorni, "costo": costo})
            print(f"Veicolo {targa} noleggiato a {cliente} per {giorni} giorni. Costo totale: €{costo}")
            return True
        print(f"Veicolo {targa} non disponibile per il noleggio.")
        return False
    
    def restituisci_veicolo(self, targa):
        veicolo = self.cerca_veicolo(targa)
        if veicolo and not veicolo.disponibile:
            veicolo.disponibile = True
            print(f"Veicolo {targa} restituito e ora disponibile.")
            return True
        print(f"Veicolo {targa} non trovato o già disponibile.")
        return False
    
    def visualizza_flotta(self):
        if not self.flotta:
            print("La flotta è vuota.")
        else:
            print("Flotta attuale:")
            for veicolo in self.flotta:
                print(veicolo.descrizione())
                
    def visualizza_storico_noleggi(self):
        if not self.storico_noleggi:
            print("Nessun noleggio registrato.")
        else:
            print("Storico noleggi:")
            for noleggio in self.storico_noleggi:
                print(f"Cliente: {noleggio['cliente']}, Veicolo: {noleggio['veicolo'].descrizione()}, Giorni: {noleggio['giorni']}, Costo: €{noleggio['costo']}")
                
    def analizza_per_tipo(self, tipo):
        trovati = [veicolo for veicolo in self.flotta if isinstance(veicolo, tipo)]
        for veicolo in trovati:
            print(veicolo.descrizione())
            
