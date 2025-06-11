from . import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum('admin', 'student'), default='student')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    internships = db.relationship('Internship', backref='user', lazy=True)
    applications = db.relationship('Application', backref='user', lazy=True)
    logs = db.relationship('Log', backref='user', lazy=True)
    domain_assignments = db.relationship('InternDomainAssignment', backref='user', lazy=True)
    validation_logs = db.relationship('ValidationLog', backref='user', lazy=True)
    mentor = db.relationship('Mentor', backref='assigned_user', lazy=True, uselist=False)


class Domain(db.Model):
    __tablename__ = 'domains'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    internships = db.relationship('Internship', backref='domain', lazy=True)
    domain_assignments = db.relationship('InternDomainAssignment', backref='domain', lazy=True)
    business_rules = db.relationship('BusinessRule', backref='domain', lazy=True)


class Internship(db.Model):
    __tablename__ = 'internships'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    domain_id = db.Column(db.Integer, db.ForeignKey('domains.id'), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    duration = db.Column(db.Integer)
    status = db.Column(db.Enum('pending', 'approved', 'completed'), default='pending')
    remarks = db.Column(db.Text)

    applications = db.relationship('Application', backref='internship', lazy=True)
    extensions = db.relationship('InternshipExtension', backref='internship', lazy=True)


class Application(db.Model):
    __tablename__ = 'applications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    internship_id = db.Column(db.Integer, db.ForeignKey('internships.id'), nullable=False)
    status = db.Column(db.Enum('pending', 'approved', 'rejected'), default='pending')
    applied_on = db.Column(db.DateTime, default=datetime.utcnow)


class Log(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    action = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


class InternDomainAssignment(db.Model):
    __tablename__ = 'intern_domain_assignments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    domain_id = db.Column(db.Integer, db.ForeignKey('domains.id'), nullable=False)
    assigned_on = db.Column(db.Date)


class Mentor(db.Model):
    __tablename__ = 'mentors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    expertise = db.Column(db.Text)
    assigned_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)


class BusinessRule(db.Model):
    __tablename__ = 'business_rules'
    id = db.Column(db.Integer, primary_key=True)
    rule_name = db.Column(db.String(100))
    rule_description = db.Column(db.Text)
    rule_type = db.Column(db.String(50))
    value = db.Column(db.String(255))
    domain_id = db.Column(db.Integer, db.ForeignKey('domains.id'), nullable=True)


class ValidationLog(db.Model):
    __tablename__ = 'validation_logs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    action = db.Column(db.Text)
    status = db.Column(db.String(20))
    message = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


class InternshipExtension(db.Model):
    __tablename__ = 'internship_extensions'
    id = db.Column(db.Integer, primary_key=True)
    internship_id = db.Column(db.Integer, db.ForeignKey('internships.id'), nullable=False)
    new_end_date = db.Column(db.Date)
    reason = db.Column(db.Text)
    approved = db.Column(db.Boolean, default=False)
    requested_on = db.Column(db.DateTime, default=datetime.utcnow)


class Grade(db.Model):
    __tablename__ = 'grades'
    id = db.Column(db.Integer, primary_key=True)
    internship_id = db.Column(db.Integer, db.ForeignKey('internships.id'), nullable=False)
    grade = db.Column(db.String(5), nullable=False)
    feedback = db.Column(db.Text, nullable=True)

    internship = db.relationship('Internship', backref='grades')