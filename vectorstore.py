from pinecone import Pinecone
from dotenv import load_dotenv
import os
import uuid

load_dotenv()

_index = None

def get_pinecone_index():
    global _index
    if _index is None:
        api_key = os.getenv("PINECONE_API_KEY")
        index_name = os.getenv("PINECONE_INDEX_NAME")
        if not api_key:
            raise ValueError("PINECONE_API_KEY environment variable is not set.")
        if not index_name:
            raise ValueError("PINECONE_INDEX_NAME environment variable is not set.")
        client = Pinecone(api_key=api_key)
        _index = client.Index(index_name)
    return _index


def store_inpinecone(chunks,embedder,namespace=""):
         vect_list=[]
         for i in range(len(chunks)):
             chunk = chunks[i]
             embedding = embedder[i]

             vector_data = {
                 "id": f"chunk_{uuid.uuid4().hex}",
                 "values": embedding,
                 "metadata": {
                        "text": chunk,
                        "chunk_index": i
                              }
                        }

             vect_list.append(vector_data)

         index = get_pinecone_index()
         batch=100
         for i in range(0,len(vect_list),batch):
            batch_vectors=vect_list[i:i+batch]
            index.upsert(vectors=batch_vectors,namespace=namespace)


def search_in_pincone(query_vector,top_k=10,namespace=""):
         index = get_pinecone_index()
         results=index.query(
            vector=query_vector,
            top_k=top_k,
            include_metadata=True,
            namespace=namespace
            )
         match_chunks=[]
         for match in results.matches:
              match_chunks.append(match.metadata.get("text",""))
         
         return match_chunks



        
