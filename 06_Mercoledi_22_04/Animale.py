class Animale:
    
    NUMERO_ANIMALI = 0                  # Attributo di classe
    
    def __init__(self, nome, specie):   # costruttore
        self.nome = nome
        self.specie = specie
        Animale.NUMERO_ANIMALI +=1      # Aumenta il contatore di classe
        
    @classmethod
    def quanti_animali(cls):            # metodo di classe, stampa numero di istanza create
        print(f"Numero di animali creati: {cls.NUMERO_ANIMALI}")
        
d = Animale("Ninna", "gatto")
g = Animale("Lino", "gatto")
p = Animale("Turi", "cane")

Animale.quanti_animali()
        
    