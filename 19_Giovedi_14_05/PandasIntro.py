import pandas as pd
import numpy as np


print("===================================")
print("Pandas Introduction")
print("===================================")


data = {
    "Nome": ["Alice", "Bob", "Carla", "Giulio"],
    "Età": [25, 30, 22, 16],
    "Città": ["Roma", "Milano", "Napoli", "Torino"]
}

df = pd.DataFrame(data)

print("\nDataFrame Originale")
print(df)

# Selezione delle righe in base a condizione
df_older = df[df["Età"] > 23]
print("\nPersone con età maggiore di 23 anni")
print(df_older)

# Creazione di una nuova colonna
df["Maggiorenne"] = df["Età"] >= 18
print("\n Nuova colonna Maggiorenne")
print(df)

# Pulizia dei dati su pandas
data2 = {
    "Nome": ["Alice", "Bob", "Carla", "Bob", "Carla", "Alice", None],
    "Età": [25, 30, 22, 20, np.nan, 25, 29],
    "Città": ["Roma", "Milano", "Napoli", "Milano", "Napoli", "Roma", "Roma"]
}

df2 = pd.DataFrame(data2)

print("\nDataFrame originale")
print(df2)

# Rimozione duplicati:

df2 = df2.drop_duplicates()
print("\nDuplicati rimossi")
print(df2)

# Rimozione valori nulli
df_cleaned = df2.dropna()
print("Rimozione valori mancanti, creazione nuovo dataframe df_cleaned")
print(df_cleaned)

# Sostituzione dei valori mancanti
df2.fillna({ "Età": df["Età"].mean()}, inplace = True)
print("\nRimozione valori mancanti in df2")
print(df2)

data_multi = {
  'Paese': ['Italia', 'Italia', 'Francia', 'Francia'],
  'Anno': [2023, 2024, 2023, 2024],
  'Vendite': [120, 135, 110, 118]
}

df_multi = pd.DataFrame(data_multi)

# Creo un indice gerarchico con Paese e Anno
df_multi = df_multi.set_index(['Paese', 'Anno'])

print("\nDataFrame con MultiIndex:")
print(df_multi)

print("\n tutte le righed ell'italia")
print(df_multi.loc['Italia'])

print("\n valore vendite Francia 2024")
print(df_multi.loc[('Francia', 2024)], "Vendite")


data = {
    'Data': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
    'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],
    'Vendite': [100, 200, 150, 300, 250]
}


df = pd.DataFrame(data)
# Creazione della tabella pivot
pivot_df = df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')
print(pivot_df)

data = {
    'Data': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
    'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],
    'Vendite': [100, 200, 150, 300, 250]
    
}


df = pd.DataFrame(data)

grouped_df = df.groupby('Prodotto').sum()
print(grouped_df)


print("\n DF prdinato per vendite")
df_sorted = df.sort_values(by = "Vendite", ascending= False)
print(df_sorted)

df["Prezzo + IVA"] = df['Vendite'].apply(lambda x: x * 1.22)
print(df)

# Esempio riepilogativo

# Creazione dei DataFrame
data_vendite = {
    'Prodotto': ['Tastiera', 'Mouse', 'Monitor', 'Tastiera', 'Monitor'],
    'Quantità': [5, 10, 2, 7, 3],
    'Città': ['Roma', 'Milano', 'Roma', 'Napoli', 'Milano'],
    'Data': ['2021-09-01', '2021-09-01', '2021-09-02', '2021-09-02', '2021-09-03']
}

vendite_df = pd.DataFrame(data_vendite)

data_costi = {
    'Prodotto': ['Tastiera', 'Mouse', 'Monitor'],
    'Costo per unità': [50, 25, 150]
}

costi_df = pd.DataFrame(data_costi)

# Unione dei DataFrame
df_merge = pd.merge(vendite_df, costi_df, on='Prodotto')
# Creazione della tabella pivot
pivot_table = df_merge.pivot_table(index='Prodotto', columns='Città', values='Quantità', aggfunc='sum')

# Visualizzazione del risultato
print(pivot_table)