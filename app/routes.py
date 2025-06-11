from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import User, Internship, Domain
import app.services as services
from app.services import (
    register_user,
    login_user,
    logout_user,
    apply_for_internship,
    list_internships,
    manage_domains,
    get_user_profile,
    update_profile,
    generate_reports,
    assign_grade,
    configure_duration_rules
)

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        success, msg = services.login_user(request.form)
        flash(msg, 'success' if success else 'danger')
        return redirect(url_for('main.dashboard' if success else 'main.login'))
    return render_template('login.html')

@main.route('/logout')
def logout():
    services.logout_user()
    flash("Logged out successfully", "info")
    return redirect(url_for('main.login'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        success, msg = services.register_user(request.form)
        flash(msg, 'success' if success else 'danger')
        return redirect(url_for('main.login'))
    return render_template('register.html')

@main.route('/dashboard')
def dashboard():
    user_id = session.get('user_id')
    user = User.query.get(user_id) if user_id else None
    return render_template('dashboard.html', user=user)

@main.route('/internship/form', methods=['GET', 'POST'])
def internship_form():
    if request.method == 'POST':
        success, msg = services.apply_for_internship(request.form)
        flash(msg, 'success' if success else 'danger')
        return redirect(url_for('main.internship_list'))

    domains = services.get_all_domains()
    return render_template('internship_form.html', domains=domains)

@main.route('/internship/list')
def internship_list():
    all_internships = Internship.query.all()
    return render_template('internship_list.html', internships=all_internships)

@main.route('/domain-management', methods=['GET', 'POST'])
def domain_management():
    if request.method == 'POST':
        services.manage_domains(request.form)
        flash("Domain updated successfully!", "success")
        return redirect(url_for('main.domain_management'))
    return render_template('domain_management.html')

@main.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        services.update_profile(request.form)
    profile_data = services.get_user_profile()
    return render_template('user_profile.html', user=profile_data)

@main.route('/admin')
def admin_panel():
    return render_template('admin_panel.html')

@main.route('/duration-configuration', methods=['GET', 'POST'])
def duration_configuration():
    if request.method == 'POST':
        services.configure_duration_rules(request.form)
        flash("Rules updated!", "success")
        return redirect(url_for('main.duration_configuration'))
    return render_template('duration_configuration.html')

@main.route('/reports')
def reports():
    data = services.generate_reports()
    return render_template('reports.html', reports=data)

@main.route('/grade', methods=['GET', 'POST'])
def grade():
    from app.models import Internship
    internships = Internship.query.all()

    if request.method == 'POST':
        services.assign_grade(request.form)
        flash("Grade assigned successfully!", "success")
        return redirect(url_for('main.grade'))

    return render_template('grade.html', internships=internships)