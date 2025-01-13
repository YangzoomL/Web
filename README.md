# Champion Martial Arts Club - Web Application

This is a lightweight Flask-based web application for managing karate trial bookings and contact messages. The app provides functionality for:
- Viewing pages like "About Us", "Our Trainers", and "Class Schedule".
- Submitting and managing trial bookings.
- Contacting the organization through a contact form.

---

## Features
- Dynamic routing using Flask.
- User-friendly booking form with validation.
- Contact form to send inquiries directly to the organization.
- SQLite database for lightweight data management.
- Flash messages for user feedback.

---

## Project Structure

```plaintext
Web/
├── app.py                   # Main Flask app with routes
├── db.py                    # Database initialization and connection logic
├── validators.py            # Form validation logic
├── templates/               # HTML templates
│   ├── base.html            # Base layout template
│   ├── index.html           # Homepage
│   ├── bookings.html        # Booking form and management
│   ├── contact.html         # Contact form
│   ├── about.html           # About page
│   └── trainers.html        # Trainers page
├── static/                  # Static assets (CSS, JS, images)
│   ├── css/
│   │   └── style.css        # Main stylesheet
│   ├── js/
│   │   └── main.js          # JavaScript (optional)
│   └── images/              # Images for the website
├── tests/                   # Test cases for the app
│   ├── test_app.py          # Tests for app routes
│   ├── test_validators.py   # Tests for validators
├── requirements.txt         # Dependencies for the project
└── karate.db                # SQLite database (auto-created on first run)

## **Setup Instructions**

### **Prerequisites**
- Python 3.10+ installed on your system.
- Basic understanding of Flask and Python.
- A terminal or command prompt to run commands.

---

### **Installation**

1. Clone the Repository**:
   git clone https://github.com/YOUR-USERNAME/ChampionMartialArtsWeb.git
   cd Web

2. Create a Virtual Environment
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate     # On Windows

3. Install Dependencies
    pip install -r requirements.txt

4. Initialize the Database
    python -c "from db import init_db; init_db()"

5. Running the Application
    python app.py
    
    By default, the app runs on http://127.0.0.1:5000.

6. Run Tests
   pytest


