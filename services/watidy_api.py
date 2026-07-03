import os
import requests


def enviar_whatsapp(telefone: str, mensagem: str):
    base = os.getenv("WATIDY_API_URL", "").rstrip("/")
    path = os.getenv("WATIDY_SEND_PATH", "/send-message")
    token = os.getenv("WATIDY_TOKEN")
    if not base or not token:
        return {"ok": False, "erro": "WATIDY_API_URL ou WATIDY_TOKEN não configurado"}

    payload = {"phone": telefone, "message": mensagem}
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    try:
        r = requests.post(f"{base}{path}", json=payload, headers=headers, timeout=20)
        return {"ok": r.ok, "status_code": r.status_code, "resposta": r.text[:300]}
    except Exception as e:
        return {"ok": False, "erro": str(e)}
