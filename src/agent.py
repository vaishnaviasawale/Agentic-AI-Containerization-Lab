from src.tools import calculator, ask_llm


def execute(task: str):

    task_lower = task.lower()

    if any(word in task_lower for word in ["calculate", "+", "-", "*", "/"]):

        expression = (
            task_lower
            .replace("calculate", "")
            .strip()
        )

        return {
            "tool": "calculator",
            "result": calculator(expression)
        }

    return {
        "tool": "llm",
        "result": ask_llm(task)
    }