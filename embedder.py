from dotenv import load_dotenv
import ollama
import os
import requests


Embed_Model="nomic-embed-text:latest"

def embed_chunks(chunks):
    embeddings_list = []
    for chunk in chunks:
        response = ollama.embeddings(
            model=Embed_Model,
            prompt=chunk
        )
        embeddings_list.append(response["embedding"])
    
    return embeddings_list


def embed_query(query):
    response=ollama.embeddings(
        prompt=query,
        model=Embed_Model
     )
    return response["embedding"]