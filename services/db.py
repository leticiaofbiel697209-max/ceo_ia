import os
from datetime import datetime
from typing import Dict, Any, List

try:
    from supabase import create_client
except Exception:
    create_client = None


def get_supabase():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    if not url or not key or not create_client:
        return None
    return create_client(url, key)


def save_snapshot(chave: str, origem: str, payload: Dict[str, Any]):
    client = get_supabase()
    if not client:
        return False
    data = {
        "chave": chave,
        "salvo_em": datetime.utcnow().isoformat(),
        "origem": origem,
        "payload": payload,
    }
    client.table("nova_snapshots").upsert(data).execute()
    return True


def list_tasks_demo() -> List[Dict[str, Any]]:
    return [
        {"prioridade": "Alta", "area": "Comercial", "tarefa": "Verificar orçamentos sem retorno", "status": "Pendente"},
        {"prioridade": "Alta", "area": "CRM", "tarefa": "Ligar para clientes próximos da recompra", "status": "Pendente"},
        {"prioridade": "Média", "area": "Operação", "tarefa": "Conferir entregas pendentes", "status": "Pendente"},
        {"prioridade": "Média", "area": "Impressoras", "tarefa": "Checar solicitações de toner", "status": "Pendente"},
        {"prioridade": "Baixa", "area": "Marketing", "tarefa": "Criar postagem do dia", "status": "Pendente"},
    ]
