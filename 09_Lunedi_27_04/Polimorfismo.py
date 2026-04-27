class origine:
    
    def lavoro(self):
        print("Lavoro")

class lavoratore_mauale(origine):
    
    def lavoro(self):
        print("Lavoro manuale")

class lavoratore_digitale(origine):
    
    def lavoro(self):
        print("Lavoro digitale")
    
class lavoratore_nullafacente(origine):
    
    pass

def fai_lavorare(lavoratore: origine):  
    lavoratore.lavoro()
    

l1 = lavoratore_mauale()
l2 = lavoratore_digitale()
l3 = lavoratore_nullafacente()

fai_lavorare(l1)
fai_lavorare(l2)
fai_lavorare(l3)