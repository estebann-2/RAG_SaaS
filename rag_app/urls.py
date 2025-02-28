from django.urls import path
from . import views

app_name = 'rag_app'

urlpatterns = [
    path('', views.home, name='home'),  # Default homepage
    path('upload/', views.upload_document, name='upload_document'),
    path('documents/', views.document_list, name='document_list'),
    path('query/<int:document_id>/', views.query_document, name='query_document'),
]
