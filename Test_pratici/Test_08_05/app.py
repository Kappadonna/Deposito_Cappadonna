import streamlit as st
import pandas as pd
from Agenzia import Agenzia
from Veicolo import Automobile, Furgone
from GestioneDati import salva_flotta, carica_flotta, salva_storico, carica_storico

# ── Configurazione pagina ──────────────────────────────────────────────────────
st.set_page_config(
    page_title="Masamune Rent",
    page_icon="🚗",
    layout="wide",
)

# ── Stile custom ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: red;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1rem;
        color: #6c757d;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background: #f8f9fa;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        border-left: 4px solid #4361ee;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 0.9rem;
        font-weight: 500;
    }
    div[data-testid="stSuccessMessage"], div[data-testid="stErrorMessage"] {
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ── Inizializzazione sessione ──────────────────────────────────────────────────
if "agenzia" not in st.session_state:
    agenzia = Agenzia("Masamune Rent")
    agenzia.flotta = carica_flotta()
    agenzia.storico_noleggi = carica_storico()
    st.session_state.agenzia = agenzia

agenzia: Agenzia = st.session_state.agenzia

# ── Helper: converti flotta in DataFrame ──────────────────────────────────────
def flotta_to_df(flotta):
    rows = []
    for v in flotta:
        tipo = "Automobile" if isinstance(v, Automobile) else "Furgone"
        extra_label = "Posti" if tipo == "Automobile" else "Capacità (kg)"
        extra_val = v.n_posti if tipo == "Automobile" else v.capacità
        rows.append({
            "Tipo": tipo,
            "Targa": v.targa,
            "Marca": v.marca,
            "Modello": v.modello,
            "Anno": v.anno,
            "€/giorno": v.prezzo_giornaliero,
            extra_label: extra_val,
            "Disponibile": "✅" if v.disponibile else "❌",
        })
    return pd.DataFrame(rows) if rows else pd.DataFrame()

def storico_to_df(storico):
    return pd.DataFrame(storico) if storico else pd.DataFrame(
        columns=["targa", "cliente", "giorni", "costo"]
    )

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="main-header">🚗 Masamune Rent</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Gestione flotta e noleggi</div>', unsafe_allow_html=True)

# ── KPI bar ───────────────────────────────────────────────────────────────────
tot = len(agenzia.flotta)
disp = sum(1 for v in agenzia.flotta if v.disponibile)
noleggiati = tot - disp
incasso = sum(n["costo"] for n in agenzia.storico_noleggi)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Veicoli in flotta", tot)
c2.metric("Disponibili", disp)
c3.metric("Noleggiati", noleggiati)
c4.metric("Incasso totale", f"€ {incasso:,.2f}")

st.divider()

# ── Tab principali ─────────────────────────────────────────────────────────────
tab_flotta, tab_crea, tab_noleggio, tab_restituzione, tab_modifica, tab_rimuovi, tab_storico = st.tabs([
    "📋 Flotta", "➕ Aggiungi", "🔑 Noleggia", "↩️ Restituisci", "✏️ Modifica", "🗑️ Rimuovi", "📜 Storico"
])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 – FLOTTA
# ══════════════════════════════════════════════════════════════════════════════
with tab_flotta:
    st.subheader("Flotta attuale")

    col_filter, col_disp = st.columns([2, 2])
    with col_filter:
        filtro_tipo = st.selectbox("Filtra per tipo", ["Tutti", "Automobile", "Furgone"])
    with col_disp:
        filtro_disp = st.selectbox("Filtra disponibilità", ["Tutti", "Disponibili", "Noleggiati"])

    flotta_filtrata = agenzia.flotta
    if filtro_tipo != "Tutti":
        cls = Automobile if filtro_tipo == "Automobile" else Furgone
        flotta_filtrata = [v for v in flotta_filtrata if isinstance(v, cls)]
    if filtro_disp == "Disponibili":
        flotta_filtrata = [v for v in flotta_filtrata if v.disponibile]
    elif filtro_disp == "Noleggiati":
        flotta_filtrata = [v for v in flotta_filtrata if not v.disponibile]

    df = flotta_to_df(flotta_filtrata)
    if df.empty:
        st.info("Nessun veicolo corrisponde ai filtri selezionati.")
    else:
        st.dataframe(df, use_container_width=True, hide_index=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 – AGGIUNGI VEICOLO
# ══════════════════════════════════════════════════════════════════════════════
with tab_crea:
    st.subheader("Aggiungi un nuovo veicolo")

    with st.form("form_crea"):
        tipo = st.radio("Tipo veicolo", ["Automobile", "Furgone"], horizontal=True)
        col1, col2 = st.columns(2)
        with col1:
            targa  = st.text_input("Targa").upper()
            marca  = st.text_input("Marca")
            anno   = st.number_input("Anno", min_value=1990, max_value=2025, value=2020, step=1)
        with col2:
            modello = st.text_input("Modello")
            prezzo  = st.number_input("Prezzo giornaliero (€)", min_value=1.0, step=1.0, value=30.0)
            if tipo == "Automobile":
                extra = st.number_input("Numero di posti", min_value=2, max_value=5, value=5, step=1)
            else:
                extra = st.number_input("Capacità (kg)", min_value=500.0, max_value=3000.0, value=1000.0, step=50.0)

        submitted = st.form_submit_button("➕ Aggiungi veicolo", use_container_width=True)

    if submitted:
        if not targa or not marca or not modello:
            st.error("Compila tutti i campi obbligatori.")
        elif agenzia.cerca_veicolo(targa):
            st.error(f"Esiste già un veicolo con targa {targa}.")
        else:
            if tipo == "Automobile":
                v = Automobile(targa, marca, modello, int(anno), prezzo, True, int(extra))
            else:
                v = Furgone(targa, marca, modello, int(anno), prezzo, True, float(extra))
            agenzia.aggiungi_veicolo(v)
            salva_flotta(agenzia.flotta)
            st.success(f"Veicolo {targa} aggiunto con successo!")
            st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 – NOLEGGIO
# ══════════════════════════════════════════════════════════════════════════════
with tab_noleggio:
    st.subheader("Noleggia un veicolo")

    disponibili = [v for v in agenzia.flotta if v.disponibile]
    if not disponibili:
        st.info("Nessun veicolo disponibile al momento.")
    else:
        df_disp = flotta_to_df(disponibili)
        st.dataframe(df_disp, use_container_width=True, hide_index=True)

        with st.form("form_noleggio"):
            targhе_disponibili = [v.targa for v in disponibili]
            targa_sel = st.selectbox("Seleziona veicolo (targa)", targhе_disponibili)
            cliente   = st.text_input("Nome cliente")
            giorni    = st.number_input("Numero di giorni", min_value=1, step=1, value=1)

            # Anteprima costo
            veicolo_sel = agenzia.cerca_veicolo(targa_sel) if targa_sel else None
            if veicolo_sel:
                costo_prev = veicolo_sel.calcola_costo(giorni)
                st.info(f"💰 Costo stimato: **€ {costo_prev:.2f}**" +
                        (" (sconto applicato)" if giorni > 7 else ""))

            submitted_n = st.form_submit_button("🔑 Conferma noleggio", use_container_width=True)

        if submitted_n:
            if not cliente:
                st.error("Inserisci il nome del cliente.")
            elif agenzia.noleggia_veicolo(targa_sel, cliente, int(giorni)):
                salva_flotta(agenzia.flotta)
                salva_storico(agenzia.storico_noleggi)
                st.success(f"Veicolo {targa_sel} noleggiato a {cliente} per {giorni} giorni. Costo: €{costo_prev:.2f}")
                st.rerun()
            else:
                st.error("Operazione non riuscita.")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 4 – RESTITUZIONE
# ══════════════════════════════════════════════════════════════════════════════
with tab_restituzione:
    st.subheader("Restituisci un veicolo")

    noleggiati_list = [v for v in agenzia.flotta if not v.disponibile]
    if not noleggiati_list:
        st.info("Nessun veicolo attualmente noleggiato.")
    else:
        df_nol = flotta_to_df(noleggiati_list)
        st.dataframe(df_nol, use_container_width=True, hide_index=True)

        with st.form("form_restituzione"):
            targa_rest = st.selectbox("Seleziona veicolo da restituire", [v.targa for v in noleggiati_list])
            submitted_r = st.form_submit_button("↩️ Restituisci", use_container_width=True)

        if submitted_r:
            if agenzia.restituisci_veicolo(targa_rest):
                salva_flotta(agenzia.flotta)
                st.success(f"Veicolo {targa_rest} restituito e nuovamente disponibile.")
                st.rerun()
            else:
                st.error("Operazione non riuscita.")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 5 – MODIFICA
# ══════════════════════════════════════════════════════════════════════════════
with tab_modifica:
    st.subheader("Modifica un veicolo")

    if not agenzia.flotta:
        st.info("La flotta è vuota.")
    else:
        with st.form("form_modifica"):
            targa_mod = st.selectbox("Seleziona veicolo (targa)", [v.targa for v in agenzia.flotta])

            veicolo_m = agenzia.cerca_veicolo(targa_mod)
            if veicolo_m:
                st.caption(f"Prezzo attuale: €{veicolo_m.prezzo_giornaliero}/giorno — Disponibile: {'Sì' if veicolo_m.disponibile else 'No'}")

            col_m1, col_m2 = st.columns(2)
            with col_m1:
                nuovo_prezzo_str = st.text_input("Nuovo prezzo (lascia vuoto per non cambiare)")
            with col_m2:
                nuova_disp = st.selectbox("Disponibilità", ["Non modificare", "Disponibile", "Non disponibile"])

            submitted_m = st.form_submit_button("✏️ Salva modifiche", use_container_width=True)

        if submitted_m:
            prezzo_val = float(nuovo_prezzo_str) if nuovo_prezzo_str else None
            disp_val = None
            if nuova_disp == "Disponibile":    disp_val = True
            elif nuova_disp == "Non disponibile": disp_val = False

            if agenzia.modifica_veicolo(targa_mod, prezzo_val, disp_val):
                salva_flotta(agenzia.flotta)
                st.success(f"Veicolo {targa_mod} aggiornato.")
                st.rerun()
            else:
                st.error("Modifica non riuscita.")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 6 – RIMUOVI
# ══════════════════════════════════════════════════════════════════════════════
with tab_rimuovi:
    st.subheader("Rimuovi un veicolo dalla flotta")

    if not agenzia.flotta:
        st.info("La flotta è vuota.")
    else:
        with st.form("form_rimuovi"):
            targa_rim = st.selectbox("Seleziona veicolo da rimuovere", [v.targa for v in agenzia.flotta])
            veicolo_r = agenzia.cerca_veicolo(targa_rim)
            if veicolo_r:
                st.warning(f"Stai per rimuovere: {veicolo_r.descrizione()}")
            confirm = st.checkbox("Confermo la rimozione")
            submitted_del = st.form_submit_button("🗑️ Rimuovi", use_container_width=True)

        if submitted_del:
            if not confirm:
                st.error("Spunta la casella di conferma prima di procedere.")
            elif agenzia.rimuovi_veicolo(targa_rim):
                salva_flotta(agenzia.flotta)
                st.success(f"Veicolo {targa_rim} rimosso dalla flotta.")
                st.rerun()
            else:
                st.error("Rimozione non riuscita.")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 7 – STORICO
# ══════════════════════════════════════════════════════════════════════════════
with tab_storico:
    st.subheader("Storico noleggi")

    if not agenzia.storico_noleggi:
        st.info("Nessun noleggio registrato.")
    else:
        df_storico = storico_to_df(agenzia.storico_noleggi)
        df_storico.columns = ["Targa", "Cliente", "Giorni", "Costo (€)"]
        st.dataframe(df_storico, use_container_width=True, hide_index=True)

        st.divider()
        st.markdown(f"**Totale noleggi:** {len(agenzia.storico_noleggi)} &nbsp;&nbsp; **Incasso complessivo:** €{incasso:,.2f}")
