from google import genai
from dotenv import load_dotenv
from google.genai import types
load_dotenv()

client= genai.Client()

SYSTEM_PROMPT = """
You are a helpful and professional assistant. 
- Always follow rules: respond accurately and clearly.
- Maintain context from the conversation history.
- Use deterministic outputs when needed.
- Do not hallucinate facts; if info is missing, say "I don't know".
"""


history=[]
def chat_func(user_input:str):
    global history
    history.append(f"User :{user_input}")
    history[:]=history[-5:]
    conversation="\n".join(history)
    prompt=(f"\n {SYSTEM_PROMPT} \n conversation so far {conversation}\n")
    response=client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt,
    config=types.GenerateContentConfig(
            max_output_tokens=400
        )

    )
    bot_reply=response.text.strip()
    history.append(bot_reply)
    history[:]=history[-5:]
    return bot_reply

