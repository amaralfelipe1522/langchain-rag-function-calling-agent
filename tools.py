import requests
from langchain.tools import tool

@tool
def fetch_cep_info(cep: str):
    """
    Função para buscar informações do CEP usando a API ViaCEP.
    """
    url = f"https://viacep.com.br/ws/{cep}/json/"
    print("CHAMOU O FETCH CEP:::::::::")
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    
tools = [fetch_cep_info]