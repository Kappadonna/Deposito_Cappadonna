class Animale:
    
    def __init__(self, nome):
        self.nome = nome
        
    def parla(self):
        print(f"{self.nome} fa un verso generico ")
        
class Cane(Animale):
    
    def parla(self):
        print(f"{self.nome} abbaia!")
        
class Gatto(Animale):
    
    def parla(self):
        print(f"{self.nome} miagola!")
        
a = Animale("Tommy")
c = Cane("Pino")
g = Gatto("Lino")

a.parla()
c.parla()
g.parla()


    
    