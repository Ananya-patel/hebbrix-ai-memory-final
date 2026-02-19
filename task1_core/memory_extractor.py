from llm_client import client
from config import MODEL

def extract_memories(conversation_text):
    prompt = f"""Extract only long-term, user-specific facts.
Return strictly as Python list of strings.

Conversation:
{conversation_text}"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role":"user","content":prompt}]
    )
    try:
        return eval(response.choices[0].message.content)
    except:
        return []
