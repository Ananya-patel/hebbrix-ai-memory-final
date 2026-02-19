from llm_client import client
from config import MODEL
from memory_extractor import extract_memories
from memory_store import add_memory, retrieve_memories

print("Groq AI Memory Bot (type exit)")
log = ""

while True:
    u = input("You: ")
    if u=="exit": break
    log += f"User: {u}\n"
    mem = retrieve_memories(u)

    sys = "You are a helpful AI assistant."
    if mem:
        sys += "\nUser facts:\n" + "\n".join(f"- {x}" for x in mem)

    r = client.chat.completions.create(
        model=MODEL,
        messages=[{"role":"system","content":sys},{"role":"user","content":u}]
    )
    a = r.choices[0].message.content
    print("AI:",a)
    log += f"AI: {a}\n"

    for f in extract_memories(log):
        add_memory(f)
    log = ""
