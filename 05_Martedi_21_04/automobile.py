class Automobile:
    
    NUMERO_RUOTE = 4                    # attributo di classe
    
    def __init__(self, marca, modello): # costruttore
        self.marca = marca              # attributo di istanza
        self.modello = modello          # attributo di istanza
        
    def stampa_info(self):
        print(f"L'automobile è una {self.marca} {self.modello}")
        
auto1 = Automobile("Fiat", "Panda")
auto2 = Automobile("Smart", "ForTwo")

auto1.stampa_info()
auto2.stampa_info()

print(auto2.NUMERO_RUOTE)
print(auto2.marca)
print(auto2.modello)

auto1.marca = "Nissan"
auto1.modello = "Micra"

auto1.stampa_info()
        
    