from app.models import Domain

def validate_application(data):
    try:
        age = int(data.get('age', 0))
        duration = int(data.get('duration', 0))
        domain_id = int(data.get('domain_id'))
    except (ValueError, TypeError):
        return False, "Age, duration, and domain ID must be valid numbers."

    if not (18 <= age <= 30):
        return False, "Age must be between 18 and 30."

    if not (1 <= duration <= 6):
        return False, "Duration must be 1–6 months."

    domain = Domain.query.get(domain_id)
    if not domain:
        return False, "Invalid domain selected."

    return True, ""