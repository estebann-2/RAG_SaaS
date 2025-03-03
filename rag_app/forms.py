from django import forms
from .models import Document, Message
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import os

# ✅ Document Upload Form with Better Validation
class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file', 'title']

    def clean_file(self):
        file = self.cleaned_data.get('file', False)

        if not file:
            raise ValidationError("Debes subir un archivo.")

        # ✅ Use model's validation function
        from .models import validate_file_extension
        validate_file_extension(file)

        # ✅ Validate file size (10MB limit)
        max_size = 10 * 1024 * 1024  # 10MB
        if file.size > max_size:
            raise ValidationError("El archivo es demasiado grande. Máximo 10MB.")

        return file

# ✅ User Registration Form with Email Validation
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get("email").lower()

        # ✅ Ensure unique email
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este email ya está registrado. Usa otro.")

        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"].lower()  # Normalize email case
        if commit:
            user.save()
        return user

# ✅ Message Form with Trimmed Text
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["text"]
        widgets = {
            "text": forms.TextInput(attrs={
                "placeholder": "Escribe un mensaje...",
                "maxlength": "500",  # Prevent excessively long messages
                "autocomplete": "off",
            }),
        }

    def clean_text(self):
        text = self.cleaned_data.get("text", "").strip()
        if not text:
            raise ValidationError("El mensaje no puede estar vacío.")
        return text
