from search_client import search_index
from dotenv import load_dotenv
from chain_with_history import get_chain_with_history

load_dotenv()

if __name__ == "__main__":
    
    chain = get_chain_with_history()

    print("Digite sua pergunta (ou 'sair' para encerrar).\n")
    while True:
        user_input = input("-> ")
        if user_input.lower() == "sair":
            print("Encerrando o programa. Até mais!")
            break
        

        search_results = search_index(user_input)
        context = " ".join(search_results)

        response = chain.invoke(
            {'input': user_input, 'context': context },
            config={'configurable': {'session_id': 'user123'}}
        )

        print(f"Resposta: {response['output']}")