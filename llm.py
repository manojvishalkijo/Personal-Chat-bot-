import ollama

def query_llm_with_context(query,context):
    system_content="""You are a helpful assistant for answering user queries based on provided context.
Use the context to provide accurate and relevant answers.
Do not make assumptions beyond the context provided.
If the context does not contain enough information to answer the query,
say that you cannot answer based on the given context."""
    
    response=ollama.chat(
        model="phi3:latest",
    messages=[{"role":"system","content":system_content},
    {"role":"user","content":f"Query: {query}\n\n Context:\n{context}"}
    ]
    )

    return response["message"]["content"]