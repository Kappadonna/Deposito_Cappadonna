class Stampa:
    
    def mostra(self, a = None, b = None):
        if a is not None and b is not None:
            print(a+b)
        elif a is not None:
            print(a)
        else:
            print("Niente da mostrare")
            
a = Stampa()

a.mostra(10, 4)

a.mostra(5)

a.mostra()