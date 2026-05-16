import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
import pandas as pd


# PARAMETRI COMUNI A TUTTI I PLOT
# plt.rcParams["figure.figsize"] = [10, 6]
# plt.rcParams["figure.dpi"] = 100
# plt.rcParams["figure.facecolor"] = "green"

# # LINE PLOT

# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# plt.figure()
# plt.plot(x, y)
# plt.title("Grafico a linee")
# plt.xlabel("Asse X")
# plt.ylabel("Asse Y")
# #plt.show()

# # BAR PLOT

# categorie = ["A", "B", "C", "D", "E"]
# valori = [3, 7, 2, 5, 8]

# plt.figure()
# plt.bar(categorie, valori)
# plt.title("Grafico a barre")
# plt.xlabel("Categorie")
# plt.ylabel("Valori")
# #plt.show()

# # HIST PLOT

# data = np.random.randn(1000)

# plt.figure()
# plt.hist(data, bins=30)
# plt.title("Istogramma")
# plt.xlabel("Valori")
# plt.ylabel("Frequenza")
# #plt.show()

# # SCATTER PLOT

# x = np.random.rand(50)
# y = np.random.rand(50)

# plt.figure()
# plt.scatter(x, y)
# plt.title("Scatter plot")
# plt.xlabel("Asse X")
# plt.ylabel("Asse Y")
# #plt.show()

# # SUBPLOT

# fig, axes = plt.subplots(nrows= 2, ncols = 2, figsize= (10, 8))

# axes[0, 0].plot([1, 2, 3, 4], [1, 4, 6, 9])
# axes[0, 0].set_title("1: Line plot")

# axes[0, 1].scatter(x, y)
# axes[0, 1].set_title("2: Scatter plot")

# axes[1, 0].bar(categorie, valori)
# axes[1, 0].set_title("3: Bar chart")

# axes[1, 1].hist(data, bins= 30)
# axes[1, 1].set_title("4: Hist plot")
# #plt.show()

# sns.set_theme(style="darkgrid")

# tips = sns.load_dataset("tips")
# print(tips.head())

# sns.barplot(x = "day", y = "total_bill", data = tips)
# plt.title("Conto totale del giorno")
# plt.show()


fmri = sns.load_dataset("fmri")
print(fmri.head())

sns.lineplot(x= "timepoint", y = "signal", data = fmri)
plt.title("Segnale FMRI nel tempo")
plt.show()

