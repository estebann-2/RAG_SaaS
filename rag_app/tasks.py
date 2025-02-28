from celery import shared_task
from .models import Document, Query
from .services.llm_processor import LLMProcessor

llm = LLMProcessor()

@shared_task
def generate_summary(document_id):
    document = Document.objects.get(id=document_id)
    document.summary = llm.summarize(document.file.read())
    document.save()

@shared_task
def process_query(query_id):
    query = Query.objects.get(id=query_id)
    document = query.document
    query.answer = llm.query(query.question, document.summary or document.file.read())
    query.save()
