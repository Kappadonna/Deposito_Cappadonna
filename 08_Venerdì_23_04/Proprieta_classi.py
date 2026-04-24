# INCAPSULAMENTO

class Computer:
    
    def __init__(self, processore):
        self.__processore = processore # Dichiaro un attributo privato
        
    def get_processore(self):
        return self.__processore
    
    def set_processore(self, processore):
        self.__processore = processore
        

pc = Computer("M3")

print(pc.get_processore())
pc.set_processore("M4")
print(pc.get_processore())

pc.__processore = "M5" # Non consente di modficarlo in questo modo
print(pc.get_processore())
print(pc.__processore)
print(pc.get_processore())

# EREDITARIETA'

class Animale:
    
    def __init__(self, nome, eta: int):
        self._nome = nome
        self.eta = eta
        
    def descrizione(self):
        print(f"{self._nome} è un animale di {self.eta} anni")
        
    def fai_suono(self):
        print(f"{self._nome} sta facendo un suono")
        
    def get_nome(self):
        return self._nome
        

class Cane(Animale):
    
    SPECIE = "cane"
    def __init__(self, nome, eta, pelo):
        super().__init__(nome, eta)
        self.pelo = pelo
        
    def descrizione(self):
        super().descrizione()
        print(f"In particolare {self._nome} è un {self.SPECIE} a pelo {self.pelo}")
        
    def fai_suono(self):
        print(f"{self._nome} sta abbaiando!")
    
    def gioca(self):
        print(f"{self._nome} sta giocando col suo padrone")
        
class Gatto(Animale):
    
    SPECIE = "gatto"
    def __init__(self, nome, eta, colore):
        super().__init__(nome, eta)
        self.colore = colore
    
    def descrizione(self):
        super().descrizione()
        print(f"In particolare {self._nome} è un {self.SPECIE} di colore {self.colore}")
        
    def fai_suono(self):
        print(f"{self._nome}, sta miagolando!")
    
    def caccia(self):
        print(f"{self._nome} sta cacciando il topo")
        
class Topo(Animale):
    
    SPECIE = "topo"
    def __init__(self, nome, eta, dimensione):
        super().__init__(nome, eta)
        self.dimensione = dimensione
        
    def descrizione(self):
        super().descrizione()
        print(f"In particolare {self._nome} è un {self.SPECIE} {self.dimensione}")
        
    def fai_suono(self):
        print(f"{self._nome}, sta squittendo!")   
        
    def scappa(self):
        print(f"{self._nome}, sta scappando!") 
        

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
    
print(cane.get_nome())
print(gatto.get_nome())
print(topo.get_nome())
        
        
class Studente:
    
    def __init__(self, nome, voto):
        self.nome = nome
        self.__voto = voto
        
    @property
    def voto(self):
        print("Voto getter")
        return self.__voto
    
    @voto.setter
    def voto(self, nuovo_voto):
        if(0 <= nuovo_voto <=30):
            self.__voto = nuovo_voto
        else:
            print("voto non valido")


s = Studente("Gianlu", 18)

print(s.voto)
s.voto = -5
s.voto = 30
print(s.voto)            
        