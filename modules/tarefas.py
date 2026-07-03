import streamlit as st
import pandas as pd
from services.db import list_tasks_demo


def render():
    st.title("Tarefas e Prioridades")
    st.caption("Começo simples para organizar o dia. Depois conectamos ao Supabase.")

    df = pd.DataFrame(list_tasks_demo())
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.subheader("Adicionar tarefa manual")
    with st.form("nova_tarefa"):
        area = st.selectbox("Área", ["Comercial", "Financeiro", "Operação", "Impressoras", "Marketing", "Projetos"])
        prioridade = st.selectbox("Prioridade", ["Alta", "Média", "Baixa"])
        tarefa = st.text_input("Tarefa")
        submitted = st.form_submit_button("Adicionar")
        if submitted:
            st.success("Tarefa registrada nesta sessão. Na próxima etapa salvaremos no Supabase.")
            st.write({"area": area, "prioridade": prioridade, "tarefa": tarefa})
