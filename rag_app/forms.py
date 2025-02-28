from django import forms
from .models import Document, Query

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file', 'title']

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['question']
