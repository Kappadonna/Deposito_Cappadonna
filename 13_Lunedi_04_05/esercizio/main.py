from inserimento import inserimento_dati
from analisi import Giorno
from gestione_txt import crea_file_giorno

def main():
    input("Benvenuto! Premi Invio per iniziare l'inserimento dei dati di vendita.")
    # Crea un dizionario per memorizzare il totale delle vendite per ogni giorno
    totale_giorni = {}
    # Ciclo per inserire i dati di vendita per più giorni
    while True:
        g = int(input("Inserisci il giorno (1-31): "))
        mese = int(input("Inserisci il mese (1-12): "))
        anno = int(input("Inserisci l'anno: "))
        
        # Crea un'istanza della classe Giorno con i dati inseriti
        giorno = Giorno(g, mese, anno)
        print(f"Inserisci i dati di vendita per giorno {giorno.giorno}/{giorno.mese}/{giorno.anno}")
        vendite = inserimento_dati()
        # Assegna i dati di vendita all'istanza del giorno e analizza i dati
        giorno.dati = vendite
        giorno.analisi_dati(giorno.dati)
        giorno.valuta_vendite(giorno.dati)
        crea_file_giorno(giorno)
        
        # Calcola il totale delle vendite per il giorno e memorizzalo nel dizionario
        totale = giorno.analisi_dati(giorno.dati)[0]
        totale_giorni[giorno] = totale
        
        scelta = input("Vuoi inserire i dati per un altro giorno? (s/n): ").strip().lower()
        if scelta != 's':
            break
        
    # Crea un file di testo con i giorni che hanno vendite superiori alla media
    with open(f"13_Lunedi_04_05/esercizio/Giorni_con_vendite_superiori_alla_media.txt", "w") as file:
        for giorno, valore in totale_giorni.items():
            # Verifica se il totale delle vendite del giorno è superiore alla media dei totali dei giorni
            if valore > sum(totale_giorni.values()) / len(totale_giorni):
                # Scrive il giorno nel file
                file.write(f"Giorno: {giorno.giorno}/{giorno.mese}/{giorno.anno}\n")
                print(f"Giorno {giorno.giorno}/{giorno.mese}/{giorno.anno} con vendite superiori alla media: €{valore}")

        
    
    
if __name__ == "__main__":
    main()
    