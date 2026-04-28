from abc import ABC, abstractmethod

class Impiegato(ABC):
    
    def __init__(self, nome, cognome, stipendio):
        self._nome = nome
        self._cognome = cognome
        self._stipendio = stipendio
        
    def get_info(self):
        return f"{self._nome} {self._cognome}"
    
    @abstractmethod
    def calcola_stipendio(self):
        pass
    

""" class Promozione(ABC):
    
    def __init__(self, n_vendite):
        self._n_vendite = n_vendite
        
    def promuovi(self):
        if self.n_vendite > 100:
            self._stipendio *= 1.35
        elif self.n_vendite > 50:
            self._stipendio *= 1.15
        else:
            self._stipendio = self._stipendio """
    

class ImpiegatoFisso(Impiegato):
        
    def calcola_stipendio(self):
        return self._stipendio
    

class ImpiegatoAProvvigione(Impiegato):
        
    def calcola_stipendio(self):
        return self._stipendio * 1.1
    
    
imp = ImpiegatoAProvvigione("Gianluca", "Cappadonna", 1000)
emp = ImpiegatoFisso("Johnluke", "Kwoman", 1000)

print(imp.get_info())
print(f"Stipendio: €{imp.calcola_stipendio()}")

print(emp.get_info())
print(f"Stipendio: €{emp.calcola_stipendio()}")
    

class SistemaInformatico:
    
    def __init__(self, impiegati = None):
        self._impiegati = impiegati if impiegati is not None else []
        
    def aggiungi_impiegati(self):
        scelta = input("Scegli il tipo di impiegato da aggiungere al sistema informatico: 1 per Impiegato fisso | 2 per Impiegato a provvigione")
        nome = input("Nome dell'impiegato: ")
        cognome = input("Cognome dell'impiegato: ")
        stipendio = float(input("Inserisci lo stipendio dell'impiegato"))
        
        match scelta:
            case "1":
                imp = ImpiegatoFisso(nome, cognome, stipendio)
            
            case "2":
                imp = ImpiegatoAProvvigione(nome, cognome, stipendio)
                
            case _:
                print("Scelta non valida")
                return
                
        self._impiegati.append(imp)
        print("Impiegato aggiunto correttamente")
                
    def stampa_info(self):

        for imp in self._impiegati:
            print(imp.get_info())
            print(f"Stipendio: €{imp.calcola_stipendio()}")
            

s = SistemaInformatico()

s.aggiungi_impiegati()
s.aggiungi_impiegati()
s.stampa_info()
            
    
            
