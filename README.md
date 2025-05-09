# Agente de IA com RAG, Function Calling e Memória de Conversa
Aplicação desenvolvida com LangChain que integra um agente de linguagem utilizando Azure OpenAI com suporte a Function Calling, recuperação de contexto via RAG (Retrieval-Augmented Generation) e gerenciamento de histórico de conversas. O agente é capaz de responder perguntas com base em contexto externo, acionar ferramentas dinamicamente e manter a continuidade do diálogo com memória persistente.

## Passo a Passo

1. Instale as dependências do projeto:
```sh
pip install -r requirements.txt
```
2. Subir a aplicação na porta 8080
```sh
uvicorn app:app --reload --port 8080
```
3. Teste via cURL
```sh
curl -X POST "http://127.0.0.1:8080/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "Como cadastrar um cliente?", "session_id": "user123"}'
```

Documentação estará disponível em http://127.0.0.1:8080/docs
