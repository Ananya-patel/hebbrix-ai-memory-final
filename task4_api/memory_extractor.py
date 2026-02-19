
from llm_client import client
from config import MODEL

def extract_memories(text):
    prompt = f'''
Extract only long-term, user-specific facts worth remembering.
Ignore greetings and short-term context.
Return strictly as a Python list of strings.

Text:
{text}
'''
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role":"user","content":prompt}]
    )
    try:
        return eval(response.choices[0].message.content)
    except:
        return []
