
# Task 4+ – AI Memory System REST API

This project exposes an AI-powered memory system as a REST API using **FastAPI**.  
It wraps the core memory engine (extraction, storage, and retrieval) behind clean, well-documented endpoints and adds production-oriented enhancements.

The system is designed to be **simple, explainable, and extensible**, while demonstrating real-world backend and ML integration skills.

---

##  Features & Endpoints

### Core Endpoints
- **GET `/health`** – Service health check and memory count  
- **POST `/memories`** – Extract and store long-term user memories  
- **GET `/memories/search?q=...&top_k=...`** – Semantic memory retrieval  
- **GET `/memories`** – List all stored memories  
- **DELETE `/memories/{id}`** – Delete a specific memory  
- **POST `/evaluate`** – Lightweight memory evaluation endpoint  

---

##  Highlights

- FastAPI-based REST interface with automatic validation
- Semantic memory retrieval using cosine similarity
- Configurable `top_k` results for flexible search behavior
- Similarity scores returned for transparency and debugging
- Health and evaluation endpoints for production readiness
- Interactive **Swagger UI**
- Docker support for reproducible execution

---

##  Running the Project

```bash
pip install -r requirements.txt
uvicorn api:app --reload
generates interactive API documentation.

After running the server, open:

http://127.0.0.1:8000/docs

From Swagger UI you can:
- Create new memories
- Search stored memories
- List all memories
- Delete memories by ID
- Check service health
- Run lightweight evaluation tests

## Demo Screenshots



### Creating a Memory (POST /memories)
![Create Memory](hebbrix_task4_api/screenshots/Screenshot 2026-02-19 073729.png)

### Searching Memories (GET /memories/search)
![Search Memories]()

### Evaluation Endpoint
![Evaluate](screenshots/evaluate.png)



## Design Decisions

- Used FastAPI for automatic validation and documentation
- Chose JSON storage and local embeddings for simplicity and transparency
- Exposed top-k as a query parameter for configurable retrieval
- Added health and evaluation endpoints to simulate production concerns
- Prioritized explainability over heavy infrastructure

##  Improvements With More Time

Given additional time and resources, the system could be extended in the following ways to improve robustness, scalability, and usability:

### 1. Semantic Vector Database
- Replace JSON-based storage with a vector database such as **FAISS** or **ChromaDB**.
- This would enable faster similarity search and better scalability as memory size grows.
- Would also support approximate nearest neighbor (ANN) search for large datasets.

### 2. Memory Lifecycle Management
- Introduce memory importance scoring and decay over time.
- Allow memories to be updated, corrected, or forgotten when user preferences change.
- Add explicit user feedback signals (e.g., reinforce or demote memories).

### 3. Multi-User & Session Support
- Extend the system to support multiple users with isolated memory profiles.
- Associate memories with user IDs and session IDs.
- Enable personalization across devices and sessions.

### 4. Stronger Evaluation & Metrics
- Expand the evaluation endpoint into a full benchmark suite.
- Measure retrieval accuracy, relevance ranking, and memory precision/recall.
- Add automated regression tests for memory quality as prompts or models change.

### 5. Security & Configuration Improvements
- Move API keys and configuration to environment variables or a secrets manager.
- Add request rate limiting and basic authentication for production use.
- Introduce request logging and monitoring hooks.

### 6. Web Interface & Memory Inspector
- Build a lightweight web UI to visualize, edit, and delete memories.
- Allow human inspection of embeddings, similarity scores, and retrieval decisions.
- Useful for debugging, demos, and non-technical stakeholders.

### 7. Model Abstraction Layer
- Abstract the LLM and embedding providers behind a clean interface.
- Enable easy switching between different models or providers.
- Improve long-term maintainability and experimentation speed.

These improvements were intentionally scoped out to keep the current implementation simple, explainable, and focused on core memory mechanics.



