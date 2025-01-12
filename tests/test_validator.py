from validators import validate_booking_form, validate_contact_form


def test_validate_booking_form_valid():
    """Test valid booking form data."""
    data = {
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890",
        "experience": "beginner",
        "trial_date": "2025-01-15",
        "trial_time": "10:00",
    }
    is_valid, error = validate_booking_form(data)
    assert is_valid
    assert error is None


def test_validate_booking_form_missing_name():
    """Test booking form with missing name."""
    data = {
        "email": "john@example.com",
        "phone": "1234567890",
        "experience": "beginner",
        "trial_date": "2025-01-15",
        "trial_time": "10:00",
    }
    is_valid, error = validate_booking_form(data)
    assert not is_valid
    assert error == "Name is required."


def test_validate_contact_form_valid():
    """Test valid contact form data."""
    data = {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "message": "Hello! I have a question about classes.",
    }
    is_valid, error = validate_contact_form(data)
    assert is_valid
    assert error is None


def test_validate_contact_form_invalid_email():
    """Test contact form with invalid email."""
    data = {
        "name": "Jane Doe",
        "email": "invalid-email",
        "message": "Hello! I have a question about classes.",
    }
    is_valid, error = validate_contact_form(data)
    assert not is_valid
    assert error == "Invalid email address."
