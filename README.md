RAG System for Netflix Movies: Semantic Search, Embeddings & LangChain Pipeline
A production-ready Retrieval-Augmented Generation (RAG) system that intelligently answers questions about Netflix movies using semantic search and local LLM inference.

Main Functionality
Semantic Search: 6,020 Netflix movies chunked into 7,655 documents and indexed in Chroma vector database
Context-Aware Answers: Uses HuggingFace embeddings + TinyLlama LLM to generate accurate, grounded responses
REST API: Flask endpoints for easy integration into applications
Zero API Costs: Runs entirely locally on CPU — no external API calls or subscription fees


Setup

```bash
pip install -r requirements.txt
python main.py
# API runs on http://localhost:5500/ask



Response example(aswer part only):
<img width="694" height="282" alt="image" src="https://github.com/user-attachments/assets/6e25f35f-a42c-4a8e-a73d-86943334c3a0" />


Localhost tested in termnal.
<img width="2680" height="114" alt="image" src="https://github.com/user-attachments/assets/a57a2d5e-c9b2-4627-90c9-a65fea95fb67" />
