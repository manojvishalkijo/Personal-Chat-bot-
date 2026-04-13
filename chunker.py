from typing import List,Tuple
def chunk_page(pages,chunk_size=900,chunk_overlap=150):
    
    #Create the list for storing the chunks
    chunks=[]
    
    merge_text=" ".join(pages)
    page_text=len(merge_text)

    if page_text==0:
        return chunks
    
    start=0
    while start<page_text:
      end=min(start+chunk_size,page_text)
      chunk=merge_text[start:end].strip()
      chunks.append(chunk)
      
      if end>=page_text:
        break
      start = end - chunk_overlap
    
    return chunks

      
