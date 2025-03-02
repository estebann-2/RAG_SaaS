from django.urls import path
from .views import register_user, login_view, logout_view, home, upload_document, document_list, query_document


urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home, name='home'),  # Homepage
    path('upload/', upload_document, name='upload_document'),
    path('documents/', document_list, name='document_list'),
    path('query/<int:document_id>/', query_document, name='query_document'),
]
