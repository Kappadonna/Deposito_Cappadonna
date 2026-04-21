class Libro:
    
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        
    def descrizione(self):
        print(f"Il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine")
        

libro1 = Libro("Decameron", " Giovanni Boccaccio", "423")

libro1.descrizione()