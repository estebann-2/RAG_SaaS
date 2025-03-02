from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Document, Query
from .forms import DocumentUploadForm, QueryForm, RegisterForm
import os
from .tasks import process_document

# Vista para registrar usuarios
def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Autenticación automática después del registro
            messages.success(request, "Registro exitoso. Bienvenido!")
            return redirect('document_list')
    else:
        form = RegisterForm()
    return render(request, 'rag_app/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Inicio de sesión exitoso.")
            return redirect('home')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'rag_app/login.html', {'form': form})

# Logout view
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, "Has cerrado sesión correctamente.")
        return redirect('login')


# Create your views here.

@login_required
def home(request):
    return render(request, 'rag_app/base.html')

@login_required
def upload_document(request):
    if request.method == "POST":
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)  # Don't save yet
            document.user = request.user  # Assign the logged-in user
            document.save()  # Now save
            process_document.delay(document.id)  # Process document asynchronously
            messages.success(request, "Documento subido exitosamente. Se procesará en segundo plano.")
            return redirect('document_list')  # Redirect to the document list
    else:
        form = DocumentUploadForm()
    
    return render(request, 'rag_app/upload.html', {'form': form})

@login_required
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'rag_app/document_list.html', {'documents': documents})

# Query Endpoint
@login_required
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
