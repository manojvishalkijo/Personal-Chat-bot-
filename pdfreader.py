import os
from pypdf import PdfReader
from chunker import chunk_page

def read_pdf(pdf_path):
    if not os.path.exists(pdf_path ):
        raise FileNotFoundError(f"file not found in {pdf_path}")
    
    render=PdfReader(pdf_path)
    pages=[]
    for page in render.pages:
        pages.append(page.extract_text())
    return pages

