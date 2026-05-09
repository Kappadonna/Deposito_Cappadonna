# 🚗 Masamune Rent — Gestione Flotta e Noleggi

Sistema di gestione di un'agenzia di noleggio veicoli, sviluppato in Python con paradigma **orientato agli oggetti (OOP)**.

---

## 📌 Descrizione

Il programma modella il flusso operativo di un'agenzia di autonoleggio, permettendo di:

- Aggiungere e rimuovere veicoli dalla flotta (automobili e furgoni)
- Noleggiare un veicolo a un cliente per un numero definito di giorni
- Calcolare il costo del noleggio con logica di sconto automatica (> 7 giorni)
- Restituire un veicolo e renderlo nuovamente disponibile
- Modificare prezzo giornaliero e disponibilità di un veicolo esistente
- Visualizzare e filtrare la flotta per tipo e disponibilità
- Consultare lo storico completo dei noleggi con relativo incasso
- Persistere lo stato su file CSV tra una sessione e l'altra

La struttura è costruita attorno alla classe astratta `Veicolo`, da cui derivano `Automobile` e `Furgone`, e alla classe `Agenzia`, che incapsula la flotta e lo storico dei noleggi tramite proprietà con getter/setter e metodi di aggiunta/rimozione. La persistenza è delegata al modulo `GestioneDati`, che gestisce la lettura e scrittura su file CSV.

---

## 📂 File

| File | Contenuto |
|---|---|
| `Veicolo.py` | Classe astratta `Veicolo` e sottoclassi `Automobile`, `Furgone` |
| `Agenzia.py` | Classe `Agenzia` con gestione flotta, noleggi e storico |
| `GestioneDati.py` | Modulo per il salvataggio e caricamento dello stato su CSV |
| `main.py` | Programma originale con interfaccia testuale (terminale) |
| `app.py` | Versione con interfaccia grafica su Streamlit |

---

## 🏗️ Struttura OOP

```
Veicolo (ABC)
├── targa, marca, modello, anno      → proprietà con getter/setter
├── prezzo_giornaliero               → setter con validazione (> 0)
├── disponibile                      → setter con validazione (bool)
├── descrizione()                    → metodo astratto
└── calcola_costo(giorni)            → metodo astratto

Automobile(Veicolo)
├── n_posti                          → setter con validazione (2–5)
├── descrizione()                    → implementazione concreta
└── calcola_costo(giorni)            → sconto 10% oltre 7 giorni

Furgone(Veicolo)
├── capacità                         → setter con validazione (500–3000 kg)
├── descrizione()                    → implementazione concreta
└── calcola_costo(giorni)            → sconto 15% oltre 7 giorni

Agenzia
├── nome, flotta, storico_noleggi
├── aggiungi_veicolo / rimuovi_veicolo / cerca_veicolo / modifica_veicolo
├── noleggia_veicolo / restituisci_veicolo
├── visualizza_flotta / visualizza_storico_noleggi
└── analizza_per_tipo                → filtro per classe tramite MAPPA_TIPI

Persistenza (GestioneDati.py)
├── flotta.csv                       → stato attuale di tutti i veicoli
└── storico_noleggi.csv              → registro di tutti i noleggi effettuati
```

---

## ▶️ Come eseguire

**Versione terminale:**
```bash
python main.py
```

**Versione Streamlit:**
```bash
pip install streamlit
streamlit run app.py
```

I file CSV (`flotta.csv`, `storico_noleggi.csv`) vengono creati automaticamente nella stessa cartella al primo salvataggio.

---

## 🎨 Interfaccia Streamlit

La versione grafica include:

- **Barra KPI** — riepilogo sempre visibile con veicoli totali, disponibili, noleggiati e incasso complessivo
- **7 tab** principali per separare le funzionalità:
  - 📋 **Flotta** — visualizzazione dell'intera flotta con filtri per tipo e disponibilità
  - ➕ **Aggiungi** — form per la creazione di un nuovo veicolo (Automobile o Furgone)
  - 🔑 **Noleggia** — selezione da dropdown dei soli veicoli disponibili, con anteprima del costo e indicazione dello sconto applicato
  - ↩️ **Restituisci** — selezione dai veicoli attualmente noleggiati
  - ✏️ **Modifica** — modifica di prezzo giornaliero e/o disponibilità
  - 🗑️ **Rimuovi** — rimozione con checkbox di conferma obbligatoria
  - 📜 **Storico** — tabella di tutti i noleggi registrati con totale incassato

---

## 🤖 Nota sull'uso di AI

Il programma originale (`main.py`) — inclusi la struttura OOP, la gerarchia `Veicolo → Automobile / Furgone`, la classe `Agenzia` con i relativi metodi, il modulo `GestioneDati` per la persistenza CSV e il menu interattivo da terminale — è stato sviluppato **interamente in autonomia**.

La versione Streamlit (`app.py`) è stata realizzata con il supporto di **Claude (Anthropic)**. A partire dal codice originale, Claude ha contribuito a:
- Convertire l'interfaccia testuale in un'app web con Streamlit
- Progettare la struttura a tab, la barra KPI e i form interattivi
- Gestire lo stato della sessione tramite `st.session_state`
- Implementare i filtri per tipo e disponibilità nel tab Flotta
- Mantenere invariata la logica OOP originale senza modifiche alle classi

Questa distinzione riflette un uso trasparente e consapevole degli strumenti AI come supporto allo sviluppo, non come sostituto delle competenze personali.
