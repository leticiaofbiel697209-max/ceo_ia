import os
from typing import List, Dict
from openai import OpenAI

DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

SYSTEM_PROMPT = """
Você é a NOVA IA, assistente executiva e operacional da NovaPrint.
Seu papel é ajudar Gabriel a organizar a empresa, priorizar tarefas, analisar comercial,
financeiro, entregas, impressoras locadas, marketing e projetos internos.

Regras de comportamento:
- Seja objetiva, prática e direta.
- Sempre destaque prioridades e próximos passos.
- Quando não houver dados reais conectados, diga claramente que está usando dados demonstrativos.
- Pense como diretora de operações: comercial primeiro quando houver chance de faturamento.
- Não invente valores reais da empresa. Use apenas dados fornecidos ou dados marcados como exemplo.
"""


def get_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None
    return OpenAI(api_key=api_key)


def ask_nova(user_message: str, context: Dict | None = None, history: List[Dict] | None = None) -> str:
    client = get_client()
    context = context or {}
    history = history or []

    if not client:
        return (
            "A chave OPENAI_API_KEY ainda não foi configurada. "
            "Mesmo assim, posso operar em modo demonstrativo. Configure a chave em Secrets ou no arquivo .env."
        )

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    if context:
        messages.append({
            "role": "system",
            "content": f"Contexto operacional atual da NovaPrint: {context}"
        })

    messages.extend(history[-8:])
    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=messages,
        temperature=0.3,
    )
    return response.choices[0].message.content or "Não consegui gerar resposta agora."
