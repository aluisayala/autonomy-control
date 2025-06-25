# omega_agent.py
# Uses the Ω equation to select and execute the best task.

from core.omega_control import omega_score

def execute_task(prompt):
    responses = {
        "write poem": "Roses are red, AI is bold,\nI chose this task with logic and gold.",
        "get weather": "Currently sunny, 75°F, mild wind.",
        "summarize article": "Inflation continues to influence markets and prices.",
        "play chess": "Chess engine not implemented."
    }
    return responses.get(prompt, "Unknown task.")

def pick_best_task(prompts):
    scores = {p: omega_score(p) for p in prompts}
    print("[Agent]: Ω scores →", scores)
    return max(scores, key=scores.get)

if __name__ == "__main__":
    prompts = ["write poem", "get weather", "play chess", "summarize article"]
    best = pick_best_task(prompts)
    print(f"[Agent]: Selected → '{best}'")
    print(f"[Agent]: Ω score = {omega_score(best)}")
    print(f"[Agent]: Result → {execute_task(best)}")
