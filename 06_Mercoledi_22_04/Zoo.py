class Animale:
    
    def __init__(self, nome, eta: int):
        self.nome = nome
        self.eta = eta
        
    def descrizione(self):
        print(f"{self.nome} è un animale di {self.eta} anni")
        
    def fai_suono(self):
        print(f"{self.nome} sta facendo un suono")
        

class Cane(Animale):
    
    SPECIE = "cane"
    def __init__(self, nome, eta, pelo):
        super().__init__(nome, eta)
        self.pelo = pelo
        
    def descrizione(self):
        super().descrizione()
        print(f"In particolare {self.nome} è un {self.SPECIE} a pelo {self.pelo}")
        
    def fai_suono(self):
        print(f"{self.nome} sta abbaiando!")
    
    def gioca(self):
        print(f"{self.nome} sta giocando col suo padrone")
        
class Gatto(Animale):
    
    SPECIE = "gatto"
    def __init__(self, nome, eta, colore):
        super().__init__(nome, eta)
        self.colore = colore
    
    def descrizione(self):
        super().descrizione()
        print(f"In particolare {self.nome} è un {self.SPECIE} di colore {self.colore}")
        
    def fai_suono(self):
        print(f"{self.nome}, sta miagolando!")
    
    def caccia(self):
        print(f"{self.nome} sta cacciando il topo")
        
class Topo(Animale):
    
    SPECIE = "topo"
    def __init__(self, nome, eta, dimensione):
        super().__init__(nome, eta)
        self.dimensione = dimensione
        
    def descrizione(self):
        super().descrizione()
        print(f"In particolare {self.nome} è un {self.SPECIE} {self.dimensione}")
        
    def fai_suono(self):
        print(f"{self.nome}, sta squittendo!")   
        
    def scappa(self):
        print(f"{self.nome}, sta scappando!") 
        

cane = Cane("Pippo", 8, "corto")
cane.descrizione()
cane.fai_suono()
cane.gioca()

gatto = Gatto("Lino", 4, "bianco")
gatto.descrizione()
gatto.fai_suono()
gatto.caccia()

topo = Topo("Rattata", 1, "grande")
topo.descrizione()
topo.fai_suono()
topo.scappa()
    
    
        