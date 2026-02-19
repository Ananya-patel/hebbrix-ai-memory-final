
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

from memory_extractor import extract_memories
from memory_store import add_memory, retrieve_memories, load, save

app = FastAPI(title="AI Memory System API", version="1.1")

class MemoryRequest(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok", "memory_count": len(load())}

@app.post("/memories")
def create_memory(req: MemoryRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    extracted = extract_memories(req.text)
    if not extracted:
        raise HTTPException(status_code=400, detail="No valid memories extracted")

    stored = []
    for fact in extracted:
        mem_id = str(uuid.uuid4())
        add_memory(fact, mem_id)
        stored.append({"id": mem_id, "text": fact})

    return {"stored": stored}

@app.get("/memories/search")
def search_memories(q: str, top_k: int = 3):
    if not q.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    return {"results": retrieve_memories(q, k=top_k)}

@app.get("/memories")
def list_memories():
    return load()

@app.delete("/memories/{memory_id}")
def delete_memory(memory_id: str):
    memories = load()
    for i, m in enumerate(memories):
        if m["id"] == memory_id:
            deleted = memories.pop(i)
            save(memories)
            return {"deleted": deleted}
    raise HTTPException(status_code=404, detail="Memory not found")

@app.post("/evaluate")
def evaluate():
    tests = {"dinner": "Italian", "allergy": "peanut"}
    report = {}
    for q, expected in tests.items():
        res = retrieve_memories(q, k=1)
        passed = bool(res) and expected.lower() in res[0]["text"].lower()
        report[q] = {"retrieved": res, "pass": passed}
    return report
@app.get("/")
def root():
    return {
        "message": "AI Memory System API is running",
        "docs": "/docs"
    }
