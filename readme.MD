# RAG_SaaS: A Django-based Retrieval-Augmented Generation (RAG) System

## Introduction
**RAG_SaaS** is a **Django-based Retrieval-Augmented Generation (RAG) system** that allows users to **upload documents and query them** using an **LLM-powered AI assistant**. The system extracts, processes, and stores text from uploaded files, enabling **intelligent document-based queries**.

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
git clone https://github.com/yourusername/RAG_SaaS.git
cd RAG_SaaS
```

### 2️⃣ Create a Virtual Environment & Install Dependencies

```python
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
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

## ⚡ Core Functionality

### 🔹 Document Upload & Processing
- Users upload a document (**PDF, DOCX, TXT, or Markdown**).
- The text is extracted and **chunked** into smaller segments.
- Each chunk is **embedded** using **OpenAI’s text-embedding-ada-002** or **FAISS**.
- The embeddings are stored in a **FAISS vector database** for retrieval.

### 🔹 Query Processing
- Users enter **natural language questions** related to uploaded documents.
- The system **retrieves relevant chunks** using **vector similarity search**.
- The retrieved context is **fed into an LLM** (e.g., OpenAI GPT, LlamaIndex) to generate answers.

### 🔹 API Endpoints (Django REST Framework)
| **Endpoint**            | **Method** | **Description**            |
|-------------------------|------------|----------------------------|
| `/api/upload/`         | `POST`     | Upload a document          |
| `/api/documents/`      | `GET`      | List uploaded documents    |
| `/api/query/<doc_id>/` | `POST`     | Query a document           |

---

## 🚀 Running with Docker
To deploy the app using Docker, run:

```bash
docker-compose up --build
````
