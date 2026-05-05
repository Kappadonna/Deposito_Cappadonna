from inventario import Inventario

class Cliente:
    
    def __init__(self, nome, cognome, username, password):
        self.__nome = nome
        self.__cognome = cognome
        self.__username = username
        self.__password = password
        self.storico_acquisti = []

    def acquista_articolo(self, inventario: Inventario, nome, quantità):
        articolo = inventario.cerca_articolo(nome)      
        if articolo is None:
            print(f"Articolo '{nome}' non trovato nell'inventario")
            return False
        if inventario.vendi_articolo(nome, quantità):   
            self.storico_acquisti.append({
                "articolo": articolo.nome,              
                "quantità": quantità,                   
                "prezzo_pagato": articolo.prezzo * quantità
            })
            return True
            
    def visualizza_storico(self):
        if len(self.storico_acquisti) > 0:
            print(self.storico_acquisti) 
        else:
            print(f"Nessun acquisto effettuato dal cliente {self.nome} {self.cognome}")
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cognome(self):
        return self.__cognome
    
    @property
    def username(self):
        return self.__username
    
    @property
    def password(self):
        return self.__password
    
    def __str__(self):
        return f"Cliente: {self.nome} {self.cognome}, Username: {self.username}"
    
