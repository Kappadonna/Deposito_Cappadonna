import pandas as pd
import numpy as np

np.random.seed(123)

prodotti = [
    "Pane", "Latte", "Pasta", "Riso",
    "Mele", "Banane", "Pizza", "Acqua",
    "Caffè", "Biscotti", "Formaggio", "Yogurt"
]

quantità = [
    78, 13, 15, 37,
    61, 42, 22, 12,
    16, 31, 29, 38
]

prezzo_unitario = [
    1.50, 2.00, 1.20, 2.50,
    0.80, 1.10, 7.50, 0.60,
    4.20, 3.40, 5.90, 1.30
]

città = [
    "Milano", "Roma", "Napoli", "Torino",
    "Catania", "Palermo", "Padova", "Bari",
    "Firenze", "Genova", "Verona", "Bologna"
]


data = {
    "Prodotto": np.random.choice(prodotti, 20),
    "Quantità": np.random.choice(quantità, 20),
    "Prezzo Unitario": np.random.choice(prezzo_unitario, 20),
    "Città": np.random.choice(città, 20)
}

df = pd.DataFrame(data)

print("\nDataframe originale")
print(df)

df["Totale Vendite"] = df["Prezzo Unitario"] * df["Quantità"]
print("\n Dataframe con colonna totale vendite aggiunta")
print(df)

print("\nTotale delle vendite per ciascun prodotto")
max_v =df.groupby("Prodotto")["Totale Vendite"].sum()
print(max_v)

print("\nProdotto più venduto in termini di quantita")
max_q = df.groupby("Prodotto")["Quantità"].sum()
prodotto = max_q.idxmax()
quantita = max_q.max()
print(prodotto, quantita)

print("\nCittà con vendite piu alte")
max_vendite = df.groupby("Città")["Totale Vendite"].sum()
citta = max_vendite.idxmax()
vendite = max_vendite.max()
print(citta, vendite)

print("\nDataframe con righe che rispettano la condizione Totale vendite > 100")
df_cento = df[df["Totale Vendite"]>100]
print(df_cento)

print("\nDataframe ordinato per totale vendite in modo decrescente")
df_sorted = df.sort_values(by="Totale Vendite", ascending=False)
print(df_sorted)

print("\nNumero di vendite per ogni città")
df_citta = df["Città"]. value_counts()
df_citta_sorted = df_citta.sort_values(ascending= False)
print(df_citta_sorted)
