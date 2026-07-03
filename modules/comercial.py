import streamlit as st
import pandas as pd


def render():
    st.title("Comercial")
    st.caption("Fila de clientes para recompra, orçamentos sem retorno e oportunidades.")

    data = [
        {"Cliente": "Cliente exemplo A", "Motivo": "Próximo da recompra", "Dias sem comprar": 66, "Ação": "Ligar hoje"},
        {"Cliente": "Cliente exemplo B", "Motivo": "Orçamento sem retorno", "Dias sem comprar": 12, "Ação": "WhatsApp"},
        {"Cliente": "Cliente exemplo C", "Motivo": "Cliente em risco", "Dias sem comprar": 95, "Ação": "Recuperação"},
    ]
    st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
    st.warning("Dados de exemplo. Na integração real, este módulo buscará vendas, orçamentos e clientes do GestãoClick.")
