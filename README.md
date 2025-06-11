# internship-management
An end-to-end web application for managing student internships, developed using Flask, MySQL, and Bootstrap. This system supports student registration, internship applications, grading, report generation, and admin domain management.

# Features

Student Registration & Login

Internship Application Submission
Domain Management by Admin
Internship Approval Workflow
Grading System with Feedback
Report Generation
Responsive UI with HTML, CSS, JS, and Bootstrap

# Tech Stack
Layer	Technologies Used
Frontend	HTML, CSS, Bootstrap, JavaScript
Backend	Python, Flask, Flask-Migrate
Database	MySQL + SQLAlchemy ORM
Tools	Alembic (migrations), Jinja2 (templating)
Deployment	Localhost (development)

# Folder Structure

internship-management/
│
├── app/
│   ├── templates/            # HTML templates
│   ├── static/               # CSS, JS, Images
│   ├── __init__.py           # Flask app factory
│   ├── models.py             # SQLAlchemy models
│   ├── routes.py             # Flask routes
│   ├── services.py           # Business logic
│   ├── validators.py         # Input validation
│
├── migrations/               # Alembic migration scripts
├── README.md                 # Project description
├── config.py                 # Database & config setup
├── run.py                    # App entry point
Setup Instructions
Clone the Repository

Install Requirements
pip install -r requirements.txt
Configure MySQL DB
Update your credentials in config.py.

Initialize the DB
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Run the App
flask run
