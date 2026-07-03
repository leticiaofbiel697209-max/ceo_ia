import streamlit as st
import pandas as pd


def render():
    st.title("Operação")
    st.caption("Entregas, técnicos e impressoras locadas.")

    entregas = [
        {"Tipo": "Entrega", "Cliente": "Cliente exemplo A", "Status": "Pendente", "Responsável": "Técnico"},
        {"Tipo": "Toner", "Cliente": "Cliente exemplo B", "Status": "Solicitado", "Responsável": "Suporte"},
        {"Tipo": "Chamado", "Cliente": "Cliente exemplo C", "Status": "Agendado", "Responsável": "Técnico"},
    ]
    st.dataframe(pd.DataFrame(entregas), use_container_width=True, hide_index=True)
