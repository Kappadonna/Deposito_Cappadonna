import numpy as np

# FILE DI SALVATAGGIO
FILE_OUTPUT = "NumpySystem.txt"


def salva_risultato(titolo, contenuto):
    with open(FILE_OUTPUT, "a", encoding="utf-8") as file:
        file.write("\n")
        file.write(f"{titolo}\n")
        file.write(str(contenuto))
        file.write("\n")

# CREAZIONE MATRICE

def crea_matrice():
    righe = int(input("Inserisci numero righe: "))
    colonne = int(input("Inserisci numero colonne: "))

    minimo = int(input("Valore minimo casuale: "))
    massimo = int(input("Valore massimo casuale: "))

    matrice = np.random.randint(minimo, massimo + 1, size=(righe, colonne))

    print("\nMatrice creata:")
    print(matrice)

    salva_risultato("MATRICE CREATA", matrice)

    return matrice

# PARTE 1

def sotto_matrice_centrale(matrice):
    righe, colonne = matrice.shape

    centro_riga = righe // 2
    centro_colonna = colonne // 2

    # Caso matrice piccola
    if righe < 2 or colonne < 2:
        sotto = matrice
    else:
        inizio_riga = max(0, centro_riga - 1)
        fine_riga = min(righe, centro_riga + 1)

        inizio_colonna = max(0, centro_colonna - 1)
        fine_colonna = min(colonne, centro_colonna + 1)

        sotto = matrice[inizio_riga:fine_riga,
                         inizio_colonna:fine_colonna]

    print("\nSotto-matrice centrale:")
    print(sotto)

    salva_risultato("SOTTO-MATRICE CENTRALE", sotto)


def trasposta_matrice(matrice):
    trasposta = matrice.T

    print("\nTrasposta:")
    print(trasposta)

    salva_risultato("TRASPOSTA MATRICE", trasposta)


def somma_elementi(matrice):
    somma = np.sum(matrice)

    print("\nSomma elementi:", somma)

    salva_risultato("SOMMA ELEMENTI", somma)
    
# MENU PARTE 1

def menu_parte1(matrice):
    while True:
        print("\n========== PARTE 1 ==========")
        print("1. Sotto-matrice centrale")
        print("2. Trasposta")
        print("3. Somma elementi")
        print("4. Torna al menu principale")

        scelta = input("Scelta: ")

        if scelta == "1":
            sotto_matrice_centrale(matrice)
        elif scelta == "2":
            trasposta_matrice(matrice)
        elif scelta == "3":
            somma_elementi(matrice)
        elif scelta == "4":
            break
        else:
            print("Scelta non valida!")


# PARTE 2

def moltiplicazione_elementwise(matrice):
    print("\nCreazione seconda matrice...")

    righe, colonne = matrice.shape # per creare matrice della stessa dimensionsione della prima

    minimo = int(input("Valore minimo casuale: "))
    massimo = int(input("Valore massimo casuale: "))

    matrice2 = np.random.randint(
        minimo,
        massimo + 1,
        size=(righe, colonne)
    )

    risultato = matrice * matrice2

    print("\nPrima matrice:")
    print(matrice)

    print("\nSeconda matrice:")
    print(matrice2)

    print("\nMoltiplicazione element-wise:")
    print(risultato)

    testo = (
        f"Prima matrice:\n{matrice}\n\n"
        f"Seconda matrice:\n{matrice2}\n\n"
        f"Risultato:\n{risultato}"
    )

    salva_risultato("MOLTIPLICAZIONE ELEMENT-WISE", testo)


def media_elementi(matrice):
    media = np.mean(matrice)

    print("\nMedia elementi:", media)
    salva_risultato("MEDIA ELEMENTI", media)


def determinante_matrice(matrice):
    righe, colonne = matrice.shape

    if righe == colonne:
        det = np.linalg.det(matrice)
        print("\nDeterminante:", det)
        salva_risultato("DETERMINANTE MATRICE", det)
    else:
        print("\nErrore: la matrice non è quadrata!")

# MENU PARTE 2

def menu_parte2(matrice):
    while True:
        print("\n========== PARTE 2 ==========")
        print("1. Moltiplicazione element-wise")
        print("2. Media elementi")
        print("3. Determinante")
        print("4. Torna al menu principale")

        scelta = input("Scelta: ")

        if scelta == "1":
            moltiplicazione_elementwise(matrice)
        elif scelta == "2":
            media_elementi(matrice)
        elif scelta == "3":
            determinante_matrice(matrice)
        elif scelta == "4":
            break
        else:
            print("Scelta non valida!")
            
# PARTE 3

def inversa_matrice(matrice):
    righe, colonne = matrice.shape

    if righe == colonne:
        det = np.linalg.det(matrice)
        if det != 0:
            inversa = np.linalg.inv(matrice)

            print("\nMatrice inversa:")
            print(inversa)

            salva_risultato("MATRICE INVERSA", inversa)
        else:
            print("\nLa matrice non è invertibile!")
    else:
        print("\nLa matrice non è quadrata!")


def funzione_matematica(matrice):
    print("\nFunzioni disponibili:")
    print("1. sin")
    print("2. cos")
    print("3. exp")

    scelta = input("Scelta: ")

    if scelta == "1":
        risultato = np.sin(matrice)
        nome = "SIN"
    elif scelta == "2":
        risultato = np.cos(matrice)
        nome = "COS"
    elif scelta == "3":
        risultato = np.exp(matrice)
        nome = "EXP"
    else:
        print("\nScelta non valida!")
        return

    print(f"\nRisultato funzione {nome}:")
    print(risultato)

    salva_risultato(f"FUNZIONE {nome}", risultato)


def filtro_condizione(matrice):
    valore = float(input("Mostrare elementi maggiori di: "))

    filtrati = matrice[matrice > valore]
    print("\nElementi filtrati:")
    print(filtrati)

    salva_risultato(
        "FILTRO CONDIZIONALE",
        f"Valori maggiori di {valore}:\n{filtrati}"
    )

# MENU PARTE 3

def menu_parte3(matrice):
    while True:
        print("\n========== PARTE 3 ==========")
        print("1. Matrice inversa")
        print("2. Applicare funzione matematica")
        print("3. Filtro condizionale")
        print("4. Torna al menu principale")

        scelta = input("Scelta: ")

        if scelta == "1":
            inversa_matrice(matrice)
        elif scelta == "2":
            funzione_matematica(matrice)
        elif scelta == "3":
            filtro_condizione(matrice)
        elif scelta == "4":
            break
        else:
            print("Scelta non valida!")

# MAIN

def main():
    print("===================================")
    print(" SISTEMA GESTIONE MATRICI NUMPY ")
    print("===================================")

    matrice = crea_matrice()

    while True:
        print("\n========== MENU PRINCIPALE ==========")
        print("1. Parte 1")
        print("2. Parte 2")
        print("3. Parte 3")
        print("4. Creare nuova matrice")
        print("5. Visualizzare matrice corrente")
        print("6. Uscire")

        scelta = input("Scelta: ")

        if scelta == "1":
            menu_parte1(matrice)
        elif scelta == "2":
            menu_parte2(matrice)
        elif scelta == "3":
            menu_parte3(matrice)
        elif scelta == "4":
            matrice = crea_matrice()
        elif scelta == "5":
            print("\nMatrice corrente:")
            print(matrice)
        elif scelta == "6":
            print("\nProgramma terminato.")
            break
        else:
            print("Scelta non valida!")


if __name__ == "__main__":
    main()
        