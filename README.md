# NOVA IA — Assistente Executiva da NovaPrint

Primeira versão funcional em Streamlit.

## O que já tem

- Centro de comando da NovaPrint
- Chat com a NOVA IA
- Tarefas e prioridades
- Comercial
- Financeiro
- Operação / Entregas / Impressoras
- Marketing
- Estrutura pronta para conectar:
  - OpenAI API
  - Supabase
  - GestãoClick
  - waTidy / Wascript

## Como rodar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Configuração da IA

Crie um arquivo `.env` baseado em `.env.example`:

```env
OPENAI_API_KEY=sua_chave_openai
OPENAI_MODEL=gpt-4.1-mini
```

Sem a chave, o app abre, mas o chat fica em modo demonstrativo.

## Como subir no Streamlit Cloud

1. Crie um repositório no GitHub.
2. Envie todos os arquivos deste projeto.
3. No Streamlit Community Cloud, escolha o repositório.
4. Main file path: `app.py`.
5. Em Secrets, cole as variáveis:

```toml
OPENAI_API_KEY="sua_chave_openai"
OPENAI_MODEL="gpt-4.1-mini"
SUPABASE_URL="https://seu-projeto.supabase.co"
SUPABASE_KEY="sua_chave"
GESTAOCLICK_API_URL="https://api.gestaoclick.com.br"
GESTAOCLICK_API_TOKEN="seu_token"
WATIDY_API_URL="https://api-whatsapp.wascript.com.br"
WATIDY_TOKEN="seu_token"
WATIDY_SEND_PATH="/send-message"
```

## SQL sugerido no Supabase

```sql
create table if not exists nova_snapshots (
  chave text primary key,
  salvo_em timestamptz default now(),
  origem text,
  payload jsonb
);

create table if not exists nova_tarefas (
  id uuid primary key default gen_random_uuid(),
  criada_em timestamptz default now(),
  area text,
  prioridade text,
  tarefa text,
  status text default 'Pendente',
  responsavel text,
  vencimento date,
  observacao text
);

create table if not exists nova_conversas (
  id uuid primary key default gen_random_uuid(),
  criada_em timestamptz default now(),
  usuario text,
  pergunta text,
  resposta text,
  contexto jsonb
);
```

## Próxima etapa recomendada

1. Subir este app no Streamlit.
2. Configurar `OPENAI_API_KEY`.
3. Criar tabelas no Supabase.
4. Conectar primeiro o módulo Comercial ao GestãoClick.
5. Depois conectar tarefas, WhatsApp e impressoras locadas.
