I have to create a django app, which is a RAG system, which have an  interface for user request, so user upload a document and can query about it, help me structure the django project


django-admin startproject RAG_SaaS
cd django_rag_project
python manage.py startapp rag_app



RAG_SaaS/
│
├── manage.py
├── RAG_SaaS/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── rag_app/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── serializers.py      # For Django REST Framework
    ├── urls.py
    ├── tasks.py            # For Celery asynchronous processing
    ├── services/            # NLP & AI Integration Logic
    │   ├── llm_processor.py
    │   └── text_summarizer.py
    ├── templates/
    │   └── rag_app/
    │       ├── base.html
    │       ├── upload.html
    │       ├── document_list.html
    │       └── query.html
    └── static/
        └── rag_app/
            └── css/
            └── js/



