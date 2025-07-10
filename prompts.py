# prompts.py

def generator_prompt(entry):
    return f"""
You are a professional career assistant helping users write engaging LinkedIn posts.

Thought: I need to understand the achievement first.
Action: Reading details.
Observation:
Title: {entry['Title']}
Description: {entry['Description']}
Date: {entry['Date']}
Tags: {entry['Tags']}
Type: {entry['Type']}
Organization: {entry['Organization']}
Location: {entry['Location']}
Link: {entry['Link']}

Thought: This looks like a {entry['Type'].lower()} worth celebrating. I should highlight the impact and relevance.
Action: Write a compelling LinkedIn post in first person, starting with an emoji. Mention key points clearly, add hashtags and a call-to-action if suitable.

Final Post:
"""

def critic_prompt(draft):
    return f"""
You are a professional content reviewer. Your task is to critique the following LinkedIn post in terms of:

- Tone (professional yet friendly?)
- Clarity (easy to understand?)
- Engagement (emotion, call to action, hashtags?)
- Length (succinct or too long?)

Thought: Read the draft carefully and assess it.

Draft:
\"\"\"
{draft}
\"\"\"

Action: Provide constructive feedback with bullet points and an overall score out of 10.
"""

def refine_prompt(draft, feedback):
    return f"""
You previously wrote this LinkedIn post:

\"\"\"
{draft}
\"\"\"

Here’s the feedback:
\"\"\"
{feedback}
\"\"\"

Thought: I need to improve the post based on this feedback.
Action: Rewrite the post to make it more polished and effective, keeping the same structure.

Final Improved Post:
"""
