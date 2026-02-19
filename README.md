# Hebbrix AI Memory System — Final Submission

This repository contains my complete submission for the **Hebbrix AI Memory System assessment**.
It demonstrates both **practical implementation** and **system-level reasoning** around long-term
memory in conversational AI.

The project is intentionally designed to be:
- Explainable
- Cost-aware (free LLM stack)
- Modular
- Easy to evaluate and extend

---

##  Repository Structure
hebbrix-ai-memory-final/
│
├── task1_core/ # Task 1: Core AI Memory Chatbot (Groq-based)
│
├── task4_api/ # Task 4: FastAPI REST API + Docker
│
├── TASK_3_MEMORY_STRATEGY.md # Task 3: Memory decision design write-up
│
├── README.md # (this file)
└── .gitignore

##  Task 1 — Core AI Memory Engine

A terminal-based AI chatbot that:

- Extracts long-term user facts using an LLM  
- Stores memories persistently in JSON  
- Retrieves relevant memories via cosine similarity  
- Injects memory into prompts for personalized responses  

### Highlights

- Uses **Groq (free)** instead of paid APIs  
- Clear memory extraction → storage → retrieval loop  
- Modular design (`memory_store`, `memory_extractor`, `llm_client`)  
- Transparent and explainable behavior  

 **Location:** `task1_core/`

---

##  Task 3 — How Should AI Decide What to Remember?

A **500–800 word design write-up** exploring intelligent memory policies for AI systems, including:

- Recency-based decay  
- Importance scoring via LLMs  
- Frequency-based reinforcement  
- MANN-inspired memory slot management  
- Hybrid strategies for scalable assistants  

The write-up emphasizes **original reasoning over citations**, with a strong connection to how humans remember and forget.

 **Location:** `TASK_3_MEMORY_STRATEGY.md`

---

##  Task 4 — Memory System REST API

A production-style **FastAPI** service that exposes the memory system via REST endpoints.

### Endpoints

- `GET /health`  
- `POST /memories`  
- `GET /memories/search?q=...`  
- `GET /memories`  
- `DELETE /memories/{id}`  
- `POST /evaluate`  

### Features

- Input validation & error handling  
- Configurable top-k retrieval  
- Similarity-based search  
- Dockerfile for containerized deployment  
- Swagger UI for interactive testing  

 **Location:** `task4_api/`

---

##  Tech Stack

- **LLM:** Groq (LLaMA family)  
- **Retrieval:** Cosine similarity (RAG-style)  
- **Storage:** JSON (simple, portable)  
- **API:** FastAPI  
- **Deployment:** Docker (Task 4)  

---

##  Design Philosophy

This system prioritizes:

- Useful memory density over memory size  
- Explainability over black-box behavior  
- Practical engineering trade-offs  
- Clean separation of concerns  

The goal is not to remember everything — but to **remember the right things**.

---

##  Notes for Reviewers

- All tasks are intentionally consolidated into a single clean repository.  
- Groq is used to allow **free, reproducible evaluation**.  
- No secrets, API keys, or virtual environments are committed.  
- Each task can be evaluated independently.  

Thank you for reviewing!


