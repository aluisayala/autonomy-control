# omega_control.py
# Core Ω Equation and Combined Model Logic

omega_score_memory = set()
omega_score_history = []

def omega_score(prompt, reward=1.0, repeat_penalty=True):
    S_align = 0.9 if any(k in prompt for k in ["write", "get", "summarize"]) else 0.6
    M_cog = 0.85
    A_auto = 0.95
    ZPE_term = 0.5  # Simulated zero-point influence factor
    R_reward = reward
    U_novelty = 1.0 if repeat_penalty and prompt in omega_score_memory else 0.0

    Ω = (
        0.35 * S_align +
        0.25 * M_cog +
        0.2 * A_auto +
        0.1 * R_reward +
        0.05 * ZPE_term -
        0.05 * U_novelty
    )
    omega_score_memory.add(prompt)
    omega_score_history.append((prompt, round(Ω, 4)))
    return round(Ω, 4)
