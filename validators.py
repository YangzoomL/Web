import re


def validate_booking_form(data):
    """
    Validate the form data for the booking form.

    Args:
        data (dict): The form data to validate.

    Returns:
        tuple: (bool, str) Validation status and error message (if any).
    """
    # Check required fields
    required_fields = ["name", "email", "phone", "trial_date", "trial_time"]
    for field in required_fields:
        if not data.get(field):
            return False, f"{field.replace('_', ' ').capitalize()} is required."

    # Validate email format
    if not re.match(r"[^@]+@[^@]+\.[^@]+", data["email"]):
        return False, "Invalid email address."

    # Validate phone format (basic check for digits and length)
    if not re.match(r"^\d{10,15}$", data["phone"]):
        return False, "Invalid phone number. It must contain 10 to 15 digits."

    # Validate experience (optional, but if provided, it must match allowed values)
    valid_experiences = ["beginner", "intermediate", "advanced"]
    if data.get("experience") and data["experience"].lower() not in valid_experiences:
        return False, "Invalid experience level."

    # Additional checks for trial_date and trial_time can go here (e.g., valid date/time formats)

    return True, None


def validate_contact_form(data):
    """
    Validate the form data for the contact form.

    Args:
        data (dict): The form data to validate.

    Returns:
        tuple: (bool, str) Validation status and error message (if any).
    """
    # Check required fields
    required_fields = ["name", "email", "message"]
    for field in required_fields:
        if not data.get(field):
            return False, f"{field.capitalize()} is required."

    # Validate email format
    if not re.match(r"[^@]+@[^@]+\.[^@]+", data["email"]):
        return False, "Invalid email address."

    # Validate message length (optional)
    if len(data["message"].strip()) < 10:
        return False, "Message must be at least 10 characters long."

    return True, None
