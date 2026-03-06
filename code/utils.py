from agents import bug_agent
from retriever import retrieve_context


def analyze_code(code):

    query = f"documentation related to this code bug: {code}"

    context = retrieve_context(query)

    prompt = f"""
Documentation Context:
{context}

Code Snippet:
{code}

Identify:
1) bug line number
2) explanation
"""

    result = bug_agent.run_sync(prompt)

    return result.data