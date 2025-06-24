# agent_runner.py
# Runs the agent using the Ω score to select and simulate a task

from core.omega_control import omega_score

def execute_task(prompt):
    responses = {
        "write poem": "Roses are red...",
        "get weather": "Sunny and 75°F.",
        "summarize article": "Inflation impacts prices.",
        "play chess": "Chess engine not yet implemented."
    }
    return responses.get(prompt, "Unknown task.")

def pick_best_task(prompts):
    scores = {p: omega_score(p) for p in prompts}
    print("Ω scores:", scores)
    return max(scores, key=scores.get)

if __name__ == "__main__":
    prompts = ["write poem", "get weather", "play chess", "summarize article"]
    best = pick_best_task(prompts)
    result = execute_task(best)
    print(f"[Agent]: Selected → '{best}'
[Output]: {result}")
