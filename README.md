

# **StudyBudd API – REST Framework Integration**

This branch introduces RESTful API support for the **StudyBudd** project using **Django REST Framework (DRF)**. It includes API endpoints for Rooms and related models, enabling seamless integration with frontend apps or third-party services.

---

## API Demo

> Access individual room details:
> **[`http://127.0.0.1:8000/api/rooms/1/`](http://127.0.0.1:8000/api/rooms/1/)**
> *(Make sure the server is running locally)*

---

## Branch: `feature/rest-api`

This branch contains the following major additions:

* ✅ Django REST Framework installation and configuration
* ✅ API views using DRF (`APIView`, `GenericAPIView`, `ModelViewSet`)
* ✅ URL routing for API endpoints
* ✅ Serializers for Room and related models

---

## Tech Stack

* **Python 3.12**
* **Django 5+**
* **Django REST Framework 3.16**
* SQLite (default) or switchable to PostgreSQL/MySQL

---

##  Setup Instructions

1. **Clone the repo & switch to API branch**

   ```bash
   git clone https://github.com/NayabMalik1/studybudd.git
   cd studybudd
   git checkout -b feature/rest-api
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv env
   .\env\Scripts\activate      # For Windows
   source env/bin/activate     # For Linux/macOS
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` doesn't exist yet, manually install:

   ```bash
   pip install django djangorestframework
   ```

4. **Add to `INSTALLED_APPS` in `settings.py`**

   ```python
   'rest_framework',
   ```

5. **Run migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start development server**

   ```bash
   python manage.py runserver
   ```

7. **Access the API**
   Open in browser:
   [http://127.0.0.1:8000/api/rooms/1/](http://127.0.0.1:8000/api/rooms/1/)

---

##  Project Structure (API-related)


studybudd/
├── api/
│   ├── serializers.py      # DRF Serializers
│   ├── views.py            # API Views (Class-based)
│   └── urls.py             # API URLs
├── studybudd/
│   └── settings.py         # Add 'rest_framework' to INSTALLED_APPS
```
