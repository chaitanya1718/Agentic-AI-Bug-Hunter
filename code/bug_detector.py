from agents import code_analyzer, bug_locator, explanation_agent
from mcp_client import search_docs


def shorten_code(code, max_lines=40):
    lines = code.split("\n")
    return "\n".join(lines[:max_lines])


def detect_bug(code, correct_code):

    code = shorten_code(code)

    # Agent 1: Analyze code
    analyzer_prompt = f"""
Analyze this C++ test code and find suspicious lines.

Code:
{code}
"""

    candidate_lines = code_analyzer.run_sync(analyzer_prompt).output

    # Retrieve documentation using MCP
    query = f"Infineon RDI bug patterns related to these lines: {candidate_lines}"
    context = search_docs(query)

    # Agent 2: Detect exact bug
    bug_prompt = f"""
Code:
{code}

Candidate lines:
{candidate_lines}

Documentation:
{context}

Find the exact buggy line.
Return only the line number.
"""

    bug_line = bug_locator.run_sync(bug_prompt).output

    # Agent 3: Explanation
    explanation_prompt = f"""
Code:
{code}

Bug line:
{bug_line}

Documentation:
{context}

Explain the bug briefly.
"""

    explanation = explanation_agent.run_sync(explanation_prompt).output

    return bug_line, explanation