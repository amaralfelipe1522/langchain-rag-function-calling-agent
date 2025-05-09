from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def get_prompt_template():
    promptTemplate = """Com base no seguinte contexto, caso houver: {context} e responda a pergunta: {input}; Historico: {history}"""

    prompt = ChatPromptTemplate.from_messages([
        ("system", promptTemplate),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="history"),
    ])

    return prompt