def calculator(expression: str):
    """Very tiny calculator tool."""

    try:
        result = eval(expression)
        return str(result)

    except Exception:
        return "Invalid expression"


def ask_llm(prompt: str):
    """
    Placeholder.
    Later we'll connect this to Ollama.
    """

    return f"LLM would answer: {prompt}"