"""
Flask API for Netflix RAG Assistant
Imports RAG pipeline from rag_pipeline.py.
"""

from flask import Flask, request, jsonify
from rag_pipeline import retriever, rag_chain

app = Flask(__name__)

# 10a: Define GET / endpoint for web interface
@app.route('/', methods=['GET'])
def home():
    """
    Simple web interface to interact with the RAG API
    """
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Netflix RAG Assistant</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; }
            input { width: 100%; padding: 10px; font-size: 16px; }
            button { padding: 10px 20px; font-size: 16px; background-color: #0066cc; color: white; border: none; cursor: pointer; }
            button:hover { background-color: #0052a3; }
            #response { margin-top: 20px; padding: 15px; background-color: #f0f0f0; border-radius: 5px; }
            .loading { color: gray; }
            .answer { margin-top: 10px; }
            .sources { margin-top: 10px; font-size: 14px; }
        </style>
    </head>
    <body>
        <h1>🎬 Netflix Movie Q&A</h1>
        <p>Ask questions about Netflix movies!</p>
        
        <input type="text" id="question" placeholder="E.g., What are some comedy movies?" />
        <button onclick="askQuestion()">Ask</button>
        
        <div id="response"></div>
        
        <script>
            function askQuestion() {
                const question = document.getElementById('question').value;
                const responseDiv = document.getElementById('response');
                
                if (!question.trim()) {
                    responseDiv.innerHTML = '<p style="color: red;">Please enter a question</p>';
                    return;
                }
                
                responseDiv.innerHTML = '<p class="loading">Loading...</p>';
                
                fetch('/ask', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({question: question})
                })
                .then(r => r.json())
                .then(data => {
                    let html = '<div class="answer"><strong>Answer:</strong><p>' + data.answer + '</p></div>';
                    if (data.sources && data.sources.length > 0) {
                        html += '<div class="sources"><strong>Sources:</strong><ul>';
                        data.sources.forEach(s => html += '<li>' + s + '</li>');
                        html += '</ul></div>';
                    }
                    responseDiv.innerHTML = html;
                })
                .catch(e => {
                    responseDiv.innerHTML = '<p style="color: red;">Error: ' + e.message + '</p>';
                });
            }
            
            // Allow Enter key to submit
            document.getElementById('question').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') askQuestion();
            });
        </script>
    </body>
    </html>
    '''

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
