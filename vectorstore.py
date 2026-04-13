from pinecone import Pinecone
from dotenv import load_dotenv
import os

load_dotenv()

pincone_client=Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index=pincone_client.Index(os.getenv("PINECONE_INDEX_NAME"))


def store_inpinecone(chunks,embedder,namespace=""):
         vect_list=[]
         for i in range(len(chunks)):
             chunk = chunks[i]
             embedding = embedder[i]

             vector_data = {
                 "id": f"chunk_{i}",
                 "values": embedding,
                 "metadata": {
                        "text": chunk,
                        "chunk_index": i
                              }
                        }

             vect_list.append(vector_data)

         batch=100
         for i in range(0,len(vect_list),batch):
            batch_vectors=vect_list[i:i+batch]
            index.upsert(vectors=batch_vectors,namespace=namespace)


def search_in_pincone(query_vector,top_k=10,namespace=""):
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



        
