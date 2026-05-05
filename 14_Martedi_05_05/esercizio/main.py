from inventario import Inventario
from cliente import Cliente
from amministratore import Amministratore
from scrittura_file import (carica_articoli, salva_articoli,
                        carica_clienti, salva_clienti,
                        carica_vendite, salva_vendite)


inventario = Inventario()
inventario.articoli = carica_articoli()
registro, guadagno = carica_vendite()
inventario.registro_vendite = registro
inventario.guadagno_totale = guadagno
lista_clienti = carica_clienti()

amministratore_1 = Amministratore("Kappadonna", "abcd")
amministratore_2 = Amministratore("Gianluca", "1234")

lista_amministratori = [amministratore_1, amministratore_2]

def registra_cliente(lista_clienti):
    nome = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    username = input("Inserisci l'username: ")
    password = input("Inserisci una password: ")
    
    for c in lista_clienti:
        if c.username == username:
            print("Username già in uso, scegline un altro.")
            return
    
    lista_clienti.append(Cliente(nome, cognome, username, password))
    print("Registrazione avvenuta con successo.")
    salva_clienti(lista_clienti)
        

def login():
    username = input("Inserisci l'username: ")
    password = input("Inserisci la password: ")
    
    for amministratore in lista_amministratori:
        if amministratore.username == username and amministratore.password == password:
            return amministratore
    
    for cliente in lista_clienti:
        if cliente.username == username and cliente.password == password:
            return cliente
        
    return None
    
    
def menu_cliente(cliente, inventario):
    while True:
        scelta = input("Cosa vuoi fare? \n 1 per visualizzare gli articoli disponibili \n 2 per acquistare un articolo \n 3 per vedere lo storico degli acquisti \n 4 per uscire: ")
        match scelta:
            case "1":
                inventario.visualizza()
            case "2":
                nome = input("Inserisci il nome dell'articolo da acquistare: ")
                quantità = int(input("Inserisci la quantità dell'articolo da acquistare: "))
                if cliente.acquista_articolo(inventario, nome, quantità):
                    salva_articoli(inventario)
                    salva_vendite(inventario)
            case "3":
                cliente.visualizza_storico()
            case "4":
                print("Uscita dal menù cliente in corso..")
                return False
            case _:
                print("Scelta non valida")
            
        
    
def menu_amministratore(amministratore, inventario):
    while True:
        scelta = input("Cosa vuoi fare? \n 1 per visualizzare gli articoli disponibili \n 2 per visualizzare le vendite \n 3 per visualizzare guadagni \n 4 aggiungere / rimuovere / aggiornare gli articoli \n 5 per uscire: ")
        match scelta:
            case "1":
                inventario.visualizza()
            case "2":
                amministratore.visualizza_vendite(inventario)
            case "3":
                amministratore.visualizza_guadagno(inventario)
            case "4":
                selezione = input("Cosa vuoi fare ? \n 1 per aggiungere un articolo \n 2 per rimuovere un articolo \n 3 per aggiornare un articolo: ")
                match selezione:
                    case "1":
                        nome = input("Inserisci il nome dell'articolo da aggiungere: ")
                        prezzo = float(input("Inserisci il prezzo dell'articolo: € "))
                        quantità = int(input("Inserisci la quantità da aggiungere: "))
                        amministratore.aggiungi_articolo(inventario, nome, prezzo, quantità)
                        salva_articoli(inventario)
                    case "2":
                        nome = input("Inserisci il nome dell'articolo da rimuovere: ")
                        amministratore.rimuovi_articolo(inventario, nome)
                        salva_articoli(inventario)
                    case "3":
                        nome = input("Inserisci il nome dell'articolo da aggiornare: ")
                        prezzo = float(input("Inserisci il prezzo dell'articolo da aggiornare: € "))
                        quantità = int(input("Inserisci la quantità da aggiornare: "))   
                        amministratore.aggiorna_articolo(inventario, nome, prezzo, quantità)
                        salva_articoli(inventario)
                    case _:
                        print("Scelta non valida")
            case "5":
                print("Uscita dal menù amministratore in corso in corso..")
                return False          
            
            
def main():
    while True:
        scelta = input("Cosa vuoi fare?\n 1 per Log-in\n 2 per registrazione\n 3 per uscire: ")
        match scelta:
            case "1":
                utente = login()
                if utente is None:
                    print("Credenziali errate, riprova.")
                    continue
                if isinstance(utente, Amministratore):
                    menu_amministratore(utente, inventario)
                elif isinstance(utente, Cliente):
                    menu_cliente(utente, inventario)
            case "2":
                registra_cliente(lista_clienti)
                print("Ora effettua il login.")
            case "3":
                print("Arrivederci!")
                break    
                        
                        
if __name__ == "__main__":
    main()
                        