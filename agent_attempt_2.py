from ollama import generate as ai
import asyncio


class Question:
    def __init__(self, Q='Who painted the Mona Lisa?', options=None, extra=None):
        if options is None:
            options = ['Leonardo da Vinci', 'Pablo Picasso', 'Claude Monet']
        self.q = Q
        self.options = options
        self.extra = extra  # optional context (e.g., a passage or hint)


def ai_func(func):
    def wrapper(q: Question):
        prompt = (
            f"Question: {q.q}\n"
            f"Options: {q.options}\n"
            f"Context: {q.extra or 'None'}\n\n"
            "Answer with exactly one of the options, nothing else."
        )
        result = asyncio.run(
            func(
                model='gemma3:1b',
                prompt=prompt,
                system="You are answering multiple-choice questions. Choose only from the provided options.",
                template=''
            )
        )
        print(f"Final Answer: {result}")
    return wrapper


@ai_func
async def ask_ai(model, prompt, system, template):
    # Run ollama.generate in a thread (non-blocking)
    response = await asyncio.to_thread(
        ai,
        model=model,
        prompt=prompt,
        system=system,
        template=template,
    )

    # response is a dict (no streaming now)
    full_text = response.get("response", "").strip().lower()

    # Post-process: return the first valid option that appears
    for opt in q.options:
        if opt.lower() in full_text:
            return opt

    # If no valid option found, return raw text
    return full_text


if __name__ == "__main__":
    q = Question()
    print("Q:", q.q)
    print("Options:", q.options)
    ask_ai(q)
