# While loop
 
conteggio = 0

while conteggio < 5:
    print(conteggio)
    conteggio +=1
    
condizione = True

while condizione:
    print("condizione vera")
    
    scelta = input("Vuoi continuare? \n").lower()
    
    if scelta == "no":
        condizione = False
        

 
numeri = [1, 2, 3, 4, 5]

for n in numeri:
    print(n)
    

 
for i in range(5):
    print(i)
    
for i in range(2, 8):
    print(i)
    
for i in range(1, 10, 2):
    print(i)
    
