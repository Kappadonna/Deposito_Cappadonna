class Calcolatrice:
    
    @staticmethod       # metodo statico, funziona senza dover inizialiazzare oggetto di classe
    def somma(a, b):
        return a +b
    

ris = Calcolatrice.somma(2,10)

print(ris)