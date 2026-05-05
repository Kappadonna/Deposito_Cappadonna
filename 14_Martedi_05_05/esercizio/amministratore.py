from inventario import Inventario

class Amministratore:
    
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        
    def visualizza_inventario(self, inventario : Inventario):
        inventario.visualizza()
        
    def visualizza_vendite(self, inventario: Inventario):
        if not inventario.registro_vendite:
            print("Nessuna vendita registrata.")
            return
        for vendita in inventario.registro_vendite:
            print(f"Articolo: {vendita['articolo']}, Quantità: {vendita['quantità']}, Incasso: {vendita['incasso']}€")
    
    def visualizza_guadagno(self, inventario: Inventario):
        print(f"Guadagno totale: {inventario.guadagno_totale:.2f}€")
        
    def aggiungi_articolo(self, inventario: Inventario, nome, prezzo, quantità):
        inventario.aggiungi_articolo(nome, prezzo, quantità)
        
    def rimuovi_articolo(self, inventario: Inventario, nome):
        inventario.rimuovi_articolo(nome)
        
    def aggiorna_articolo(self, inventario: Inventario, nome, prezzo, quantità):
        inventario.aggiorna_articolo(nome, prezzo, quantità)
        
    @property
    def username(self):
        return self.__username
    
    @property
    def password(self):
        return self.__password
    
    def __str__(self):
        return f"Amministratore: {self.username}"