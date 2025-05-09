from langchain_openai import AzureChatOpenAI
import getpass
import os

# GPT 3.5 Turbo:
#     api_version = "2023-03-15-preview"
#     deployment_id="gpt-35-turbo"

# GPT 4o:
#     api_version = "2024-05-01-preview"
#     deployment_id="gpt-4o"

def get_chat_openai_client():
    if "AZURE_OPENAI_API_KEY" not in os.environ:
        os.environ["AZURE_OPENAI_API_KEY"] = getpass.getpass(
            "Enter your AzureOpenAI API key: "
        )
    os.environ["AZURE_OPENAI_ENDPOINT"] = "https://openaibs.openai.azure.com/"

    llm = AzureChatOpenAI(
        azure_deployment="gpt-4o",
        model="gpt-4o",
        api_version="2024-05-01-preview",
        temperature=0.7,
        max_tokens=None,
        timeout=None,
        max_retries=2
    )

    return llm