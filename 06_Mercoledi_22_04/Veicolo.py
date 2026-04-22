class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        
    def mostra_info(self):
        print(f"Veicolo marca {self.marca}, modello {self.modello}")
    
    
class DotazioniSpeciali:
    def __init__(self, dotazioni: list[str]):
        self.dotazioni = dotazioni
        
    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {",".join(self.dotazioni)}")
        
class AutoSportiva(Veicolo, DotazioniSpeciali):
    
    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self, marca, modello)
        DotazioniSpeciali.__init__(self, dotazioni)
        self.cavalli = cavalli
        
    def mostra_info(self):
        super().mostra_info() # super() fa riferimento alla prima casa da cui eredita le caratteristiche, in questo caso veicolo
        self.mostra_dotazioni()
        print(f"Potenza: {self.cavalli}")
        
auto = AutoSportiva("Ferrari", "F8", ["ABS", "Controllo Trazione", "Airbag laterali"], 720)

auto.mostra_info()
