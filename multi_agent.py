# multi_agent.py

import ollama
from prompts import generator_prompt, critic_prompt, refine_prompt, stylist_prompt, optimizer_prompt

GEN_MODEL = "llama3.2"
CRITIC_MODEL = "llama3.2:1b"
STYLE_MODEL = "llama3.2:1b"
OPTIMIZER_MODEL = "llama3.2"

def call_ollama(model, prompt):
    response = ollama.generate(model=model, prompt=prompt)
    return response['response'].strip()

def multi_agent_pipeline(entry, style="inspirational", iterations=2):
    log = []

    draft = call_ollama(GEN_MODEL, generator_prompt(entry))
    log.append("🔹 Initial draft:")
    log.append(draft)

    for i in range(iterations):
        log.append(f"🔁 Iteration {i+1}: Critique + Improve")

        feedback = call_ollama(CRITIC_MODEL, critic_prompt(draft))
        log.append(f"🧐 Critique:\n{feedback}")

        draft = call_ollama(GEN_MODEL, refine_prompt(draft, feedback))
        log.append(f"✍️ Revised:\n{draft}")

    # Final stylist + polish
    styled = call_ollama(STYLE_MODEL, stylist_prompt(draft, style))
    log.append(f"🎨 Stylist applied ({style})")

    final = call_ollama(OPTIMIZER_MODEL, optimizer_prompt(styled, entry))
    log.append("📊 Optimized with hashtags + CTA")

    return {
        "log": log,
        "final": final
    }
