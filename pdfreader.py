import os
from pypdf import PdfReader
from chunker import chunk_page

def read_pdf(pdf_file):
    if isinstance(pdf_file, str):
        if not os.path.exists(pdf_file):
            raise FileNotFoundError(f"file not found in {pdf_file}")
        render = PdfReader(pdf_file)
    else:
        render = PdfReader(pdf_file)
    
    pages = []
    for page in render.pages:
        text = page.extract_text()
        if text:
            pages.append(text)
    return pages

