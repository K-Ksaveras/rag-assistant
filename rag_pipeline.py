"""
RAG Pipeline Module
Initializes all components needed for the Netflix Q&A assistant
This module is imported by app.py to get access to retriever and rag_chain - Copilot Generated
"""

import pandas as pd
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain_community.llms import HuggingFacePipeline
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

print("⏳ Initializing RAG Pipeline...")

# ============================================================================
# STEP 1: Load embeddings (reuse existing vector store)
# ============================================================================
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"batch_size": 32, "normalize_embeddings": True}
)
print("✓ Embeddings model loaded")

# ============================================================================
# STEP 2: Load vector store (populated from notebook)
# ============================================================================
vectorstore = Chroma(
    persist_directory="./data/vectorstore",
    embedding_function=embeddings
)
print("✓ Vector store connected")

# ============================================================================
# STEP 3: Create retriever
# ============================================================================
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)
print("✓ Retriever initialized")

# ============================================================================
# STEP 4: Create prompt template
# ============================================================================
prompt_temp = PromptTemplate(
    input_variables=["context", "question"],
    template="""You are a Netflix movie expert. Answer ONLY questions about Netflix movies based on the context below.
If the question is not about Netflix movies, say you can only help with Netflix movie questions.
Be direct and concise.

Context: 
{context}

Question: {question}

Answer:
"""
)

# ============================================================================
# STEP 5: Format documents helper
# ============================================================================
def format_docs(docs):
    """Format Document objects into clean text for LLM"""
    return "\n\n---\n\n".join([doc.page_content for doc in docs])

# ============================================================================
# STEP 6: Create LLM
# ============================================================================
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 100,
        "temperature": 0.9,
        "top_p": 0.9,
        "do_sample": True
    }
)
print("✓ LLM model loaded")

# ============================================================================
# STEP 7: Create RAG chain (LCEL pipe syntax)
# ============================================================================
rag_chain = (
    {
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough(),
    }
    | prompt_temp
    | llm
    | StrOutputParser()
)
print("✓ RAG chain created")

print("\n✅ RAG Pipeline ready for API calls!")
