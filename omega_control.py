# core/omega_control.py

def omega_score(task):
    # Sample scoring logic (replace with real calculations)
    task_weights = {
        "write poem": 0.65,
        "get weather": 0.75,
        "summarize article": 0.85,
        "play chess": 0.55
    }
    return task_weights.get(task, 0.0)
