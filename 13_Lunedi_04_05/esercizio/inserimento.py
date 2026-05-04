# Modulo che gestisce l'inserimento dei dati

def inserimento_dati():
    
    # Chiede all'utente di inserire una serie di importi di vendita separati da spazi e li converte in una lista di numeri
    dati = (input("Inserisci una serie di importi di vendita separati da spazi (es. 100 200 300): "))
    try:
        lista_dati = dati.split()  # Divide la stringa in una lista di stringhe
        lista_dati = [float(x) for x in lista_dati]  # Converte ogni elemento della lista in un numero float
        return lista_dati 
    except ValueError:
        print("Errore: Assicurati di inserire solo numeri separati da spazi.")
        return inserimento_dati()  # Richiama la funzione per un nuovo tentativo
        
  

""" l = inserimento_dati()
print(l) """
