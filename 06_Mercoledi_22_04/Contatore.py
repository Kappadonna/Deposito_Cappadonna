class Contatore:
    
    NUMERO_ISTANZE = 0                                              # Attributo di classe
    
    def __init__(self):                                             # Costruttore che incrementa valore attributo di classe
        Contatore.NUMERO_ISTANZE +=1
        
    @classmethod
    def mostra_numero_istanze(cls):                                 # metodo di classe, che funziona sulla classe stessa
        print(f"Sono state create {cls.NUMERO_ISTANZE} istanze")
        
c1 = Contatore()
c2 = Contatore()

Contatore.mostra_numero_istanze()