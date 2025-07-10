# react_agent.py

from prompts import generator_prompt, critic_prompt, refine_prompt
import ollama

GENERATOR_MODEL = "llama3.2"
CRITIC_MODEL = "llama3.2:1b"

def generate_post(entry):
    prompt = generator_prompt(entry)
    response = ollama.generate(model=GENERATOR_MODEL, prompt=prompt)
    return response['response'].strip()

def critique_post(post):
    prompt = critic_prompt(post)
    response = ollama.generate(model=CRITIC_MODEL, prompt=prompt)
    return response['response'].strip()

def refine_post(post, feedback):
    prompt = refine_prompt(post, feedback)
    response = ollama.generate(model=GENERATOR_MODEL, prompt=prompt)
    return response['response'].strip()

def react_agent(entry):
    reasoning = []
    
    reasoning.append("Thought: I need the title, description, and context.")
    reasoning.append(f"Observation: Loaded entry — {entry['Title']}")

    draft = generate_post(entry)
    reasoning.append("Action: Generated draft.")
    
    feedback = critique_post(draft)
    reasoning.append("Action: Critique complete.")
    
    refined = refine_post(draft, feedback)
    reasoning.append("Action: Refined draft generated.")

    return {
        "reasoning": reasoning,
        "draft": draft,
        "feedback": feedback,
        "refined": refined
    }
