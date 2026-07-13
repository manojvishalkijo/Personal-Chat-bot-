from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from QueryProcessor import process_query
import uvicorn
import os
import io
from dotenv import load_dotenv
from pdfreader import read_pdf
from chunker import chunk_page
from embedder import embed_chunks
from vectorstore import store_inpinecone

load_dotenv()

app = FastAPI(title="AI Power RAG Engine")

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str

@app.get("/")
async def root():
    return {"status": "online", "message": "FastAPI RAG Backend is running"}

@app.get("/health")
async def health():
    return {"status": "online"}

@app.post("/query", response_model=QueryResponse)
async def query_endpoint(request: QueryRequest):
    try:
        answer = process_query(request.query)
        return QueryResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        # Read the file content
        contents = await file.read()
        pdf_stream = io.BytesIO(contents)
        
        # Read PDF pages
        pages = read_pdf(pdf_stream)
        if not pages:
            raise HTTPException(status_code=400, detail="The uploaded PDF file is empty or could not be parsed.")
            
        # Chunk pages
        chunks = chunk_page(pages)
        if not chunks:
            raise HTTPException(status_code=400, detail="No text chunks could be extracted from the PDF.")
            
        # Embed chunks
        embedded_chunks = embed_chunks(chunks)
        
        # Store in Pinecone
        store_inpinecone(chunks, embedded_chunks)
        
        return {"status": "success", "message": f"Successfully indexed {len(chunks)} chunks from {file.filename}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
