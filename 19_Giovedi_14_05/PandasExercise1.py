import pandas as pd
import numpy as np

nomi = ["Gigi", "Gianluca", "Martina", "Damiano", "Chiara", "Lorenzo", "Carmelo", "Marco", "Angelo", "Roberta", "Giuliano", "Giuseppe"]

età = [14, 16, 37, 43, 83, 13 ,49, 56, 24 ,35 ,41, 65, 75, np.nan]

città = ["Milano", "Roma", "Napoli", "Torino", "Catania", "Palermo", "Padova", "Bari"]

salario = [21000, 30000, 45000, 50000, 34000, 67000, 27000, np.nan]

np.random.seed(123)

data = {
    "Nome": np.random.choice(nomi, 20),
    "Età": np.random.choice(età, 20),
    "Città": np.random.choice(città, 20),
    "Salario": np.random.choice(salario, 20)
}

df = pd.DataFrame(data)

print(df)

print("\n Prime 5 righe del dataframe")
print(df.head())

print("\n Ultime 5 righe del dataframe")
print(df.tail())

print("\nInformazioni sulle colonne, incluso il tipo di dati")
print(df.info())

print("Statistiche descrittive del dataframe")
print(df.describe())

df_cleaned = df.drop_duplicates()
print(df_cleaned)
print("\nVerifica rimozione duplicati")
print("\nNumero di righe del df_originale: " + str(len(df)) + "\nNumero di righe del df_cleaned: " + str(len(df_cleaned)))

df_cleaned.fillna({"Età":df["Età"].median(), "Salario": df["Salario"].median()}, inplace = True)
print("Sostiuzione valori mancanti con mediana della rispettiva colonna")
print(df_cleaned)

print("Aggiunta nuova colonna Categoria Età")
df_cleaned["Categoria Età"] = "Giovane"
df_cleaned.loc[df_cleaned["Età"] > 19, "Categoria Età"] = "Adulto"
df_cleaned.loc[df_cleaned["Età"] > 65, "Categoria Età"] = "Senior"

# Metodo alternativo
def categoria_eta(eta):
    if(eta < 18):
        return "Giovane"
    elif(eta < 65):
        return "Adulto"
    else:
        return "Senior"
    
df_cleaned["Categoria Età 2"] = df_cleaned["Età"].apply(categoria_eta)
    
print(df_cleaned)

df_cleaned.to_csv("Persone.csv", sep = ",")



