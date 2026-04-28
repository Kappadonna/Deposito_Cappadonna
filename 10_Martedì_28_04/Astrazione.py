from abc import ABC, abstractmethod

# Classe astratta, non verrà mai chiamata per creare istanze Animale, serve come base per le altre classi
class Animale(ABC):
    # Metodo astratto, DEVE ESSERE PRESENTE nelle classi figlie
    @abstractmethod
    def muovi(self): # DEVE AVERE PASS
        pass
    

class Cane(Animale):
    
    def muovi(self):
        print("Corri")
        

class Pesce(Animale):
    def muovi(self):
        print("Nuota")
        
        