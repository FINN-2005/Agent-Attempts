# Agent-Attempts

My experiments and attempts at building simple AI **"agents"** using [Ollama](https://ollama.ai) models in Python.  

## Overview
This repo contains small demos that showcase different ways of structuring prompts, wrapping model calls, and making the model behave like an *agent* that answers questions or performs tasks.

### Current Demos
- **Joke Generator**  
  Generates jokes on random topics and styles (`dad joke`, `pun`, `one-liner`, `knock-knock`).

- **Multiple-Choice Q&A**  
  Asks a trivia-style question (e.g., *"Who painted the Mona Lisa?"*) and forces the model to pick from a list of options.

## How It Works
- Uses `ollama.generate` inside an async wrapper.  
- Prompts are wrapped with clear instructions (system + user prompt).  
- Post-processing ensures outputs map cleanly to provided options.  

## Example: Multiple-Choice Q&A
```bash
q = Question(
    Q="Who painted the Mona Lisa?",
    options=["Leonardo da Vinci", "Pablo Picasso", "Claude Monet"]
)
ask_ai(q)
```

**Output:**
```bash
Q: Who painted the Mona Lisa?
Options: ["Leonardo da Vinci", "Pablo Picasso", "Claude Monet"]
Final Answer: Leonardo da Vinci
```

## Goals
- Explore ways to **constrain LLM outputs**.  
- Experiment with **agent-like wrappers** for task-specific AI.  
- Build toward more complex, reliable “agents.”  

## Requirements
- Python 3.9+  
- [Ollama](https://ollama.ai) installed and running. (also do ```pip install ollama```)
- Download any small llm, the code uses Gemma3:1B by default (```ollama pull gemma3:1b```)
- `pip install asyncio` (built-in for Python 3.7+, so usually no extra install needed).

## Running
1) Joke Agent
```bash
python agent_attempt_1.py
```
2) MCQ Agent
```bash
python mcq_agent.py
```
