from ollama import generate as ai
import asyncio
from random import choice

class JokeRequest:
    def __init__(self, topic: str = None, style: str = None):
        self.topic = topic or choice([
            "computers", "cats", "programmers", "math", "the office"
        ])
        self.style = style or choice([
            "one-liner", "dad joke", "pun", "knock-knock"
        ])

def ai_func(func):
    def wrapper(req: JokeRequest):
        prompt = (
            f"Generate a {req.style} joke about {req.topic}."
        )
        asyncio.run(func(
            model='gemma3:1b',
            prompt=prompt,
            system=(
                "You are a joke-writing AI. "
                "Write a single joke in the style requested, "
                "no explanation, no extra text."
            ),
            template=''
        ))
        print()
    return wrapper

@ai_func
async def make_joke(model, prompt, system, template):
    def run_model():
        return ai(
            model=model,
            prompt=prompt,
            system=system,
            template=template,
            stream=True
        )
    response = await asyncio.to_thread(run_model)
    for chunk in response:
        if chunk.get('done') == 'stop':
            break
        print(chunk.get('response', ''), end='', flush=True)

for _ in range(5):
    req = JokeRequest()
    make_joke(req)
    print(f"[{req.style} about {req.topic}]", end='\n\n')


