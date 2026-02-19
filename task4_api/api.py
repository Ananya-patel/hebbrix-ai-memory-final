
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

from memory_extractor import extract_memories
from memory_store import add_memory, retrieve_memories, load, save

app = FastAPI(title="AI Memory System API")

class MemoryRequest(BaseModel):
    text: str

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
def search_memories(q: str):
    if not q.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    return {"results": retrieve_memories(q)}

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
