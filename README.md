# Secure Offer Letter Portal
A secure web application to manage and generate offer letters for students. Built using Flask, JWT Authentication, MySQL, and Bootstrap, this system provides a protected login system, student registration, and a personalized dashboard displaying user-specific offer letter details.

# Features
Student Registration & Login (with JWT Auth)

Secure Token-Based Authentication

Offer Letter Management (extendable)

Error Handling and Redirects

Responsive UI with Bootstrap 5

# Tech Stack
Layer	Technologies Used

Frontend	HTML, CSS, JavaScript, Bootstrap

Backend	Python, Flask, Flask-JWT-Extended

Database	MySQL, SQLAlchemy ORM

Utilities	Alembic (migrations), Jinja2 (templates), LocalStorage (token storage in browser)

Deployment	Localhost (development)

# Setup Instructions

Install Dependencies:

pip install -r requirements.txt

Configure the Database

Edit the config.py file:

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<username>:<password>@localhost/<database_name>'
Replace <username>, <password>, and <database_name> with your local MySQL credentials.

Initialize the Database

flask db init

flask db migrate -m "Initial migration"

flask db upgrade

Run the Application

flask run
flask run
