import streamlit as st
from services.ai_service import ask_nova


def render():
    st.title("Marketing")
    st.caption("Gerador de ideias, legendas, roteiros e posts para NovaPrint.")

    tema = st.text_input("Tema do post", value="O concorrente não era melhor. Só respondeu primeiro.")
    formato = st.selectbox("Formato", ["Legenda", "Carrossel", "Roteiro de vídeo curto", "Ideias de posts"])

    if st.button("Gerar com a Nova"):
        prompt = f"Crie {formato} para a NovaPrint com o tema: {tema}. Seja prático e comercial."
        st.write(ask_nova(prompt))
