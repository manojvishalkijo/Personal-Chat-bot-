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
