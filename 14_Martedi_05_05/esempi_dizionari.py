studente = {
    "nome" : "Gianluca",
    "età" : 26,
    "sesso" : "Maschio"
}

# Accedere ai valori tramite le chiavi
print(studente["nome"])
print(studente["età"])
print(studente["sesso"])

# Modificare i valori di una chiave
studente["età"] = 27
print(studente)

# Aggiungeri coppia chiave-valore ad un dizionario
studente["città"] = "Catania"
print(studente)

# Restituisce la lista delle chiavi
print(studente.keys())
# Restituisce la lista dei valori
print(studente.values())
# Restituisce coppie chiave-valore
print(studente.items())