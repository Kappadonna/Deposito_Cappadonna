import csv
import os
from inventario import Articolo, Inventario
from cliente import Cliente

ARTICOLI_FILE = "articoli.csv"
CLIENTI_FILE = "clienti.csv"
VENDITE_FILE = "vendite.csv"

# ──────────────────────────────────────────
# ARTICOLI
# ──────────────────────────────────────────

def carica_articoli():
    articoli = []
    if not os.path.exists(ARTICOLI_FILE):
        return articoli
    with open(ARTICOLI_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for riga in reader:
            articolo = Articolo(
                nome=riga["nome"],
                prezzo=float(riga["prezzo"]),
                quantità=int(riga["quantità"])
            )
            articoli.append(articolo)
    return articoli


def salva_articoli(inventario: Inventario):
    with open(ARTICOLI_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["nome", "prezzo", "quantità"])
        writer.writeheader()
        for articolo in inventario.articoli:
            writer.writerow({
                "nome": articolo.nome,
                "prezzo": articolo.prezzo,
                "quantità": articolo.quantità
            })


# ──────────────────────────────────────────
# CLIENTI
# ──────────────────────────────────────────

def carica_clienti():
    clienti = []
    if not os.path.exists(CLIENTI_FILE):
        return clienti
    with open(CLIENTI_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for riga in reader:
            cliente = Cliente(
                nome=riga["nome"],
                cognome=riga["cognome"],
                username=riga["username"],
                password=riga["password"]
            )
            clienti.append(cliente)
    return clienti


def salva_clienti(lista_clienti):
    with open(CLIENTI_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["nome", "cognome", "username", "password"])
        writer.writeheader()
        for cliente in lista_clienti:
            writer.writerow({
                "nome": cliente.nome,
                "cognome": cliente.cognome,
                "username": cliente.username,
                "password": cliente.password
            })


# ──────────────────────────────────────────
# VENDITE
# ──────────────────────────────────────────

def carica_vendite():
    registro = []
    guadagno_totale = 0.0
    if not os.path.exists(VENDITE_FILE):
        return registro, guadagno_totale
    with open(VENDITE_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for riga in reader:
            vendita = {
                "articolo": riga["articolo"],
                "quantità": int(riga["quantità"]),
                "incasso": float(riga["incasso"])
            }
            registro.append(vendita)
            guadagno_totale += vendita["incasso"]
    return registro, guadagno_totale


def salva_vendite(inventario: Inventario):
    with open(VENDITE_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["articolo", "quantità", "incasso"])
        writer.writeheader()
        for vendita in inventario.registro_vendite:
            writer.writerow({
                "articolo": vendita["articolo"],
                "quantità": vendita["quantità"],
                "incasso": vendita["incasso"]
            })