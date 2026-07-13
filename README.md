<<<<<<< HEAD
# 🔮 AI Power RAG Engine - Personalized Chat Bot

A premium, glassmorphic Retrieval-Augmented Generation (RAG) chatbot designed to provide intelligent answers based on your own specialized documents.

## 🚀 Problem Statement

In the era of massive information, standard Large Language Models (LLMs) often suffer from two major limitations:
1. **Knowledge Cutoff**: They cannot access information updated after their training.
2. **Context Blindness**: They lack access to private or highly specialized documents (e.g., internal company reports, personal PDFs, or niche technical manuals).

Users are often forced to manually search through hundreds of pages of documentation, leading to inefficiency and missed insights.

## ✨ Solution: The RAG Advantage

This project implements a **Retrieval-Augmented Generation (RAG)** architecture to bridge the gap between static LLMs and dynamic, private data. Instead of retraining a model, we provide the LLM with relevant context retrieved from your own documents in real-time.

### How it Works:
1. **Document Ingestion**: Extracting text from PDFs using a custom parser.
2. **Intelligent Chunking**: Breaking down long documents into semantically coherent segments.
3. **Vector Embeddings**: Converting text segments into high-dimensional vectors.
4. **Pinecone Integration**: Storing vectors in a high-performance vector database for lightning-fast similarity search.
5. **Contextual Retrieval**: For every user query, the system retrieves only the most relevant document chunks.
6. **Smart Generation**: An LLM synthesizes an accurate, context-aware response based on the retrieved data.

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Premium Glassmorphic UI)
- **Backend**: FastAPI (High-performance API)
- **LLM/Embeddings**: Google Gemini API (gemini-1.5-flash & text-embedding-004)
- **Vector Database**: Pinecone
- **Processing**: Python (PyPDF, Requests, Uvicorn)

## 📁 Project Structure

- `app.py`: Streamlit frontend with a floating "Orb" design.
- `main.py`: FastAPI server handling query endpoints.
- `QueryProcessor.py`: The core RAG logic (Embed -> Search -> Generate).
- `vectorstore.py`: Pinecone integration for vector storage and search.
- `embedder.py`: logic for generating text embeddings using Google Gemini API.
- `pdfreader.py`: PDF text extraction utility.
- `chunker.py`: Text chunking algorithms.
- `llm.py`: Logic for querying the Gemini model via Google Gemini API.

## 🎨 UI Preview

The application features a modern, "AI Hub" design with:
- **Radial gradients** and **glassmorphism** effects.
- **Floating animation** for the central AI orb.
- **Typing effects** for a natural chat experience.
- **Responsive sidebar** for chat management and settings.

---
*Built with ❤️ for intelligent document interaction.*
=======
# 🚀 Smart Knowledge Assistant: Privacy-First RAG System

A high-performance **Retrieval-Augmented Generation (RAG)** system built for privacy and scalability. This project allows you to chat with your PDF documents with enterprise-grade accuracy, utilizing local embeddings for data privacy and Pinecone for lightning-fast semantic retrieval.

---

## ✨ Features

- **Privacy-First Embeddings:** Uses `nomic-embed-text` via **Ollama** to process data locally.
- **Scalable Vector Storage:** Integrated with **Pinecone** for high-dimensional vector search.
- **Intelligent Chunking:** Implements a sliding window semantic splitter (900 chars with 150-char overlap) to maintain contextual coherence.
- **PDF Intelligence:** automated text extraction and processing from PDF files.
- **Glassmorphic UI:** A premium, modern interface for seamless interaction.

---

## 🛠️ Tech Stack

- **Logic:** Python 3.x
- **Embeddings:** [Ollama](https://ollama.com/) (Local)
- **Vector Database:** [Pinecone](https://www.pinecone.io/) (Cloud)
- **Frontend:** Streamlit / FastAPI
- **Parsing:** PyPDF2 / Layout Analysis

---

![rag_workflow_infographic_1776065513435](https://github.com/user-attachments/assets/a765e4e3-9d24-42a3-a408-5890e4a3710c)


## 🚀 Getting Started

### 1. Prerequisites
- Install [Ollama](https://ollama.com/) and pull the Nomic model:
  ```bash
  ollama pull nomic-embed-text
  ```
- Sign up for a free [Pinecone](https://www.pinecone.io/) account and get your API key.

### 2. Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/your-username/smart-rag-assistant.git
cd smart-rag-assistant
pip install -r requirements.txt
```

### 3. Environment Setup
Create a `.env` file in the root directory:
```env
PINECONE_API_KEY=your_api_key
PINECONE_INDEX_NAME=your_index_name
```

### 4. Run the Application
```bash
streamlit run app.py
```

---

## 🧠 How it Works

1. **Ingestion:** Upload a PDF. The system extracts text and splits it into semantic chunks.
2. **Embedding:** Each chunk is converted into a vector representation locally using Ollama.
3. **Indexing:** Vectors are stored in a Pinecone index for retrieval.
4. **Querying:** When you ask a question, the system finds the most relevant chunks and passes them to the LLM as context.

---

## 📂 Project Structure

- `app.py` - Main Streamlit UI
- `chunker.py` - Semantic splitting logic
- `embedder.py` - Ollama integration
- `vectorstore.py` - Pinecone operations
- `pdfreader.py` - PDF extraction logic

---

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License
Distributed under the MIT License.
>>>>>>> 9c3e8c00ec81876c11e27b61c6f18bb2fce1459f
