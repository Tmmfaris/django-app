# EduZ Academic Suite – Academic Management System

EduZ Academic Suite is a **web-based academic management platform** designed to manage students, teachers, subjects, attendance, and marks in a centralized system.

The application is built using **Django, SQLite, HTML, CSS, and Bootstrap**, providing a scalable foundation for educational data management and future analytics integration.

This project demonstrates practical skills in:

- Django Web Development
- Database Design
- CRUD Operations
- Dashboard Development
- Cloud Deployment

---

# Live Demo

🔗 **Live Application**  
https://academic-management-system-jz3f.onrender.com

---

# Problem Statement

Educational institutions often struggle to manage academic data efficiently across multiple modules such as student records, attendance, and marks.

This project builds a **centralized academic management system** that allows administrators and teachers to manage academic information efficiently while providing a scalable architecture for future analytics and AI-driven insights.

---

# Tech Stack

## Backend
- Python
- Django

## Database
- SQLite

## Frontend
- HTML
- CSS
- Bootstrap

## Deployment
- Render Cloud Platform

---

# Features

- Academic dashboard with system overview
- Student information management
- Teacher management
- Subject and course management
- Attendance tracking system
- Marks entry and management
- Responsive admin-style dashboard UI
- Modular Django architecture

---

# System Modules

### Students
Manage student profiles, enrollment details, and academic records.

### Teachers
Maintain teacher information and faculty assignments.

### Subjects
Manage course subjects and academic syllabus tracking.

### Attendance
Record and track student attendance.

### Marks
Store and manage exam marks and academic performance.

### Dashboard
Centralized dashboard showing key academic metrics.

---

# Project Structure

```
academic-management-system/
│
├── manage.py
│
├── core/
│   ├── templates
│   ├── static
│   └── views.py
│
├── students/
│   ├── models.py
│   ├── views.py
│   └── admin.py
│
├── teachers/
│   ├── models.py
│   ├── views.py
│   └── admin.py
│
├── subjects/
│   ├── models.py
│   ├── views.py
│   └── admin.py
│
├── attendance/
│   ├── models.py
│   ├── views.py
│   └── admin.py
│
├── marks/
│   ├── models.py
│   ├── views.py
│   └── admin.py
│
├── db.sqlite3
└── requirements.txt
```

---

# Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/Tmmfaris/django-app.git
```

```
cd django-app
```

---

### Install Dependencies

```bash
pip install django
```

or

```bash
pip install -r requirements.txt
```

---

### Run Database Migrations

```bash
python manage.py migrate
```

---

### Create Admin User

```bash
python manage.py createsuperuser
```

---

### Start Development Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000
```

---

# Deployment

The application is deployed on **Render Cloud Platform** with GitHub integration.

Deployment benefits:

- Automatic redeployment
- Cloud hosting
- Scalable architecture

---

# Future Improvements

- Role-based authentication (Admin / Teacher / Student)
- Academic analytics dashboard
- AI-based student performance prediction
- REST API integration
- Data visualization and reporting system

---

# Author

**Muhammed Faris T M**

📧 Email: tmmfaris@gmail.com  
🔗 GitHub: https://github.com/Tmmfaris  
🔗 LinkedIn: [https://linkedin.com](http://www.linkedin.com/in/muhammed-faris-tm-ab1233196)

---
