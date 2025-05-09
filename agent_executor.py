from langchain.agents.openai_functions_agent.base import create_openai_functions_agent
from langchain.agents import AgentExecutor
from prompt_template import get_prompt_template
from tools import tools
from chat_openai_client import get_chat_openai_client

def get_agent_executor():
    prompt = get_prompt_template()
    llm = get_chat_openai_client()

    agent = create_openai_functions_agent(
        tools=tools,
        llm=llm,
        prompt=prompt
    )

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

    return agent_executor