from Agenzia import Agenzia
from Veicolo import Automobile, Furgone
from GestioneDati import salva_flotta, carica_flotta, salva_storico, carica_storico


def crea_veicolo(agenzia):
    # Crea un nuovo veicolo chiedendo i dati all'utente
    print("\n--- Creazione veicolo ---")
    tipo = input("Tipo (1 per Automobile/ 2 per Furgone): ")
    targa = input("Targa: ")
    marca = input("Marca: ")
    modello = input("Modello: ")
    anno = int(input("Anno: "))
    prezzo = float(input("Prezzo giornaliero: "))
    disponibile = True
    
    if tipo == "1":
        n_posti = int(input("Numero di posti: "))
        veicolo = Automobile(targa, marca, modello, anno, prezzo, disponibile, n_posti)
    elif tipo == "2":
        capacita = float(input("Capacità in kg: "))
        veicolo = Furgone(targa, marca, modello, anno, prezzo, disponibile, capacita)
    else:
        print("Tipo non valido.")
        return
    
    # Aggiunge il veicolo alla flotta in memoria e salva lo stato aggiornato nel CSV
    agenzia.aggiungi_veicolo(veicolo)
    salva_flotta(agenzia.flotta)


def noleggia_veicolo(agenzia):
    print("\n--- Noleggio veicolo ---")
    # Mostra solo i disponibili per chiarezza
    veicoli_disponibili = [v for v in agenzia.flotta if v.disponibile]
    if not veicoli_disponibili:
        print("Nessun veicolo disponibile.")
        return

    for v in veicoli_disponibili:
        print(v.descrizione())
    
    targa = input("Inserisci la targa: ")
    cliente = input("Nome cliente: ")
    giorni = int(input("Numero di giorni: "))
    
    veicolo = agenzia.cerca_veicolo(targa)
    if veicolo and veicolo.disponibile:
        costo_totale = veicolo.calcola_costo(giorni)
        # Esegue il noleggio (cambia disponibile in False in memoria)
        if agenzia.noleggia_veicolo(targa, cliente, giorni):
            # Scrive lo stato aggiornato (False) nel CSV
            salva_storico(agenzia.storico_noleggi)
            salva_flotta(agenzia.flotta) 
    else:
        print("Operazione non riuscita: veicolo non trovato o già occupato.")

def restituisci_veicolo(agenzia):
    # Restituisce un veicolo chiedendo la targa e aggiorna la disponibilità
    targa = input("Inserisci targa per la restituzione: ")
    if agenzia.restituisci_veicolo(targa):
        salva_flotta(agenzia.flotta)

def modifica_veicolo(agenzia):
    # Modifica prezzo e/o disponibilità di un veicolo esistente
    targa = input("Targa del veicolo da modificare: ")
    nuovo_prezzo = input("Nuovo prezzo (premi invio per saltare): ")
    nuova_disp = input("Disponibile? (s/n, premi invio per saltare): ")
    
    prezzo = float(nuovo_prezzo) if nuovo_prezzo else None
    disp = None
    if nuova_disp.lower() == 's': disp = True
    elif nuova_disp.lower() == 'n': disp = False
    
    if agenzia.modifica_veicolo(targa, prezzo, disp):
        salva_flotta(agenzia.flotta)

def rimuovi_veicolo(agenzia):
    # Rimuove un veicolo dalla flotta in base alla targa
    targa = input("Targa del veicolo da rimuovere: ")
    if agenzia.rimuovi_veicolo(targa):
        salva_flotta(agenzia.flotta)
        
def menu_analisi(agenzia):
    # Menu per visualizzare la flotta, filtrare per tipo o vedere lo storico dei noleggi
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
    # Carica la flotta e lo storico dei noleggi all'avvio del programma
    agenzia.flotta = carica_flotta()
    agenzia.storico_noleggi = carica_storico()
    
    while True:
        print(f"\n--- Benvenuti in {agenzia.nome} ---")
        scelta = input("1. Crea veicolo\n2. Noleggia veicolo\n3. Restituisci veicolo\n4. Modifica veicolo\n5. Rimuovi veicolo\n6. Analisi\n7. Esci\nScelta: ")
        
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
                break
            case _: 
                print("Scelta non valida.")

if __name__ == "__main__":
    main()