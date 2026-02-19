import json, os, numpy as np
from embeddings import get_embedding

FILE = "memories.json"

def load():
    if not os.path.exists(FILE): return []
    return json.load(open(FILE))

def save(m): json.dump(m, open(FILE,"w"), indent=2)

def add_memory(text):
    m = load()
    m.append({"text":text,"embedding":get_embedding(text).tolist()})
    save(m)

def cosine(a,b):
    a,b = np.array(a), np.array(b)
    return (a@b)/(np.linalg.norm(a)*np.linalg.norm(b))

def retrieve_memories(q,k=3):
    m = load()
    if not m: return []
    qe = get_embedding(q)
    scored = [(cosine(qe,x["embedding"]),x["text"]) for x in m]
    scored.sort(reverse=True)
    return [x[1] for x in scored[:k]]
