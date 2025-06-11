print("✅ services.py loaded!")

from app.models import db, Internship, User, Domain, Grade
from app.validators import validate_application
from datetime import datetime

def register_user(data):
    return True, "User registered."

def login_user(data):
    return True, "User logged in."

def logout_user():
    return True

def apply_for_internship(data):
    valid, msg = validate_application(data)
    if not valid:
        return False, msg

    domain = Domain.query.filter_by(name=data.get('domain')).first()
    if not domain:
        return False, "Selected domain does not exist."

    try:
        start_date = datetime.strptime(data.get('start_date'), "%Y-%m-%d").date()
        end_date = datetime.strptime(data.get('end_date'), "%Y-%m-%d").date()
    except Exception:
        return False, "Invalid date format. Please use yyyy-mm-dd."

    internship = Internship(
        user_id=1,  # Temporary fixed user
        title=data.get('title'),
        domain_id=domain.id,
        start_date=start_date,
        end_date=end_date,
        duration=int(data.get('duration')),
        status='pending',
        remarks=data.get('remarks', '')
    )

    db.session.add(internship)
    db.session.commit()
    return True, "Internship application submitted successfully."

def list_internships():
    return Internship.query.all()

def manage_domains(data):
    pass

def get_user_profile():
    return {"name": "Test", "email": "test@example.com"}

def get_all_domains():
    return Domain.query.all()

def update_profile(data):
    pass

def generate_reports():
    return []

def assign_grade(form_data):
    internship_id = form_data.get('internship_id')
    grade = form_data.get('grade')
    feedback = form_data.get('feedback')

    if internship_id and grade:
        new_grade = Grade(
            internship_id=internship_id,
            grade=grade,
            feedback=feedback
        )
        db.session.add(new_grade)
        db.session.commit()

def configure_duration_rules(data):
    pass