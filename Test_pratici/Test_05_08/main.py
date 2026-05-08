from agenzia import Agenzia
from veicolo import Automobile, Furgone


def crea_veicolo(agenzia):
    print("Creazione veicolo:")
    tipo = input("Tipo (1 per Automobile/ 2 per Furgone): ")
    targa = input("Targa: ")
    marca = input("Marca: ")
    modello = input("Modello: ")
    anno = int(input("Anno: "))
    prezzo = float(input("Prezzo giornaliero: "))
    disponibile = "True"
    match tipo:
        case "1":
            n_posti = int(input("Numero di posti: "))
            veicolo = Automobile(targa, marca, modello, anno, prezzo, disponibile, n_posti)
        case "2":
            capacita = float(input("Capacità in kg: "))
            veicolo = Furgone(targa, marca, modello, anno, prezzo, disponibile, capacita)
        case _:
            print("Tipo non valido.")
            return
    agenzia.aggiungi_veicolo(veicolo)
    
    
def noleggia_veicolo(agenzia):
    print("Noleggio veicolo:")
    veicoli_disponibili = [v for v in agenzia.flotta if v.disponibile]
    if not veicoli_disponibili:
        print("Nessun veicolo disponibile per il noleggio.")
        return
    print("Veicoli disponibili:")
    for v in veicoli_disponibili:
        print(v.descrizione())
    targa = input("Targa: ")
    cliente = input("Nome cliente: ")
    giorni = int(input("Giorni di noleggio: "))
    agenzia.noleggia_veicolo(targa, cliente, giorni)
    
def restituisci_veicolo(agenzia):
    print("Restituzione veicolo:")
    targa = input("Targa: ")
    agenzia.restituisci_veicolo(targa)  
    
def modifica_veicolo(agenzia):
    print("Modifica veicolo:")
    targa = input("Targa: ")
    nuovo_prezzo = input("Nuovo prezzo giornaliero (lascia vuoto per non modificare): ")
    nuova_disponibilita = input("Nuova disponibilità (True/False, lascia vuoto per non modificare): ")
    nuovo_prezzo = float(nuovo_prezzo) if nuovo_prezzo else None
    if nuova_disponibilita:
        if nuova_disponibilita.lower() == "true":
            nuova_disponibilita = True
        elif nuova_disponibilita.lower() == "false":
            nuova_disponibilita = False
        else:
            print("Valore di disponibilità non valido. Deve essere True o False.")
            return
    else:
        nuova_disponibilita = None
    agenzia.modifica_veicolo(targa, nuovo_prezzo, nuova_disponibilita)
    
def rimuovi_veicolo(agenzia):
    print("Rimozione veicolo:")
    targa = input("Targa: ")
    agenzia.rimuovi_veicolo(targa)
    
def menu_analisi(agenzia):
    scelta = input("Scegli un'opzione:\n1. Visualizza flotta\n2. Visualizza per tipo\n3. Visualizza storico noleggi\n4. Torna al menu principale\n")
    match scelta:
        case "1":
            agenzia.visualizza_flotta()
        case "2":
            tipo = input("Tipo (Automobile/Furgone): ")
            agenzia.analizza_per_tipo(tipo)
        case "3":
            agenzia.visualizza_storico_noleggi()
        case "4":
            return
        case _:
            print("Scelta non valida.")
            

def main():
    agenzia = Agenzia("Masamune Rent")
    while True:
        scelta = input("Scegli un'opzione:\n1. Crea veicolo\n2. Noleggia veicolo\n3. Restituisci veicolo\n4. Modifica veicolo\n5. Rimuovi veicolo\n6. Analizza flotta\n7. Esci\n")
        match scelta:
            case "1":
                crea_veicolo(agenzia)
            case "2":
                noleggia_veicolo(agenzia)
            case "3":
                restituisci_veicolo(agenzia)
            case "4":
                modifica_veicolo(agenzia)
            case "5":
                rimuovi_veicolo(agenzia)
            case "6":
                menu_analisi(agenzia)
            case "7":
                print("Arrivederci!")
                break
            case _:
                print("Scelta non valida.")
                
                
if __name__ == "__main__":
    main()
            
            
