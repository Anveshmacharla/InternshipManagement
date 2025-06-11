# Internship Management System
A complete web application to manage student internships, built with Flask, MySQL, and Bootstrap. It includes modules for registration, internship applications, admin approvals, grading, and report generation.

# Features
Student Registration & Login

Internship Application Submission

Admin Domain Management

Internship Approval Workflow

Grading System with Feedback

Report Generation

Responsive Design using HTML, CSS, JavaScript, and Bootstrap

# Tech Stack

Layer	Technologies Used

Frontend	HTML, CSS, JavaScript, Bootstrap

Backend	Python, Flask, Flask-Migrate

Database	MySQL, SQLAlchemy ORM

Utilities	Alembic (migrations), Jinja2 (templating)

Deployment	Localhost (development)

# Install Dependencies

pip install -r requirements.txt

Configure the Database
Open config.py

Update the MySQL database credentials (username, password, host, db name)

Initialize the Database

flask db init

flask db migrate -m "Initial migration"

flask db upgrade

Run the Application

flask run
