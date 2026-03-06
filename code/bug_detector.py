from agents import explanation_agent
from mcp_client import search_docs


# Detect bug line using diff between Code and Correct Code
def find_bug_line(code, correct_code):

    code_lines = code.split("\n")
    correct_lines = correct_code.split("\n")

    for i in range(min(len(code_lines), len(correct_lines))):
        if code_lines[i] != correct_lines[i]:
            return i + 1

    return "Unknown"


# Limit code size to avoid token overflow
def shorten_code(code, max_lines=40):

    lines = code.split("\n")
    return "\n".join(lines[:max_lines])


def detect_bug(code, correct_code):

    # shorten code
    code = shorten_code(code)

    # detect bug line without LLM
    bug_line = find_bug_line(code, correct_code)

    # retrieve documentation from MCP
    query = f"Explain bug in this code: {code}"
    context = search_docs(query)

    explanation_prompt = f"""
Documentation:
{context}

Code:
{code}

Bug line:
{bug_line}

Explain the bug in one short sentence.
"""

    explanation = explanation_agent.run_sync(explanation_prompt).output

    return bug_line, explanation