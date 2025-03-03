import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RAG_SaaS.settings")

app = Celery("RAG_SaaS")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
