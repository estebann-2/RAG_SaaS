from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    title = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    summary = models.TextField(blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)
    processed = models.BooleanField(default=False)  # ✅ New field to track processing status

    def __str__(self):
        return self.title


class Query(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='queries')
    question = models.TextField()
    answer = models.TextField(blank=True, null=True)
    queried_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query on {self.document.title}"
