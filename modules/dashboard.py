import streamlit as st
from services.gestaoclick_api import buscar_resumo_demo
from services.db import list_tasks_demo


def render():
    st.title("NOVA IA — Centro de Comando")
    st.caption("Assistente executiva e operacional da NovaPrint")

    resumo = buscar_resumo_demo()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Orçamentos abertos", resumo["orcamentos_abertos"])
    c2.metric("Próximos da recompra", resumo["clientes_proximos_recompra"])
    c3.metric("Clientes em risco", resumo["clientes_em_risco"])
    c4.metric("Potencial hoje", f"R$ {resumo['vendas_potenciais_hoje']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    st.subheader("Prioridades de hoje")
    tasks = list_tasks_demo()
    for item in tasks:
        with st.container(border=True):
            st.write(f"**{item['prioridade']} — {item['area']}**")
            st.write(item["tarefa"])
            st.caption(item["status"])

    st.info("Modo demonstrativo: conecte GestãoClick, Supabase e waTidy para puxar dados reais.")
