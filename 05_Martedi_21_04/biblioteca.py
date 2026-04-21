from libro import Libro

def create_libro(titolo, autore, pagine):
    libro = Libro(titolo, autore, pagine)
    return libro

class Biblioteca:
    
    def __init__(self, l):
        self.l = l

    def aggiungi_libro(self):
        while True:
            libro = []
            titolo = input("Quale libro vuoi inserire (Premi Q per uscire)")
            if titolo.lower() == "q":
                break
            autore = input("Chi è l'autore del libro ?")
            pagine = int(input(f"Quante pagine ha ha il libro ?"))
            libro.append(create_libro(titolo, autore, pagine))
            self.l.append(libro)
        
    def stampa_biblioteca(self):
        return self.l
        
        
biblioteca = Biblioteca([])  # <-- istanzia la classe
biblioteca.aggiungi_libro()
print(biblioteca.stampa_biblioteca())
        