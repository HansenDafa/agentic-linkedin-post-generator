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

def multi_agent_pipeline(entry, style="inspirational"):
    log = []

    # ✍️ Generator Agent
    log.append("🔹 [Generator] Creating first draft...")
    draft = call_ollama(GEN_MODEL, generator_prompt(entry))
    log.append(draft)

    # 🧐 Critic Agent
    log.append("🔹 [Critic] Reviewing the draft...")
    feedback = call_ollama(CRITIC_MODEL, critic_prompt(draft))
    log.append(feedback)

    # ✍️ Rewriting with Critique
    log.append("🔹 [Generator] Improving based on critique...")
    improved = call_ollama(GEN_MODEL, refine_prompt(draft, feedback))
    log.append(improved)

    # 🎨 Stylist Agent
    log.append(f"🔹 [Stylist] Applying '{style}' style...")
    styled = call_ollama(STYLE_MODEL, stylist_prompt(improved, style))
    log.append(styled)

    # 📊 Optimizer Agent
    log.append("🔹 [Optimizer] Final polish (hashtags, CTA, emojis)...")
    optimized = call_ollama(OPTIMIZER_MODEL, optimizer_prompt(styled, entry))
    log.append(optimized)

    return {
        "log": log,
        "final": optimized
    }
