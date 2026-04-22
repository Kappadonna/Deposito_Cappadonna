class Ristorante:
    
    APERTO = False
    
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        
    def descrivi_ristorante(self):
        print(f"Il ristorante {self.nome} ")