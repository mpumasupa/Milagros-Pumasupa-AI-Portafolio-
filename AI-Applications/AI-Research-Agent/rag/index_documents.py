import os
from pathlib import Path
from PyPDF2 import PdfReader
import docx
from vector_store.vector_store import VectorStore
from rag.openai_embed import embed_openai  # Puedes reemplazar por función local si no hay API

def extract_paragraphs_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    paragraphs = []
    for page in reader.pages:
        text = page.extract_text()
        for para in text.split('\n\n'):
            para = para.strip()
            if len(para) > 20:
                paragraphs.append(para)
    return paragraphs

def extract_paragraphs_from_docx(docx_path):
    doc = docx.Document(docx_path)
    paragraphs = [p.text.strip() for p in doc.paragraphs if len(p.text.strip()) > 20]
    return paragraphs

def index_documents(doc_folder="rag/docs", store_path="rag/store", embed_fn=embed_openai):
    store = VectorStore(path=store_path)

    for file in Path(doc_folder).glob("*"):
        if file.suffix.lower() == ".pdf":
            paragraphs = extract_paragraphs_from_pdf(file)
        elif file.suffix.lower() == ".docx":
            paragraphs = extract_paragraphs_from_docx(file)
        else:
            continue

        for para in paragraphs:
            vec = embed_fn(para)
            store.add(vec, para)

    store.save()
    print(f"Indexed documents in {doc_folder} to store at {store_path}")
