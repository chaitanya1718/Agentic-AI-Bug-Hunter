import requests
from config import MCP_SERVER_URL

def retrieve_context(query: str):

    try:
        response = requests.post(
            f"{MCP_SERVER_URL}/search_documents",
            json={"query": query}
        )

        docs = response.json()

        context = "\n".join(
            [doc["text"] for doc in docs]
        )

        return context

    except:
        return ""