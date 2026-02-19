#  Simple AI Memory Chatbot (Groq-Based, Free)

A Python terminal chatbot that automatically remembers important user facts from past conversations and reuses them to generate personalized responses in future sessions.

This project is a **working prototype** that demonstrates the core AI memory loop:

**store → retrieve → use**

---

##  What This Project Builds

- Interactive **terminal-based chatbot**
- Uses a **Large Language Model (Groq – LLaMA 3)** for reasoning and response generation
- Automatically extracts **durable, user-specific facts** from conversations
- Stores memories persistently in a local **JSON file**
- Retrieves relevant memories using **cosine similarity over vector embeddings**
- Injects retrieved memories into the system prompt for personalization
- **100% free setup** (no OpenAI, no paid APIs)

---

##  High-Level Architecture
User Input
↓
Memory Retrieval (cosine similarity)
↓
Prompt Builder (injects memories)
↓
LLM Response (Groq)
↓
Memory Extraction (LLM)
↓
Persistent Storage (memories.json)


---

##  End-to-End Flow

1. User sends a message in the terminal.
2. The system retrieves the most relevant stored memories.
3. Retrieved memories are injected into the assistant’s system prompt.
4. Groq LLM generates a personalized response.
5. The full turn (user + assistant) is analyzed.
6. Long-term, user-specific facts are extracted.
7. New memories are embedded, deduplicated, and stored in `memories.json`.

---

##  Project Structure
hebbrix_task1_groq/
├── chat.py # Main chat loop
├── config.py # API key and model config
├── llm_client.py # Shared Groq client
├── memory_extractor.py # LLM-based memory extraction
├── memory_store.py # Memory storage & retrieval logic
├── embeddings.py # Local embedding model
├── memories.json # Persistent memory database
└── README.md


---

##  Memory Representation

Each memory is stored as a JSON object:

```json
{
  "text": "User is allergic to peanuts",
  "embedding": [0.0123, -0.884, ...]
}

##  How Memory Retrieval Works

- The user query is converted into a vector embedding.
- Stored memories are compared using **cosine similarity**.
- The **Top-K most similar memories** are selected.
- These memories are injected into the **system prompt**.
- The LLM uses them to generate a **personalized response**.

This approach satisfies the requirement for **simple storage + cosine similarity**, without requiring a vector database.

---

##  Setup & Run Instructions

### ️1. Create and activate a virtual environment
```bash
python -m venv venv
.\venv\Scripts\activate   # Windows


2. Install dependencies
pip install groq sentence-transformers numpy

3.Add your Groq API key
GROQ_API_KEY = "your_groq_api_key_here"
MODEL = "llama-3.1-8b-instant"



4.Run the chatbot
python chat.py

## Example Interaction
You: Hi, I'm Priya. I love Italian food and I'm allergic to peanuts.
AI: Nice to meet you, Priya! I’ll keep that in mind.
##Conversation 2 (new session)

You: What should I eat tonight?
AI: Since you love Italian food and are allergic to peanuts,
a peanut-free pasta dish could be a great option.


## Design Tradeoffs

Used local sentence-transformers embeddings instead of hosted embeddings for cost-free operation

Used JSON storage instead of a vector database for transparency and simplicity

Memory extraction relies on LLM reasoning rather than rule-based heuristics

Single-user memory (no session or user IDs)


## Improvements With More Time

Embedding-based vector database (FAISS / ChromaDB)

Memory importance scoring and decay

Multi-user support with profile IDs

Memory update and correction logic

REST API wrapper (FastAPI)

Memory inspection / editing UI

Quantitative memory retrieval evaluation









