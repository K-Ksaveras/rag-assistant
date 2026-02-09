"""
Flask API for Netflix RAG Assistant
Imports RAG pipeline from rag_pipeline.py.
"""

from flask import Flask, request, jsonify
from rag_pipeline import retriever, rag_chain

app = Flask(__name__)


def ask_question(query):
    """
    Get answer from RAG system given a question string.
    
    Returns: {"answer": "...", "sources": ["movie1", "movie2", "movie3"]}
    
    Why return a dict? Flask's jsonify() will convert it to JSON automatically.
    """
    # Step 1: Retrieve relevant documents (top-3 most similar)
    # Gives LLM context so answers are grounded in knowledge base.
    docs = retriever.invoke(query)
    
    # Step 2: Generate answer using RAG chain
    # Combines retrieved context + LLM to avoid hallucination.
    answer = rag_chain.invoke(query)
    
    # Step 3: Return both answer + source titles for transparency
    # User can verify answer came from real Netflix movies (audit trail).
    # Why metadata['title']? Each document carries metadata through pipeline for this purpose.
    return {
        "answer": answer,
        "sources": [doc.metadata['title'] for doc in docs]
    }


# 10c: Client sends data (question) to server, which processes and returns answer.

@app.route('/ask', methods=['POST'])
def ask_endpoint():
    """
    HTTP POST /ask - Answer a question about Netflix movies.
    
    Expected request body (JSON):
        {"question": "What action movies are available?"}
    
    Response (JSON):
        {"answer": "...", "sources": []}
    """
    # Step 1: Extract JSON from HTTP request body
    data = request.get_json()
    
    # Step 2: Get the question string from request payload
    # Safe access - returns None if 'question' key missing (avoid KeyError)
    question = data.get('question')
    
    # Step 3: Call helper function to get answer + sources
    result = ask_question(question)
    
    # Step 4: Return as JSON response
    # Converts Python dict to JSON + sets Content-Type: application/json header
    
    return jsonify(result)


# 10d: Define GET /health endpoint
@app.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint - used for monitoring
    Returns simple JSON status. Health check is read-only operation (no side effects, no data modification)
    """
    return jsonify({"status": "ok"})


if __name__ == '__main__':
    print("\n🚀 Flask API running on http://127.0.0.1:5500")
    print("   POST  /ask       - Answer a question about Netflix movies")
    print("   GET   /health    - Health check")
    app.run(debug=False, port=5500)
