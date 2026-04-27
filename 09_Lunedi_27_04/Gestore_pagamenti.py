import random

class Utente:
    
    # costruttore con nome obbligatorio, saldo non obbligatorio
    def __init__(self, nome, saldo = None):
        self.nome = nome
        self.saldo = saldo
    
    # Metodo setter per impostare saldo
    def set_saldo(self):
        self.saldo = random.randint(1,100)
        
class MetodoPagamento:
    
    # Costruttore con importo non obbligatorio
    def __init__(self, importo= None):
        self.importo = importo
    
    # Metodo per effettuare pagamento
    def effettua_pagamento(self):
        print(f"Stai effettuando un pagamento di €{self.importo}")
        return self.importo
    
class CartaDiCredito(MetodoPagamento):
    
    def __init__(self, importo = None):
        super().__init__(importo)
    
    # Metodo per effettuare pagamento con commissione del 2%   
    def effettua_pagamento(self):
        print(f"Stai effettuando un pagamento di €{self.importo} con carta di credito, commisione 2%")
        totale = self.importo * 1.02
        return totale
        
class Paypal(MetodoPagamento):
    
    def __init__(self, importo = None):
        super().__init__(importo)

    # Metodo per effettuare pagamento con commissione dell'1%    
    def effettua_pagamento(self):
        print(f"Stai effettuando un pagamento di €{self.importo} con paypal, commissione 1%")
        totale = self.importo * 1.01
        return totale
        
class BonificoBancario(MetodoPagamento):
    
    def __init__(self, importo = None):
        super().__init__(importo)
    
    # Metodo per effettuare pagamento con commissione del 5%
    def effettua_pagamento(self):
        print(f"Stai effettuando un pagamento di €{self.importo} con bonifico bancario, commissione 5%")
        totale = self.importo * 1.05
        return totale
        
class GestorePagamenti:
    
    def __init__(self, importo = None):
        self.importo = importo
    
    # Metodo che seleziona in modo randomico l'importo da dover pagare    
    def set_importo(self):
        self.importo = random.randint(1, 25)
    
    # Metodo che fa pagare l'utente se il saldo disponibile lo permette
    def fai_pagare(self, nickname):
        
        # Inizializza l'utente e gli crea un saldo disponibile in maniera randomica
        utente = Utente(nickname)
        utente.set_saldo()
        # Print per debug
        print([utente.nome, utente.saldo])
        
        # Seleziona importo che l'utente deve pagare in maniera randomica
        self.set_importo()
        # Print per debug
        print(self.importo)
        
        # Chiede all'utente la modalità di pagamento
        metodo = input("Seleziona metodo di pagamento: 1 per Carta di Credito | 2 per Paypal | 3 per Bonifico Bancario: ")
        
        match metodo:
                
            case "1":
                # Inizializza lo strumento con il relativo tasso di commissione
                strumento = CartaDiCredito(self.importo)
                
            case "2":
                # Inizializza lo strumento con il relativo tasso di commissione
                strumento = Paypal(self.importo)
                
            case "3":
                # Inizializza lo strumento con il relativo tasso di commissione
                strumento = BonificoBancario(self.importo)
                                            
            case _:
                print("Metodo non valido")
                return

        # Richiama il metodo effettua_pagamento delle sottoclassi che restituiscono il totale compreso di commissioni
        tot = strumento.effettua_pagamento()

        # Confronta il totale con il saldo dell'utente per ultimare il pagamento
        if tot > utente.saldo:
            print("Saldo insufficiente dell'utente")
        else:
            utente.saldo -= tot
            print("Nuovo saldo:", utente.saldo)
        
        
        
        
g = GestorePagamenti()

g.fai_pagare("Gianluca")