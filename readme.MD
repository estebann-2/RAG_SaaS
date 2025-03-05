# RAG_SaaS: A Django-based Retrieval-Augmented Generation (RAG) System

## Introduction
**RAG_SaaS** is a **Django-based Retrieval-Augmented Generation (RAG) system** that allows users to **upload documents and query them** using an **LLM-powered AI assistant**. The system extracts, processes, and stores text from uploaded files, enabling **intelligent document-based queries**.

---

### Instructions to run on your own device:

Reach this URL: http://23.22.249.53:8000/

-Use the following credentials:

-User: ubuntu

-Password: ubuntu

Thank you very much!

---

## Tech Stack

- **Backend**: Django 4.2.10
- **Database**: MySQL
- **Task Queue**: Celery with Redis broker
- **AI/ML**: 
  - OpenAI Embeddings (text-embedding-3-small)
  - GPT-4 for text generation
- **File Processing**: 
  - PyMuPDF for PDF processing
  - python-docx for Word documents
  - Custom text processing utilities

---

## Prerequisites

- Python 3.11+
- MySQL 8.0+
- Redis Server
- OpenAI API key


---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/estebann-2/RAG_SaaS.git
cd RAG_SaaS
```

### 2️⃣ Create a Virtual Environment & Install Dependencies

```bash
conda create -n rag_saas python=3.12.7
conda activate rag_saas
pip install -r requirements.txt
```

### 3️⃣ Apply Migrations & Create Superuser

```python
python manage.py migrate
python manage.py createsuperuser  # Follow the prompt to set up an admin user
```

### 4️⃣ Run the Development Server
```python
python manage.py runserver
```

Now, open your browser and go to:
http://127.0.0.1:8000/

---

## 🚀 Running with Docker
To deploy the app using Docker, run:

```bash
docker-compose up --build
````
