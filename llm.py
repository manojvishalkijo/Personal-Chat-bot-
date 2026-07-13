# pyrefly: ignore [missing-import]
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure the Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def query_llm_with_context(query,context):
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set. Please set it in your environment or .env file.")

    system_content="""You are a helpful assistant for answering user queries based on provided context.
Use the context to provide accurate and relevant answers.
Do not make assumptions beyond the context provided.
If the context does not contain enough information to answer the query,
say that you cannot answer based on the given context."""
    
    model = genai.GenerativeModel(
        model_name="gemini-3.5-flash",
        system_instruction=system_content
    )
    
    prompt = f"Query: {query}\n\n Context:\n{context}"
    
    response = model.generate_content(prompt)
    return response.text