class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        
    def __str__(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}" 
    
    def __repr__(self):
        return f"Libro(titolo = {self.titolo}, autore = {self.autore})"
    
        
l1 = Libro("Decameron", "Boccaccio")

print(l1)
print(repr(l1))

class Squadra:
    
    def __init__(self, giocatori: list[str]):
        self.giocatori = giocatori
        
    def __len__(self):
        return len(self.giocatori)
    
    
inter = Squadra(["Lautaro", "Dimarco", "Bastoni", "Diouf", "Sucic", "Chalanoglu"])

print(len(inter))


class Prodotto:
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo
        
    def __eq__(self, other):
        return self.nome == other.nome and self.prezzo == other.prezzo
    
p1 = Prodotto("pc", 250)
p2 = Prodotto("pc", 250)
p3 = Prodotto("Maglietta", 25)

print(p1 == p2)
print(p1 == p3)


class Persona:
    
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        
    def __getattribute__(self, attributo):
        print(f"Sto accedendo all'attributo {attributo}") # aggiunge una logica
        return super().__getattribute__(attributo)
    
p = Persona("Gianluca", 26)

print(p.nome)
print(p.eta)