RAG System for Netflix Movies: Semantic Search, Embeddings & LangChain Pipeline
A production-ready Retrieval-Augmented Generation (RAG) system that intelligently answers questions about Netflix movies using semantic search and local LLM inference.

Main Functionality
Semantic Search: 6,020 Netflix movies chunked into 7,655 documents and indexed in Chroma vector database
Context-Aware Answers: Uses HuggingFace embeddings + TinyLlama LLM to generate accurate, grounded responses
REST API: Flask endpoints for easy integration into applications
Zero API Costs: Runs entirely locally on CPU — no external API calls or subscription fees



SETUP:

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
🚀 Flask API running on http://127.0.0.1:5500

Step 6: Test the API
curl -X POST http://localhost:5500/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What are some comedy movies?"}'


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
