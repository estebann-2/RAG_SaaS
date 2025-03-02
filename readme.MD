# 🚀 RAG_SaaS: A Django-based Retrieval-Augmented Generation (RAG) System

## 📖 Introduction
**RAG_SaaS** is a **Django-based Retrieval-Augmented Generation (RAG) system** that allows users to **upload documents and query them** using an **LLM-powered AI assistant**. The system extracts, processes, and stores text from uploaded files, enabling **intelligent document-based queries**.

This project integrates **Django, Celery, FAISS, and LLMs** (such as OpenAI, LlamaIndex, or LangChain) to provide a scalable, efficient, and user-friendly document management and retrieval system.

---

## 🚀 Features
✅ **User Authentication** – Secure login and user session management.  
✅ **Document Upload** – Supports **PDF, DOCX, TXT, and Markdown** files.  
✅ **Text Processing & Chunking** – Uses **LLM-based text splitters** to break documents into manageable chunks.  
✅ **Embedding Generation** – Computes document embeddings using **FAISS or OpenAI embeddings**.  
✅ **Query-Based Retrieval** – Users can ask **natural language queries** about uploaded documents.  
✅ **Asynchronous Processing** – Uses **Celery** to process document uploads and embedding generation.  
✅ **API Support** – RESTful API using **Django REST Framework (DRF)**.  
✅ **Scalability** – Deployed using **Docker & AWS** for cloud-based usage.  

---

## 📂 Project Structure

```
RAG_SaaS/                        # Root Django Project
│
├── manage.py                     # Django's management script
├── requirements.txt               # Dependencies file
│
├── RAG_SaaS/                      # Django Project Configuration
│   ├── __init__.py                # Marks as a Python module
│   ├── settings.py                 # Main settings (Database, API keys, etc.)
│   ├── urls.py                     # Main project URL routing
│   ├── wsgi.py                     # WSGI config for deployment
│   ├── asgi.py                     # ASGI config (for WebSockets if needed)
│
└── rag_app/                        # Main Django App for RAG system
    ├── __init__.py                 # Marks as a Python module
    ├── admin.py                    # Admin panel configurations
    ├── apps.py                      # App configuration
    ├── models.py                    # Database models (Documents, Queries, Users)
    ├── forms.py                     # Django forms for uploads & queries
    ├── views.py                     # Handles user requests & query processing
    ├── serializers.py               # API Serializers (DRF)
    ├── urls.py                      # App-specific URL routing
    ├── tasks.py                     # Celery async task queue
    │
    ├── services/                    # NLP & AI integration
    │   ├── llm_processor.py         # LLM-powered query processing
    │   ├── text_summarizer.py       # Summarization logic
    │
    ├── templates/                   # HTML templates for frontend
    │   └── rag_app/
    │       ├── base.html            # Main template
    │       ├── login.html           # User login page
    │       ├── upload.html          # Upload document page
    │       ├── document_list.html   # List uploaded documents
    │       ├── query.html           # Query documents
    │
    ├── static/                      # Static files (CSS, JS, Images)
    │   └── rag_app/
    │       ├── css/
    │       ├── js/
    │       ├── images/
    │
    ├── migrations/                   # Django migrations for database changes
    │   ├── __init__.py               # Marks as a Python module
    │
    ├── tests/                        # Automated tests for the app
    │   ├── __init__.py               # Marks as a Python module
    │   ├── test_views.py             # Tests for views
    │   ├── test_models.py            # Tests for models
    │   ├── test_api.py               # Tests for API endpoints
    │
    ├── utils/                        # Helper functions & utility scripts
    │   ├── file_processing.py        # Handles file processing (PDF, DOCX, etc.)
    │   ├── embedding_utils.py        # Manages vector embeddings
    │
    ├── api/                          # API functionality for external access
    │   ├── __init__.py
    │   ├── views.py                  # API views
    │   ├── urls.py                   # API URL configuration
    │   ├── serializers.py            # Serializers for API
    │
    ├── faiss_indexes/                # Folder to store FAISS indexes for retrieval
    │   ├── index.bin                 # Example FAISS index file
    │
    ├── logs/                         # Folder for log files
    │   ├── django.log                # Main log file
    │   ├── celery.log                 # Celery logs
    │
    ├── docker/                        # Docker configurations
    │   ├── Dockerfile                 # Dockerfile for building the project
    │   ├── docker-compose.yml         # Docker Compose setup
    │
    ├── scripts/                       # Useful scripts for automation
    │   ├── setup_db.sh                # Script to set up the database
    │   ├── run_celery.sh              # Script to run Celery workers
```

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

This will:

- Set up **Django, PostgreSQL, Redis, and Celery workers**.
- Expose the application on **port 8000**.

---

## 🧠 Future Improvements
✅ **Add LangChain & OpenAI integration** for smarter responses.  
✅ **Implement User Role Management** (Admin, Regular Users).  
✅ **Improve Frontend UI with React/Vue**.  
✅ **Optimize FAISS Search for Large Document Sets**.  

---

## 👨‍💻 Contributing
Feel free to **fork this repo**, submit PRs, and suggest improvements. 🚀

---

## 📄 License
This project is licensed under **MIT License**.

---

## 📩 Contact
📧 **Email:** your.email@example.com  
🐙 **GitHub:** [yourusername](https://github.com/yourusername)  

---

### ✅ Now, You Can Continue Configuration Using an LLM!
This README provides a structured introduction so an **LLM (like ChatGPT, Claude, or Copilot)** can:
- **Understand your app’s architecture.**
- **Help configure missing components (Celery, FAISS, LLMs).**
- **Generate additional code for features like authentication, API integration, and query processing.**
