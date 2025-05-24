# Django Form Miniproject

![Python Version](https://img.shields.io/badge/python-3.x-blue)
![Django Version](https://img.shields.io/badge/django-5.2.1-green)

A Django web application demonstrating a basic form-submission workflow, with:

- A **Home** page  
- A **Form** page (with server-side validation)  
- A **Success** confirmation page  

---

## 🎯 Features

- ✅ Home page with project overview  
- ✅ User input form (name, email, message)  
- ✅ Built-in Django validation (required fields, email format)  
- ✅ Success page with confirmation message  

---

## 🛠 Tech Stack

- **Backend:** Django 5.2.1  
- **Language:** Python 3.x  
- **Frontend:** HTML5, CSS3  

---

## ⚙️ Prerequisites

Make sure you have **Python 3.x** installed. You’ll also need **pipenv** (or you can swap in your preferred virtual-env tool).

## 🚀 Setup & Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/shravani-05/Django-Forms.git
   cd Django-Forms
2. **Create & activate virtual environment**
   ```bash
   pipenv install        
   pipenv shell
3. **Install dependencies**
   ```bash
   pipenv install django
4. **Run the development server**
   ```bash
   python manage.py runserver
5. **Open your browser and go to:**
   ```bash
   http://127.0.0.1:8000/

##📁 Project Structure

```bash
DJANGO-FORM/
├── form/                   # project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── formapp/                # your Django app
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── venv/                   # virtual environment
├── .gitignore
├── manage.py
└── README.md

