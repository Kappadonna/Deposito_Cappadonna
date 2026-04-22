class Convertitore:
    
    @staticmethod               # metodo statico, non utilizza istanza di classe
    def euro_in_dollari(euro: int):
        return (euro * 1.08)
    
    @staticmethod               # metodo statico, non utilizza istanza di classe
    def km_in_miglia(km: int):
        return (km * 0.621371)
    
    
dollari = Convertitore.euro_in_dollari(132)
print(f"{dollari} $")

miglia = Convertitore.km_in_miglia(23)
print(f"{miglia} miglia")