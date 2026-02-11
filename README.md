🎬 RAG Assistant – Netflix Movies Q&A

A production-ready Retrieval-Augmented Generation (RAG) system that answers questions about Netflix movies using semantic search and local LLM inference.

Built to demonstrate: Embeddings, Vector databases, LangChain LCEL pipelines, Local LLM integration and REST API deployment.


🚀 What This Project Does

This project implements a fully local Retrieval-Augmented Generation (RAG) system that answers questions about Netflix movies using semantic search and LLM inference. It ingests 6,020 movie records, splits them into 7,655 semantic chunks, generates embeddings with all-MiniLM-L6-v2, and stores them in a persistent Chroma vector database for efficient similarity search. When a user submits a query, the system retrieves the most relevant context and generates grounded responses using TinyLlama, all exposed through a Flask REST API. The entire pipeline runs locally on CPU with zero external API costs.


📂 Project Structure

rag-assistant/
→ rag_assistant.ipynb (build vector store)
→ rag_pipeline.py (RAG logic)
→ app.py (Flask API)
→ data/documents.csv (Netflix dataset)
→ data/vectorstore/ (Chroma persistence)
→ README.md


⚙️ SETUP:

Clone the Repository:
git clone https://github.com/K-Ksaveras/rag-assistant.git
cd rag-assistant

Virtual Environment:
python3 -m venv .venv
source .venv/bin/activate

Install Dependencies:
pip install -r requirements.txt

Build the Vector Store (One-time setup):
jupyter notebook rag_assistant.ipynb

Start the API:
python app.py
Flask API running on http://127.0.0.1:5500

Step 6: Test the API
curl -X POST http://localhost:5500/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What are some comedy movies?"}'


OUTPUT EXAMPLES:

Response example(aswer part only):

Question: What documentaries are available on Nefflix?

Answer:
1. "A Girl in the River: The Price of Forgiveness"
2. "Hillbilly Elegy"
3. "The Disappearance of Chantal"
4. "Eerie Encounters"
5. "The Vanishing of Sidney Hall"
6. "The Staircase"
7. "Manson: Culture of Madness"
8. "The Case of: Momoa"
9. "The Silence of the Lambs"
10. "The Night of"
11. "Moonlight"
12. "City So Real"


Localhost tested in termnal:

.. rag-assistant % curl -X POST http://localhost:5500/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What are some comedy movies?"}'
{"answer":"You are a Netflix movie expert. Answer ONLY questions about Netflix movies based on the context below.\nIf the question is not about Netflix movies, say you can only help with Netflix movie questions.\nBe direct and concise.\n\nContext: \nIn six live installments, John Mulaney explores Los Angeles during a week when pretty much every single funny person is in town. Genre: Comedy, Talk-Show Type: tv Release Year: 2024 Director: Unknown Actors: John Mulaney, Richard Kind John Mulaney Richard Kind IMDB Rating: 7.1 Available in 130 countries\n\n---\n\nIn six live installments, John Mulaney explores Los Angeles during a week when pretty much every single funny person is in town. Genre: Comedy, Talk-Show Type: tv Release Year: 2024 Director: Unknown Actors: John Mulaney, Richard Kind John Mulaney Richard Kind IMDB Rating: 7.1 Available in 130 countries\n\n---\n\nJack Whitehall and his father embark on a globe-trotting trip to find answers to the big questions facing the comedian after becoming a dad. Genre: Comedy, Documentary Type: tv Release Year: 2024 Director: Unknown Actors: Jack Whitehall, Michael Whitehall Jack Whitehall Michael Whitehall IMDB Rating: 6.7 Available in 129 countries\n\nQuestion: What are some comedy movies?\n\nAnswer:\n1. Ghostbusters (1984)\n2. The Jerk (1979)\n3. Porky's (1982)\n4. Anchorman: The Legend of Ron Burgundy (2004)\n5. Shaun of the Dead (2004)\n6. The Hangover (2009)\n7. Forgetting Sarah Marshall (2008","sources":["John Mulaney Presents: Everybody's in LA John Mulaney Presents Everybodys in LA","John Mulaney Presents: Everybody's in LA John Mulaney Presents Everybodys in LA","Jack Whitehall: Fatherhood with My Father Jack Whitehall Fatherhood with My Father"]}


🧩 Key Engineering Decisions

Chunk size 500 + overlap 50 → balances recall & precision

Persistent Chroma store → avoids re-embedding

LCEL pipeline syntax → modern LangChain design

Local LLM → zero API cost & privacy-safe

Separation of concerns → notebook for data, Python modules for production



🔄 Where This Architecture Can Be Reused

The same RAG system structure can be adapted for:

🏦 Internal Knowledge Assistants
Answering questions over HR policies, compliance documents, or internal banking procedures.

📚 Educational Q&A Systems
Retrieval-based tutoring systems grounded in textbooks or course materials.

🏢 Company Documentation Search
Semantic search over technical docs, onboarding guides, or support manuals.

🛍 E-Commerce Product Assistants
Answering product questions using structured catalog data.

⚖️ Legal / Regulatory Search
Querying contracts, policies, or regulatory documents with contextual grounding.

🧾 Customer Support Automation
Combining retrieval with LLM generation to provide accurate, source-backed answers
