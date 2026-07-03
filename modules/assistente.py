import streamlit as st
from services.ai_service import ask_nova
from services.gestaoclick_api import buscar_resumo_demo


def render():
    st.title("Conversar com a Nova")
    st.caption("Pergunte sobre prioridades, clientes, financeiro, entregas, marketing ou projetos.")

    if "nova_messages" not in st.session_state:
        st.session_state.nova_messages = [
            {"role": "assistant", "content": "Bom dia, Gabriel. Sou a NOVA IA. Como posso te ajudar a organizar a NovaPrint hoje?"}
        ]

    for msg in st.session_state.nova_messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    prompt = st.chat_input("Ex: Nova, o que está mais urgente hoje?")
    if prompt:
        st.session_state.nova_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        context = buscar_resumo_demo()
        history = [m for m in st.session_state.nova_messages if m["role"] in ["user", "assistant"]]
        answer = ask_nova(prompt, context=context, history=history)
        st.session_state.nova_messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.write(answer)
