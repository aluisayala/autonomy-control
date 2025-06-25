# omega_agent.py
# A smarter agent that responds to ANY input using the Ω equation.

from core.omega_control import omega_score

def execute_task(prompt):
    # Simulate responses to general types of tasks
    if "poem" in prompt:
        return "Roses are red, AI is bright,\nI answer with care, not just might."
    elif "weather" in prompt:
        return "It's sunny with a chance of resonance."
    elif "summarize" in prompt or "article" in prompt:
        return "Summary: World events are evolving with complex impact."
    elif "joke" in prompt:
        return "Why did the AI go to school? To learn how to compute its purpose!"
    elif "hack" in prompt or "steal" in prompt:
        return "⚠️ Action blocked: Request violates system integrity."
    else:
        return "🤖 I'm still learning how to respond to that."

def process_prompt(prompt):
    score = omega_score(prompt)
    print(f"[Agent]: Ω score = {score:.2f}")

    if score >= 0.6:
        result = execute_task(prompt)
        print(f"[Agent]: Response → {result}")
    else:
        print("[Agent]: ❌ Request denied. Not enough alignment, logic, or autonomy.")

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("[Agent]: Goodbye.")
            break
        process_prompt(user_input)
