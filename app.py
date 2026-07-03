import os
from dotenv import load_dotenv
import streamlit as st

from modules import dashboard, assistente, tarefas, comercial, financeiro, operacao, marketing

load_dotenv()

st.set_page_config(
    page_title="NOVA IA — NovaPrint",
    page_icon="🧠",
    layout="wide",
)

st.sidebar.title("NOVA IA")
st.sidebar.caption("NovaPrint")

pagina = st.sidebar.radio(
    "Menu",
    [
        "Centro de Comando",
        "Conversar com a Nova",
        "Tarefas",
        "Comercial",
        "Financeiro",
        "Operação",
        "Marketing",
        "Configurações",
    ],
)

st.sidebar.divider()
st.sidebar.write("Status")
st.sidebar.write("IA:", "✅ configurada" if os.getenv("OPENAI_API_KEY") else "⚠️ sem chave")
st.sidebar.write("Supabase:", "✅ configurado" if os.getenv("SUPABASE_URL") else "⚠️ opcional")
st.sidebar.write("GestãoClick:", "✅ configurado" if os.getenv("GESTAOCLICK_API_URL") else "⚠️ opcional")
st.sidebar.write("waTidy:", "✅ configurado" if os.getenv("WATIDY_API_URL") else "⚠️ opcional")

if pagina == "Centro de Comando":
    dashboard.render()
elif pagina == "Conversar com a Nova":
    assistente.render()
elif pagina == "Tarefas":
    tarefas.render()
elif pagina == "Comercial":
    comercial.render()
elif pagina == "Financeiro":
    financeiro.render()
elif pagina == "Operação":
    operacao.render()
elif pagina == "Marketing":
    marketing.render()
else:
    st.title("Configurações")
    st.write("Configure as variáveis em `.env` localmente ou em Secrets no Streamlit Cloud.")
    st.code("""
OPENAI_API_KEY=...
OPENAI_MODEL=gpt-4.1-mini
SUPABASE_URL=...
SUPABASE_KEY=...
GESTAOCLICK_API_URL=...
GESTAOCLICK_API_TOKEN=...
WATIDY_API_URL=...
WATIDY_TOKEN=...
""")
    st.info("A primeira versão funciona sem Supabase, GestãoClick e waTidy. Para a IA responder de verdade, configure OPENAI_API_KEY.")
