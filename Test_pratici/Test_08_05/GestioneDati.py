import csv
import os
from Veicolo import Automobile, Furgone


FILE_FLOTTA = "flotta.csv"
FILE_STORICO = "storico_noleggi.csv"

HEADER_FLOTTA = ["tipo", "targa", "marca", "modello", "anno", "prezzo_giornaliero", "disponibile", "extra"]
HEADER_STORICO = ["targa", "cliente", "giorni", "costo"]

def salva_flotta(flotta):
    # Sovrascrive il file CSV con tutti i veicoli della flotta.
    with open(FILE_FLOTTA, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(HEADER_FLOTTA) # Scrive l'header
        for v in flotta:
            # Determina il tipo e l'attributo extra (n_posti o capacità) in base alla classe dell'oggetto
            tipo = "Automobile" if isinstance(v, Automobile) else "Furgone"
            extra = v.n_posti if tipo == "Automobile" else v.capacità
            # Scrive la riga con tutti gli attributi, incluso il tipo e l'extra specifico
            writer.writerow([tipo, v.targa, v.marca, v.modello, v.anno, v.prezzo_giornaliero, v.disponibile, extra])


def carica_flotta():
    # Legge il CSV e ricostruisce gli oggetti veicolo.
    flotta = []
    if not os.path.exists(FILE_FLOTTA):
        return flotta
    
    # Legge il file CSV, salta l'header e crea oggetti veicolo in base al tipo specificato nella prima colonna
    with open(FILE_FLOTTA, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        try:
            next(reader) # Salta header
        except StopIteration:
            return flotta

        # Per ogni riga, verifica il tipo e crea l'oggetto corrispondente (Automobile o Furgone) con i dati letti
        for row in reader:
            # Validazione semplice per assicurarsi che la riga abbia abbastanza colonne e che l'anno sia un numero
            if not row or len(row) < 8: continue
            tipo, targa, marca, modello, anno, prezzo, disponibile, extra = row
            if not anno.isdigit(): continue
            
            # Converte la stringa "True"/"False" in booleano per l'attributo disponibile
            is_disp = disponibile == 'True'
            if tipo == "Automobile":
                v = Automobile(targa, marca, modello, int(anno), float(prezzo), is_disp, int(extra))
            else:
                v = Furgone(targa, marca, modello, int(anno), float(prezzo), is_disp, float(extra))
            # Aggiunge l'oggetto creato alla lista della flotta
            flotta.append(v)
    return flotta

def salva_storico(lista_storico):
    # Sovrascrive il file storico con i dati attuali della memoria.
    with open(FILE_STORICO, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(HEADER_STORICO)
        for n in lista_storico:
            # Assumendo che n sia un dizionario come gestito in Agenzia.py
            # { "targa": ..., "cliente": ..., "giorni": ..., "costo": ... }
            writer.writerow([n['targa'], n['cliente'], n['giorni'], n['costo']])

def carica_storico():
    # Carica lo storico dal file CSV all'inizio della sessione.
    storico = []
    if not os.path.exists(FILE_STORICO):
        return storico
    
    # Legge il file CSV, salta l'header e ricostruisce la lista dello storico con dizionari per ogni noleggio
    with open(FILE_STORICO, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        try:
            next(reader) # Salta header
        except StopIteration:
            return storico

        # Per ogni riga, crea un dizionario con i dati del noleggio e lo aggiunge alla lista dello storico
        for row in reader:
            if not row or len(row) < 4: continue
            targa, cliente, giorni, costo = row
            storico.append({
                "targa": targa,
                "cliente": cliente,
                "giorni": int(giorni),
                "costo": float(costo)
            })
    return storico