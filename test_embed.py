from embedder import embed_query
import os

try:
    vector = embed_query("test query")
    print(f"Vector type: {type(vector)}")
    print(f"Vector length: {len(vector) if vector else 'None'}")
    print(f"Vector first 5: {vector[:5] if vector else 'None'}")
except Exception as e:
    print(f"Error: {e}")
