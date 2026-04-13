from pdfreader import read_pdf 
from chunker import chunk_page
from embedder import embed_chunks
from vectorstore import store_inpinecone
from typing import List

pdf_path='./resources/sample_rag_5_pages.pdf'

pages=read_pdf(pdf_path)

print(f"Extracted {len(pages)} pages from the PDF")
print("First page content:")
print(pages[0] if pages else "Nothing extracted")

chunks=chunk_page(pages,chunk_size=900,chunk_overlap=150)
print(f"Total chunks: {len(chunks)}")
print(chunks[0])

embeded_chunks=embed_chunks(chunks)
print(f"Total embedded chunks: {len(embeded_chunks)}")
print(embeded_chunks[0])

store_inpinecone(chunks, embeded_chunks, namespace="")