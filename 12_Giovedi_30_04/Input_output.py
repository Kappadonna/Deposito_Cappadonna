file = open("12_Giovedi_30_04/test.txt", "r")

contenuto = file.read() # Legge l'intero contenuto del file
riga = file.readline() # Legge una singola riga del file

print(contenuto)


file = open("12_Giovedi_30_04/test.txt", "w") # apertura in modalità scrittura
file.write("W i gatti")
file.close() # chiusura del file

with open("12_Giovedi_30_04/test.txt", "r") as file:
    contenuto = file.read() # il file viene chiuso automaticamente al temrine del blocco 'with'