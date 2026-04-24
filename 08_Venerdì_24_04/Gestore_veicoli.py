class Veicolo:
    def __init__(self, marca, modello, anno, accensione):
        
        self._marca = marca
        self._modello = modello
        self._anno = anno
        self._accensione = accensione
        
    def accendi(self):
        self._accensione = True
    
    def spegni(self):
        self._accensione = False
    
