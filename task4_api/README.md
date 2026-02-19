
# Task 4 – AI Memory System REST API

This project wraps the AI memory system in a REST API using FastAPI.

## Required Endpoints
- POST /memories
- GET /memories/search?q=...
- GET /memories
- DELETE /memories/{id}

## Run locally
pip install -r requirements.txt
uvicorn api:app --reload

## Docker
docker build -t ai-memory-api .
docker run -p 8000:8000 ai-memory-api
