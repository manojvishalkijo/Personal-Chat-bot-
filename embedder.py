from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
import google.generativeai as genai
import os

load_dotenv()

# Configure the Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

Embed_Model="models/embedding-001"

def embed_chunks(chunks):
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set. Please set it in your environment or .env file.")
        
    embeddings_list = []
    # Batch embeddings into chunks of 100 to reduce API calls and avoid Rate Limits
    batch_size = 100
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i+batch_size]
        response = genai.embed_content(
            model=Embed_Model,
            content=batch
        )
        embeddings_list.extend(response["embedding"])
    
    return embeddings_list


def embed_query(query):
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set. Please set it in your environment or .env file.")
        
    response = genai.embed_content(
        model=Embed_Model,
        content=query
     )
    return response["embedding"]