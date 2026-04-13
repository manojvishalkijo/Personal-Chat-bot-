from embedder import embed_query
from vectorstore import search_in_pincone
from llm import query_llm_with_context

def process_query(query):
    if not query.strip():
        return "Please enter a valid query."
        
    # Create a vector representation of the user query
    query_vector = embed_query(query)
    
    # Generate top matching chunks
    chunk_list = search_in_pincone(query_vector)
    
    # Join chunks into a single context string for better LLM processing
    context = "\n\n".join(chunk_list)
    
    # Load context and query to the LLM
    response = query_llm_with_context(query, context)
    return response

if __name__=="__main__":
    query=input("Enter:")
    response=process_query(query)
    print(response)
