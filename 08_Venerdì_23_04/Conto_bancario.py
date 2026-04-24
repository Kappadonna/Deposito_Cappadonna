class ContoBancario:
    
    def __init__(self, titolare, saldo):
        self.__titolare = titolare
        self.__saldo = saldo
        
    def deposita(self, importo):
        print(f"Saldo prima del deposito {self.__saldo}")
        if importo > 0:
            self.__saldo += importo 
        print(f"Saldo dopo il deposito {self.__saldo}")
            
    def preleva(self, importo):
        print(f"Saldo prima del prelievo {self.__saldo}")
        if importo > 0 and self.__saldo > importo:
            self.__saldo -= importo 
        else:
            print("Importo non disponibile per il prelievo")
        print(f"Saldo dopo il prelievo {self.__saldo}") 
        
    def visualizza_saldo(self):
        print(f"Il saldo disponibile è {self.__saldo}")   
        
    def get_titolare(self):
        return self.__titolare
    
    def set_titolare(self, titolare):
        if isinstance(titolare, str) and titolare.strip() != "":
            self.__titolare = titolare
        else:
            raise ValueError("Il titolare deve essere una stringa non vuota") 
        
        
c = ContoBancario("Gianluca", 200)

c.deposita(10)

c.preleva(230)

c.preleva(50)

c.visualizza_saldo()

print(c.get_titolare())
c.set_titolare("Gianluca Cappadonna")
print(c.get_titolare())