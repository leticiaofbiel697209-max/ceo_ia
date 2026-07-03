import os
import requests


def get_headers():
    token = os.getenv("GESTAOCLICK_API_TOKEN")
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def get_base_url():
    return os.getenv("GESTAOCLICK_API_URL", "").rstrip("/")


def testar_conexao():
    base = get_base_url()
    if not base:
        return {"ok": False, "erro": "GESTAOCLICK_API_URL não configurada"}
    try:
        r = requests.get(base, headers=get_headers(), timeout=15)
        return {"ok": r.ok, "status_code": r.status_code, "resposta": r.text[:300]}
    except Exception as e:
        return {"ok": False, "erro": str(e)}


def buscar_resumo_demo():
    return {
        "orcamentos_abertos": 17,
        "clientes_proximos_recompra": 26,
        "clientes_em_risco": 11,
        "vendas_potenciais_hoje": 41200,
        "entregas_pendentes": 5,
    }
