class Posto:
    def __init__(self, numero: int, fila: str, occupato= False):
        self._numero = numero
        self._fila = fila
        self._occupato = occupato
        
    def prenota(self):
        if self._occupato:
            print(f"Il posto {self._numero} {self._fila} è già occupato")
            return False
        self._occupato = True
        print(f"Posto {self._numero} {self._fila} prenotato")
        return True
    
    def libera(self):
        if not self._occupato:
            print(f"Il posto {self._numero} {self._fila} è gia libero")
            return False
        
        self._occupato = False
        print(f"Posto {self._numero} {self._fila} liberato")
    
    def get_info(self):
        return (self._numero, self._fila, self._occupato)
    
    
class PostoVIP(Posto):
    
    def __init__(self, numero, fila, occupato = False, servizi_extra = None):
        super().__init__(numero, fila, occupato)
        self.servizi_extra = servizi_extra if servizi_extra is not None else []
        
    def prenota(self):
        super().prenota()
        prenotazione_servizi = True
        while prenotazione_servizi:
            servizi = input("Quali servizi extra vuoi prenotare? 1 per Accesso al lounge | 2 per Servizio in posto | * per smemmete di selezionare servizi aggiuntivi: ")
            match servizi:
                case "1":
                    self.servizi_extra.append("accesso al lounge")
                case "2":
                    self.servizi_extra.append("servizio in posto")
                case "*":
                    prenotazione_servizi = False
                case _:
                    "Servizio selezionato non valido"
                
        
    
class PostoStandard(Posto):
    
    def __init__(self, numero, fila, costo, occupato = False):
        super().__init__(numero, fila, occupato)
        self.costo = costo
        
    def prenota(self):
        super().prenota()
        print(f"Il posto selezionato ha un costo di €{self.costo}")
    

class Teatro:
    
    def __init__(self, posti):
        self._posti = posti
        
    def aggiungi_posto(self, posto: Posto):
        self._posti.append(posto)
    
    def prenota_posto(self, numero, fila):
        posto_trovato = None
        
        for posto in self._posti:
            if posto._numero == numero and posto._fila == fila:
                posto_trovato = posto
                break
        
        if posto_trovato is None:
            print("Posto non trovato")
            return
        
        if posto_trovato.prenota():
            print("Prenotazione effettuata")
        else:
            print("Posto già occupato")
    
    def stampa_posti_occupati(self):
        for posto in self._posti:
            if posto._occupato == True:
                print(posto)
    
    
p = Posto(3, "b")

print(p.get_info())

p.prenota()
print(p.get_info())

p.libera()
print(p.get_info())

t = Teatro([])

t.aggiungi_posto(Posto(1, "A"))
t.aggiungi_posto(Posto(2, "A"))
t.aggiungi_posto(PostoVIP(3, "B"))
t.aggiungi_posto(PostoStandard(4, "B", 10, False))

t.prenota_posto(1, "A")
t.prenota_posto(1, "A")   # test doppia prenotazione
t.prenota_posto(99, "Z")  # test non esistente

t.stampa_posti_occupati()