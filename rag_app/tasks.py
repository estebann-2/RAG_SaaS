from celery import shared_task
import os
import fitz  # PyMuPDF para extraer texto de PDFs
from docx import Document as DocxDocument
from langchain.text_splitter import RecursiveCharacterTextSplitter
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import SimpleDirectoryReader, GPTVectorStoreIndex
import logging
logger = logging.getLogger(__name__)


from .models import Document

# @shared_task
# def process_document(document_id):
#     doc = Document.objects.get(id=document_id)
#     file_path = doc.file.path

#     # Extraer texto
#     text = extract_text(file_path)

#     # Dividir en chunks
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
#     chunks = text_splitter.split_text(text)

#     # Generar embeddings (requiere una API de OpenAI o un modelo local)
#     embedder = OpenAIEmbedding(model_name="text-embedding-ada-002")
#     embeddings = [embedder.get_text_embedding(chunk) for chunk in chunks]

#     # Guardar embeddings en FAISS
#     save_to_faiss(embeddings, document_id)

#     # Marcar como procesado
#     doc.processed = True
#     doc.save()

#     return f"Procesado documento {doc.title}"

@shared_task
def process_document(document_id):
    try:
        document = Document.objects.get(id=document_id)
        # Simulating document processing
        import time
        time.sleep(5)  # Simulate processing delay
        document.processed = True  # ✅ Mark as processed
        document.save()

        # 🔍 Confirm it's actually updated
        updated_doc = Document.objects.get(id=document_id)
        if updated_doc.processed:
            logger.info(f"✅ Document '{document.title}' marked as processed!")
        else:
            logger.error(f"❌ Document '{document.title}' not updated!")

    except Document.DoesNotExist:
        logger.error(f"⚠️ Document {document_id} does not exist.")

def extract_text(file_path):
    _, ext = os.path.splitext(file_path)
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    else:
        return ""

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(docx_path):
    doc = DocxDocument(docx_path)
    return "\n".join([p.text for p in doc.paragraphs])

def save_to_faiss(embeddings, document_id):
    import faiss
    import numpy as np
    index = faiss.IndexFlatL2(len(embeddings[0]))  # Crear índice FAISS
    index.add(np.array(embeddings))
    faiss.write_index(index, f"faiss_index_{document_id}.bin")
