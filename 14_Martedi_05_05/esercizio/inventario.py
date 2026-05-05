class Articolo:
    
    def __init__(self, nome, prezzo, quantità):
        self.__nome = nome
        self.__prezzo = prezzo
        self.__quantità = quantità
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def prezzo(self):
        return self.__prezzo
    
    @prezzo.setter
    def prezzo(self, nuovo_prezzo):
        self.__prezzo = nuovo_prezzo
    
    @property
    def quantità(self):
        return self.__quantità
    
    @quantità.setter
    def quantità(self, nuova_quantità):
        self.__quantità = nuova_quantità
    
    def __str__(self):
        return f"Articolo: {self.nome}, Prezzo: {self.prezzo}, Quantità: {self.quantità}"
    
    
class Inventario:
    
    def __init__(self, guadagno_totale = 0):
        self.articoli = []
        self.registro_vendite = []
        self.guadagno_totale = guadagno_totale
        
        
    def aggiungi_articolo(self, nome, prezzo, quantità):
        articolo = Articolo(nome, prezzo, quantità)
        self.articoli.append(articolo)
        return True
        
    def rimuovi_articolo(self, nome):
        for articolo in self.articoli:
            if articolo.nome == nome:
                self.articoli.remove(articolo)
                return True  
        print(f"L' articolo {nome} non è presente nell'inventario")
        return False
    
    def aggiorna_articolo(self, nome, prezzo, quantità):
        for articolo in self.articoli:
            if articolo.nome == nome:
                articolo.prezzo = prezzo
                articolo.quantità = quantità
                return True       
        print(f"L'articolo {nome} non è presente nell'inventario")
        return False
                
    def vendi_articolo(self, nome, quantità):
        for articolo in self.articoli:
            if articolo.nome == nome and articolo.quantità >= quantità:
                articolo.quantità -= quantità
                self.guadagno_totale += (articolo.prezzo * quantità)
                self.registro_vendite.append({
                    "articolo": articolo.nome,
                    "quantità": quantità,
                    "incasso": articolo.prezzo * quantità})
                return True
        print(f"Quantità non disponibile per articolo selezionato, max quantità disponibile per Articolo {nome} è di {articolo.quantità}")
        return False
    
    def visualizza(self):
        for articolo in self.articoli:
            print(articolo)
            
    def cerca_articolo(self, nome):
        for articolo in self.articoli:
            if articolo.nome == nome:
                return articolo
        return None