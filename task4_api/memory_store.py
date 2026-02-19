
import json, os, numpy as np
from embeddings import get_embedding

FILE = "memories.json"

def load():
    if not os.path.exists(FILE):
        return []
    return json.load(open(FILE))

def save(memories):
    json.dump(memories, open(FILE, "w"), indent=2)

def add_memory(text, mem_id):
    memories = load()
    memories.append({
        "id": mem_id,
        "text": text,
        "embedding": get_embedding(text).tolist()
    })
    save(memories)

def cosine(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve_memories(query, k=3):
    memories = load()
    if not memories:
        return []
    q_emb = get_embedding(query)
    scored = [(cosine(q_emb, m["embedding"]), {"id": m["id"], "text": m["text"]}) for m in memories]
    scored.sort(reverse=True)
    return [x[1] for x in scored[:k]]
