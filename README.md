# 👨‍💼 Employee Management System

A modern **Employee Management System (EMS)** built with **Django**, **SQLite**, **HTML**, **CSS**, and **Bootstrap**. This application allows administrators to securely manage employee records through a clean dashboard with authentication, employee management, search functionality, and responsive design.

---

## 📌 Features

- 🔐 Secure User Authentication (Login & Logout)
- 📊 Interactive Admin Dashboard
- 👥 Add New Employees
- ✏️ Edit Employee Information
- 🗑️ Delete Employee Records
- 🔍 Search Employees
- 🏢 Department-wise Employee Management
- 💰 Salary Information
- 📱 Fully Responsive User Interface
- 📂 Employee Profile Management
- 📈 Dashboard Statistics

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Programming |
| Django | Web Framework |
| SQLite | Database |
| HTML5 | Frontend Structure |
| CSS3 | Styling |
| Bootstrap | Responsive UI |
| JavaScript | Client-side Functionality |
| WhiteNoise | Static File Handling |
| Gunicorn | Production WSGI Server |
| Render | Cloud Deployment |

---

## 📂 Project Structure

```text
Employee-Management-System/
│
├── employees/              # Main Django App
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── ems/                    # Django Project
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── static/
├── media/
├── manage.py
├── requirements.txt
├── build.sh
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Sowmyabondili/Employee-Management-System.git
```

### Navigate to the Project

```bash
cd Employee-Management-System
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Database Migrations

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Development Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## 📷 Screenshots

> Add screenshots here after uploading them to your repository.

### Login Page

```
docs/login.png
```

### Dashboard

```
docs/dashboard.png
```

### Employee List

```
docs/employee-list.png
```

### Add Employee

```
docs/add-employee.png
```

---

## 🚀 Deployment

This project is deployment-ready using **Render**.

### Build Command

```bash
./build.sh
```

### Start Command

```bash
gunicorn ems.wsgi:application
```

---

## 📦 Requirements

Major packages used:

- Django
- Gunicorn
- WhiteNoise
- Pillow
- psycopg2-binary

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Authentication

The system provides:

- Secure Login
- Logout
- Session Management
- Protected Dashboard
- Protected Employee Operations

---

## 📈 Future Enhancements

- Employee Attendance Module
- Payroll Management
- Email Notifications
- Export to Excel/PDF
- Role-based Access Control
- REST API Integration
- PostgreSQL Database
- Employee Performance Analytics

---

## 👩‍💻 Author

**Sowmya Bondili**

B.Tech – Artificial Intelligence & Data Science

Velagapudi Ramakrishna Siddhartha Engineering College (VRSEC)

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is developed for educational and learning purposes.
