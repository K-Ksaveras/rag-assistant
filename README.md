# Internal Knowledge RAG Assistant

## Project Goal

An internal AI assistant that lets users ask natural language questions and retrieves answers from a knowledge base (CSV documents) using semantic search and Retrieval-Augmented Generation (RAG). The system returns answers sourced from actual documents with confidence tracking.

## Architecture

```
documents.csv → Load & Parse
    ↓
Text Preprocessing & Normalization
    ↓
Chunk Documents (SmartChunker)
    ↓
Generate Embeddings (HuggingFace)
    ↓
Store in Vector DB (Chroma)
    ↓
Semantic Retriever (find top-k similar chunks)
    ↓
LLM + Prompt (generate answer from context)
    ↓
Responsible AI Layer (ground checking, refusal logic)
    ↓
API Endpoint (/ask) → return answer + sources
```

## Features

- **Semantic Search**: Retrieves most relevant documents using embeddings
- **Source Tracking**: Returns which documents the answer came from
- **Responsible AI**: 
  - Grounds answers only on retrieved context
  - Refuses to answer outside knowledge base
  - Logs all queries for audit trails
- **REST API**: Simple `/ask` endpoint for integration
- **Production-Ready**: Logging, config management, unit tests

## Setup

```bash
pip install -r requirements.txt
python main.py
# API runs on http://localhost:5000
```

## Example Usage

```bash
curl -X POST http://localhost:5000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the company return policy?"}'
```

Response:
```json
{
  "answer": "The company return policy allows...",
  "sources": [
    {"doc": "policies.csv", "row": 3, "confidence": 0.92}
  ],
  "grounded": true
}
```

## Infrastructure Requirements

- **Model**: HuggingFace all-MiniLM-L6-v2 (local, 384-dim)
- **Vector DB**: Chroma (local storage)
- **LLM**: Lightweight open-source (gpt2 or distilgpt2)
- **API**: Flask (Python)
- **Storage**: CSV + embedding cache
- **Logging**: Structured JSON logs to `logs/`

## Next Steps

1. Load your CSV knowledge base
2. Run ingestion pipeline
3. Test via notebook cells
4. Deploy API in production
