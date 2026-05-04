from analisi import Giorno
import inserimento


""" vendite = inserimento.inserimento_dati()
giorno = Giorno(4, 5, 2024, vendite) """


def crea_file_giorno(giorno):
    
    # Crea un file di testo con il nome "Giorno_giorno_mese_anno.txt"
    with open(f"13_Lunedi_04_05/esercizio/Giorno_{giorno.giorno}_{giorno.mese}_{giorno.anno}.txt", "w") as file:
        file.write(f"Giorno: {giorno.giorno}/{giorno.mese}/{giorno.anno}\n")
        # Scrive i dati di vendita nel file
        for valore in giorno.dati:
            file.write(str(valore) + "\n")
        
        # Scrive i risultati relativi al totale e alla medianel file 
        totale, media = giorno.analisi_dati()
        sopra_media = giorno.valuta_vendite()
        file.write(f"Totale: {totale}\n")
        file.write(f"Media: {media}\n")
        file.write(f"Vendite sopra la media: {sopra_media}\n")

    print(f"File 'Giorno_{giorno.giorno}_{giorno.mese}_{giorno.anno}.txt' creato con successo!")
    return file
    
# file = crea_file_giorno(giorno)