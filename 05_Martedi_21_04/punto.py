class Punto:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def modifica_coordinate(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
    
    def distanza_origine(self):
        distanza = (self.x**2 + self.y**2) ** (0.5)
        return (distanza)
    
punto1 = Punto(10,5)

print(punto1.x)
print(punto1.y)

punto1.modifica_coordinate(32, 22)

print(punto1.x)
print(punto1.y)

print(punto1.distanza_origine())
