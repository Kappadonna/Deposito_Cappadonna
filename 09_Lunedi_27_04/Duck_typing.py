# Duck Typing

class Cerchio:
    
    def disegna(self):
        print("Fai un cerchio")
        
class Rettangolo:
    
    def disegna(self):
        print("Fai un rettangolo")
        
def disegna_figura(figura):
    figura.disegna()
    
figure = [Cerchio(), Rettangolo()]

for figura in figure:
    disegna_figura(figura)