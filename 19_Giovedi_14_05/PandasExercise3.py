import pandas as pd
import numpy as np


np.random.seed(123)

# DATAFRAME ISCRITTI

iscritti = pd.DataFrame({
    "Nome": ["Luca", "Anna", "Marco", "Sara", "Giulia",
             "Paolo", "Elena", "Luca", "Davide", None],
    
    "Eta": [25, 16, 41, 29, np.nan,
            56, 18, 25, 48, 28],
    
    "Citta": ["Catania", "Messina", "Palermo", "Catania", "Siracusa",
              "Messina", "Catania", "Catania", None, "Siracusa"],
    
    "Tipo_Abbonamento": ["Base", "Premium", "Family", "Base", "Premium",
                         "Family", "Base", "Base", "Premium", None]
})

print("DATAFRAME ISCRITTI")
print(iscritti)

# 2. DATAFRAME PRESENZE

presenze = pd.DataFrame({
    "Data": [
        "2026-05-01", "2026-05-01", "2026-05-01",
        "2026-05-02", "2026-05-02", "2026-05-02",
        "2026-05-03", "2026-05-03", "2026-05-03",
        "2026-05-04", "2026-05-04", "2026-05-04",
        "2026-05-05", "2026-05-05", "2026-05-05"
    ],
    
    "Corso": [
        "Yoga", "Crossfit", "Nuoto",
        "Pilates", "Yoga", "Nuoto",
        "Crossfit", "Pilates", "Yoga",
        "Nuoto", "Crossfit", "Pilates",
        "Yoga", "Nuoto", "Crossfit"
    ],
    
    "Citta": [
        "Catania", "Messina", "Palermo",
        "Catania", "Siracusa", "Messina",
        "Palermo", "Catania", "Siracusa",
        "Messina", "Palermo", "Catania",
        "Siracusa", "Messina", "Palermo"
    ],
    
    "Partecipanti": [
        15, 20, 18,
        12, 14, 19,
        22, 11, 16,
        25, 21, 13,
        17, 24, 23
    ]
})

presenze["Data"] = pd.to_datetime(presenze["Data"])

print("\nDATAFRAME PRESENZE")
print(presenze)


# 3. DATAFRAME COSTI

costi_abbonamento = pd.DataFrame({
    "Tipo_Abbonamento": ["Base", "Premium", "Family"],
    "Costo_Mensile": [30, 50, 80]
})

print("\nDATAFRAME COSTI ABBONAMENTO")
print(costi_abbonamento)


# INTRODUZIONE

# Stampa gli iscritti originali
iscritti_originale = iscritti["Nome"]
print("\nIscritti originali")
print(iscritti_originale)

# Filtra gli iscritti con età maggiore di 25
maggiore_25 = iscritti[iscritti["Eta"] > 25]
iscritti_maggiore_25 = maggiore_25[["Nome", "Eta"]]
print("\nIscritti con età superiore a 25 anni")
print(iscritti_maggiore_25)

# Crea colonna Attivo
iscritti["Attivo"] = np.random.choice([True, False], 10)
print("\nIscritti con nuova colonna 'Attivo'")
print(iscritti)

# PULIZIA DATI

iscritti_puliti = iscritti.copy()

# Rimuovi duplicati dagli iscritti
iscritti_puliti = iscritti.drop_duplicates()

# Gestisci valori mancanti
iscritti_puliti["Nome"] = iscritti_puliti["Nome"].fillna("Sconosciuto")
iscritti_puliti["Eta"] = iscritti_puliti["Eta"].fillna(iscritti_puliti["Eta"].mean())
iscritti_puliti["Citta"] = iscritti_puliti["Citta"].fillna("Non specificata")
iscritti_puliti["Tipo_Abbonamento"] = iscritti_puliti["Tipo_Abbonamento"].fillna("Base")

print("\nISCRITTI DOPO PULIZIA")
print(iscritti_puliti)


# APPLY CON FUNZIONE PERSONALIZZATA

# Funzione fascia_età
def fascia_eta(eta):
    if(eta < 18):
        return "Junior"
    elif(eta < 45):
        return "Adulto"
    else:
        return "Senior"
    
# Applica funzione
iscritti_puliti["Fascia_Eta"] = iscritti_puliti["Eta"].apply(fascia_eta)

print("\nISCRITTI CON AGGIUNTA FASCIA ETÀ")
print(iscritti_puliti)


# ANALISI PRESENZE

# Ordina il dataframe presenze per citta e partecipanti
presenze = presenze.sort_values(["Citta", "Partecipanti"], ascending= [True, False])

print("\nDATAFRAME PRESENZA ORDINATO PER CITTA (ASC) E PARTECIPANTI (DESC)")
print(presenze)

# Groupby per corso con somma totale partecipanti
tot_partecipanti_corso = presenze.groupby("Corso")["Partecipanti"].sum()
print("\nTotale partecipanti per ogni corso")
print(tot_partecipanti_corso)

# Groupby per città con media partecipanti
mean_partecipanti_citta = presenze.groupby("Citta")["Partecipanti"].mean().round(2)
print("\nMedia partecipanti per ogni città")
print(mean_partecipanti_citta)

# Tabella pivot con media dei partecipanti per corso e città
report_presenze_pivot = pd.pivot_table(
    data = presenze, 
    index = "Corso", 
    columns = "Citta", 
    values = "Partecipanti", 
    aggfunc= "mean")
print("Valori medi di partecipanti per corso e città")
print(report_presenze_pivot)

# MULTIINDEX

import pandas as pd

sedi = pd.DataFrame({
    "Sede": ["Nord", "Nord", "Centro", "Centro", "Sud", "Sud"],
    "Anno": [2024, 2025, 2024, 2025, 2024, 2025],
    "Iscritti": np.random.randint(50, 300, 6)
})

sedi = sedi.set_index(["Sede", "Anno"])

print(sedi)

# Tutte le righe di una sede
nord = sedi.loc["Nord"]

print("\nIscritti durante gli anni al nord")
print(nord)

# Valori iscritti di una sede in un anno specifico
print("\nIscritti nel 2024 al nord")
iscritti_2024 = sedi.loc[("Nord", 2024)]
print(iscritti_2024)


# MERGE

merged_df = iscritti.merge(costi_abbonamento, on= "Tipo_Abbonamento")
print("\nUnione di iscritti e costi_abbonamenti su Tipo_Abbonamento")
print(merged_df)

merged_df["Costo_Annuale"] = merged_df["Costo_Mensile"] * 12

print("\nDataframe aggiornato con nuova colonna Costo_Annuale")
print(merged_df)

# OUTPUT FINALE

iscritti_puliti.to_csv("iscritti_puliti.csv")

report_presenze_pivot.to_csv("report_presenze_pivot.csv")

merged_df.to_csv("iscritti_con_costi.csv")