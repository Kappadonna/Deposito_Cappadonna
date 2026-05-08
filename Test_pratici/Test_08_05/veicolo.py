from abc import ABC, abstractmethod

class Veicolo(ABC):
    
    def __init__(self, targa, marca, modello, anno, prezzo_giornaliero, disponibile):
        self._targa = targa
        self._marca = marca
        self._modello = modello
        self._anno = anno
        self._prezzo_giornaliero = prezzo_giornaliero
        self._disponibile = disponibile
        
    @abstractmethod
    def descrizione(self):
        pass
    
    @abstractmethod
    def calcola_costo(self, giorni):
        pass
    
    @property
    def targa(self):
        return self._targa
    
    @property
    def marca(self):
        return self._marca
    
    @property
    def modello(self):
        return self._modello
    
    @property
    def anno(self):
        return self._anno
    
    @property
    def prezzo_giornaliero(self):
        return self._prezzo_giornaliero
    
    @prezzo_giornaliero.setter
    def prezzo_giornaliero(self, prezzo):
        if prezzo > 0:
            self._prezzo_giornaliero = prezzo
    
    @property
    def disponibile(self):
        return self._disponibile
    
    @disponibile.setter
    def disponibile(self, valore):
        if isinstance(valore, bool):
            self._disponibile = valore
    
    def __str__(self):
        return f"Targa: {self.targa}, Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Prezzo giornaliero: {self._prezzo_giornaliero}, Disponibile: {self.disponibile}"
    
    def to_list(self):
        return [self.targa, self.marca, self.modello, self.anno, self.prezzo_giornaliero, self.disponibile]

    
class Automobile(Veicolo):
    
    def __init__(self, targa, marca, modello, anno, prezzo_giornaliero, disponibile, n_posti):
        super().__init__(targa, marca, modello, anno, prezzo_giornaliero, disponibile)
        self.__n_posti = n_posti
        
    def descrizione(self):
        return f"{self.__class__.__name__} {self.marca} {self.modello} con {self.n_posti} posti, prezzo giornaliero €{self.prezzo_giornaliero}"
    
    
    def calcola_costo(self, giorni):
        if giorni > 7:
            return self.prezzo_giornaliero * giorni * 0.9 # sconto del 10% per noleggi superiori a 7 giorni
        return self.prezzo_giornaliero * giorni
    
    @property
    def n_posti(self):
        return self.__n_posti
    
    @n_posti.setter
    def n_posti(self, nuovi_posti):
        if 2 <= nuovi_posti <= 5:
            self.__n_posti = nuovi_posti
        else:
            print("Numero di posti non valido. Deve essere tra 2 e 5.")
            
    def to_list(self):
        return super().to_list() + [self.n_posti]
            
class Furgone(Veicolo):
    
    def __init__(self, targa, marca, modello, anno, prezzo_giornaliero, disponibile, capacità):
        super().__init__(targa, marca, modello, anno, prezzo_giornaliero, disponibile)
        self.__capacità = capacità
        
    def descrizione(self):
        return f"{self.__class__.__name__} {self.marca} {self.modello} con capacità di {self.capacità} kg, prezzo giornaliero €{self.prezzo_giornaliero}"
    
    def calcola_costo(self, giorni):
        if giorni > 7:
            return self.prezzo_giornaliero * giorni * 0.85 # sconto del 15% per noleggi superiori a 7 giorni
        return self.prezzo_giornaliero * giorni
    
    @property
    def capacità(self):
        return self.__capacità
    
    @capacità.setter
    def capacità(self, nuova_capacità):
        if 500 <= nuova_capacità <= 3000:
            self.__capacità = nuova_capacità
        else:
            print("Capacità non valida. Deve essere tra 500 e 3000 kg.")
            
    def to_list(self):
        return super().to_list() + [self.capacità]
    
    
a = Automobile("AB123CD", "Fiat", "Panda", 2020, 30, True, 5)
print(a)
print(a.descrizione())
print(f"Costo per 5 giorni: €{a.calcola_costo(5)}")
print(f"Costo per 10 giorni: €{a.calcola_costo(10)}")
lista_automobile = a.to_list()
print(lista_automobile)

f = Furgone("EF456GH", "Mercedes", "Sprinter", 2019, 80, True, 1500)
print(f)
print(f.descrizione())
print(f"Costo per 5 giorni: €{f.calcola_costo(5)}")
print(f"Costo per 10 giorni: €{f.calcola_costo(10)}")
lista_furgone = f.to_list()
print(lista_furgone)
    