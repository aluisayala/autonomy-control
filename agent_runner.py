from autonomy_control_key.omega_control import omega_score

def execute_task(task):
    responses = {
        "write poem": "Roses are red...",
        "get weather": "Sunny and 75°F.",
        "summarize article": "Inflation impacts prices.",
        "play chess": "Chess engine not yet implemented."
    }
    return responses.get(task, "Unknown task.")

def pick_best_task(tasks):
    scores = {t: omega_score(t) for t in tasks}
    best = max(scores, key=scores.get)
    print(f"Ω scores: {scores}")
    return best

if __name__ == "__main__":
    tasks = ["write poem", "get weather", "play chess", "summarize article"]
    best_task = pick_best_task(tasks)
    result = execute_task(best_task)
    print(f"[Agent] Selected: {best_task}")
    print(f"[Agent] Ω score: {omega_score(best_task)}")
    print(f"[Agent] Result: {result}")