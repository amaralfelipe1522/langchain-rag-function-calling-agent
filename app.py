from retrievers.search_client import search_index
from dotenv import load_dotenv
from chains.chain_with_history import get_chain_with_history
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()

app = FastAPI()
chain = get_chain_with_history()

class QueryRequest(BaseModel):
    question: str
    session_id: str = "default"

@app.post("/ask")
async def ask_question(query: QueryRequest):
    search_results = search_index(query.question)
    context = " ".join(search_results)

    response = chain.invoke(
        {'input': query.question, 'context': context },
        config={'configurable': {'session_id': query.session_id}}
    )

    return {"answer": response.get("output", "Não foi possível gerar uma resposta.")}