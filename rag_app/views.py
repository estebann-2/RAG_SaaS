from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Document, Query
from .forms import DocumentUploadForm, QueryForm
import os

# Create your views here.

def home(request):
    return render(request, 'rag_app/base.html')


# Upload Document Endpoint
def upload_document(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('rag_app:document_list')
    else:
        form = DocumentUploadForm()
    return render(request, 'rag_app/upload.html', {'form': form})

# List Uploaded Documents
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'rag_app/document_list.html', {'documents': documents})

# Query Endpoint
def query_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            query = form.save(commit=False)
            query.document = document
            
            # TODO: Add RAG system logic here
            # Example: query.answer = call_rag_system(query.question, document.file.path)
            query.answer = "This is a placeholder response."
            query.save()
            return JsonResponse({'question': query.question, 'answer': query.answer})
    else:
        form = QueryForm()
    return render(request, 'rag_app/query.html', {'form': form, 'document': document})
