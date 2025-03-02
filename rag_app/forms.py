from django import forms
from .models import Document, Query
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file', 'title']

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['question']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
