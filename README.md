# HRMS Lite - Backend API
 
## Project Overview
HRMS Lite Backend is a robust RESTful API built with **Django** and **Django REST Framework (DRF)**. It serves as the data management layer for the HRMS Lite application, handling employee records, attendance tracking, and business logic validation.
 
##  Tech Stack
- **Framework**: Django 5.x
- **API Toolkit**: Django REST Framework
- **Database**: SQLite (Default) / Extensible to PostgreSQL
- **CORS**: `django-cors-headers` for frontend communication
- **Server**: Gunicorn (Production), Manage.py (Dev)
 
## Project Structure
```
hrms_backend/
├── api/                # Main app containing models, views, and serializers
│   ├── models.py       # database schema (Employee, Attendance)
│   ├── views.py        # API logic (ViewSets)
│   ├── serializers.py  # JSON conversion
│   └── urls.py         # API routing
├── hrms_backend/       # Project configuration (settings.py)
├── db.sqlite3          # Local database
├── Dockerfile          # Container configuration
├── manage.py           # Django command-line utility
└── requirements.txt    # Python dependencies
```
 
##  Setup & Installation
 
### Prerequisites
- Python 3.8+
- pip (Python package manager)
 
### 1. Initialize Authentication
Navigate to the backend directory:
```bash
cd hrms_backend
```
 
### 2. Create Virtual Environment
It is recommended to use a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
 
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
 
### 4. Database Setup
Apply migrations to create the database schema:
```bash
python manage.py makemigrations
python manage.py migrate
```
 
### 5. Run Development Server
```bash
python manage.py runserver
```
The API will be available at `http://localhost:8000`.
 
## 🔌 API Endpoints
 
### Employees
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/employees/` | List all employees |
| `POST` | `/api/employees/` | Create a new employee |
| `GET` | `/api/employees/{id}/` | Retrieve specific employee details |
| `PUT` | `/api/employees/{id}/` | Update employee details |
| `DELETE` | `/api/employees/{id}/` | Delete an employee record |
 
**Sample Employee Object:**
```json
{
    "employee_id": "EMP001",
    "full_name": "John Doe",
    "email": "john@example.com",
    "department": "Engineering"
}
```
 
### Attendance
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/attendance/` | List all attendance records |
| `POST` | `/api/attendance/` | Mark attendance (Present/Absent) |
 
**Logic:**
- Prevents duplicate attendance entries for the same employee on the same day.
- Validates that the employee exists before marking attendance.
 
##  Docker Deployment
To build and run the backend container independently:
```bash
docker build -t hrms-backend .
docker run -p 8000:8000 hrms-backend
```
 
