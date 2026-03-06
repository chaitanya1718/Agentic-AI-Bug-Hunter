import os
from dotenv import load_dotenv
from pydantic_ai import Agent

# Load environment variables
load_dotenv()

# Ensure API key is available
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


# Agent 1 — Code Analyzer
code_analyzer = Agent(
    "groq:llama-3.1-8b-instant",
    system_prompt="""
You analyze code snippets and detect suspicious lines.

Return possible bug lines as a list of line numbers.
"""
)


# Agent 2 — Bug Detector
bug_detector = Agent(
    "groq:llama-3.1-8b-instant",
    system_prompt="""
You detect the exact buggy line in code.

You will receive candidate bug lines.
Analyze the code carefully and return the exact buggy line number.

Return ONLY the line number.
"""
)


# Agent 3 — Explanation Generator
explanation_agent = Agent(
    "groq:llama-3.1-8b-instant",
    system_prompt="""
Explain software bugs in ONE short sentence.

Format:
Changed <wrong code> to <correct code>.
"""
)