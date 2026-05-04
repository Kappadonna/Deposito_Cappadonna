# Modulo che gestisce le analisi dei dati

import inserimento
import datetime

class Giorno:
    def __init__(self, giorno, mese, anno, dati = None):
        self.__giorno = giorno
        self.__mese = mese
        self.__anno = anno
        self.dati = dati #if dati is not None else inserimento.inserimento_dati()

    def analisi_dati(self, dati):
        # verifica che la lista non sia vuota
        if len(self.dati) == 0:
            print("Nessun dato da analizzare.")
            return
        
        # calcola il totale e la media dei dati della lista
        totale = sum(self.dati)
        media = totale / len(self.dati)
        
        print(f"Il totale delle vendite è €{totale}")
        print(f"La media delle vendite è €{media}")
        
        return (totale, media)

    def valuta_vendite(self, dati):
        # crea lista delle vendite sopra la media
        sopra_media = [x for x in self.dati if x > sum(self.dati) / len(self.dati)]
        
        if len(sopra_media) == 0:
            print("Nessuna vendita sopra la media.")
        else:
            print("Vendite sopra la media:")
            for vendita in sopra_media:
                print(f"€{vendita}")
            return sopra_media
        
    @property
    def giorno(self):
        return self.__giorno
    
    @giorno.setter
    def giorno(self, value):
        if 1 <= value <= 31:
            self.__giorno = value
        else:
            raise ValueError("Il giorno deve essere compreso tra 1 e 31.")
    
    @property
    def mese(self):
        return self.__mese

    @mese.setter
    def mese(self, value):
        if 1 <= value <= 12:
            self.__mese = value
        else:
            raise ValueError("Il mese deve essere compreso tra 1 e 12.")

    @property
    def anno(self):
        return self.__anno
    
    @anno.setter
    def anno(self, value):
        if value > 0 and value <= datetime.datetime.now().year:
            self.__anno = value
        else:
            raise ValueError("L'anno deve essere un numero positivo minore o uguale all'anno corrente.")
    
        
    
    
# Esempio di utilizzo
""" vendite = inserimento.inserimento_dati()
giorno = Giorno(4, 5, 2024, vendite)
totale, media = giorno.analisi_dati(giorno.dati)
sopra_media = giorno.valuta_vendite(giorno.dati)  """

