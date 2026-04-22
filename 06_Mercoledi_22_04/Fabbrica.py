class Prodotto:
    
    def __init__(self, nome:str, costo_produzione: int, prezzo_vendita: int): # costruttore
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        
    def descrizione(self):  # output stringa per descrizione
        print(f"{self.nome} è un prodotto con un costo di produzione di €{self.costo_produzione} e un prezzo di vendita di €{self.prezzo_vendita}")
        
    def calcola_profitto(self): # metodo per calcolare profitto
        return (self.prezzo_vendita - self.costo_produzione)
    

class Elettronica(Prodotto):
    
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia:int):
        super().__init__(nome, costo_produzione, prezzo_vendita) # prende gli attributi dalla classe super()
        self.garanzia = garanzia
        
    def descrizione(self):
        super().descrizione() # utilizza funzione descrizione della calsse super()
        print(f"{self.nome} è un prodotto di Elettronica con {self.garanzia} anni di garanzia") # aggiunge descrizione personalizzata
        
    
class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiali: list[str]):
        super().__init__(nome, costo_produzione, prezzo_vendita) # prende gli attributi dalla classe super()
        self.materiali = materiali
        
    def descrizione(self):
        super().descrizione() # utilizza funzione descrizione della calsse super()
        print(f"{self.nome} è un capo di abbigliamento realizzato con {", ".join(self.materiali)}") # aggiunge descrizione personalizzata
        
    
    


class Fabbrica:
    
    def __init__(self, inventario: dict): # costruttore
        self.inventario = inventario
        
    def aggiungi_prodotto(self, prodotto: Prodotto): # il prodotto è un'istanza della classe prodotto
        if prodotto.nome not in self.inventario: # controlla che l'attributo nome del prodotto non sia già nel dizionario
            self.inventario[prodotto.nome] = 0 # se non c'è lo aggiunge
        self.inventario[prodotto.nome] += 1 # aggiunge +1 alla al valore che fa riferimento alla chiava nome del prodotto

    def vendi_prodotto(self, prodotto: Prodotto):
        if prodotto.nome  in self.inventario and self.inventario[prodotto.nome ] > 0: # se l'ttributo nome del prodotto è nell'inventario e il valore corrispondente è meggiore di 0
            self.inventario[prodotto.nome] -= 1 # rimuove un'unità perchè l'articolo è venduto
        
    def resi_prodotto(self, prodotto: Prodotto): # funzionamento uguale a aggiungi prodotto
        if prodotto.nome  not in self.inventario:
            self.inventario[prodotto.nome] = 0
        self.inventario[prodotto.nome] += 1
        
    def magazzino(self): # serve a stampare le giacenza del magazzino
        print(self.inventario)
        
        
pc = Elettronica("Computer", 150, 500, 3)
pc.descrizione()
print(pc.calcola_profitto())
    
    
tshirt = Abbigliamento("Maglietta", 5, 30, ["cotone", "poliestere"])
tshirt.descrizione()
print(tshirt.calcola_profitto())

pantalone = Abbigliamento("Pantalone", 10, 50, ["cotone"])
jeans = Abbigliamento("Jeans", 7, 30, ["Denim"])
        
f = Fabbrica({})

f.aggiungi_prodotto(pc)
f.vendi_prodotto(pc)
f.aggiungi_prodotto(pc)
f.aggiungi_prodotto(pc)

f.aggiungi_prodotto(tshirt)
f.aggiungi_prodotto(pantalone)
f.resi_prodotto(jeans)

f.magazzino()