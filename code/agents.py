import os
from dotenv import load_dotenv
from pydantic_ai import Agent

# Load environment variables
load_dotenv()

# Ensure GROQ key exists
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
MODEL = "groq:llama-3.1-8b-instant"

# Agent 1 – Code Analyzer
code_analyzer = Agent(
    MODEL,
    system_prompt="""
You analyze C++ test code using Infineon RDI APIs.

Your job:
Identify suspicious lines where a bug might exist.

Return line numbers only.
Example:
5
or
3,4
"""
)

# Agent 2 – Bug Locator
bug_locator = Agent(
    MODEL,
    system_prompt="""
You detect the exact bug line.

You will receive:
- Code snippet
- Candidate bug lines
- Documentation retrieved from Infineon manual

Return ONLY the final bug line number.
"""
)

# Agent 3 – Explanation Agent
explanation_agent = Agent(
    MODEL,
    system_prompt="""
Explain the bug in ONE short sentence.

Format:
Changed <wrong code> to <correct code>.
"""
)