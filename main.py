from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from QueryProcessor import process_query
import uvicorn

app = FastAPI(title="AI Power RAG Engine")

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str

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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
