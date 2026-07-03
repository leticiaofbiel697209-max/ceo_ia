import streamlit as st


def render():
    st.title("Financeiro")
    st.caption("Visão executiva de contas, recebíveis, inadimplência e fluxo.")

    c1, c2, c3 = st.columns(3)
    c1.metric("Recebido hoje", "R$ 14.200")
    c2.metric("A receber", "R$ 86.500")
    c3.metric("Atrasado", "R$ 22.300")

    st.info("Na próxima fase, conectamos contas a receber e contas a pagar do GestãoClick.")
