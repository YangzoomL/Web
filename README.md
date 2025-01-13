
# Champion Martial Arts Club - Web Application

This is a lightweight Flask-based web application for managing karate trial bookings and contact messages. The app provides functionality for:
- Viewing pages like "About Us", "Our Trainers", and "Class Schedule".
- Submitting and managing trial bookings.
- Contacting the organization through a contact form.

---

## **Features**
- Dynamic routing using Flask.
- User-friendly booking form with validation.
- Contact form to send inquiries directly to the organization.
- SQLite database for lightweight data management.
- Flash messages for user feedback.

---

## **Project Structure**

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
├── requirements-dev.txt     # Development dependencies
└── karate.db                # SQLite database (auto-created on first run)
```

---

## **Setup Instructions**

### **Prerequisites**
- Python 3.10+ installed on your system.
- Basic understanding of Flask and Python.
- A terminal or command prompt to run commands.

---

### **Installation**

1. **Clone the Repository**:
   ```
   git clone https://github.com/YOUR-USERNAME/ChampionMartialArtsWeb.git
   cd Web
   ```

2. **Create a Virtual Environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**:
   - **For Production (Runtime Only)**:
     ```
     pip install -r requirements.txt
     ```
   - **For Development (Runtime + Tools)**:
     ```
     pip install -r requirements-dev.txt
     ```

4. **Initialize the Database**:
   ```
   python -c "from db import init_db; init_db()"
   ```

5. **Running the Application**:
   ```
   python app.py
   ```
   By default, the app runs on [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## **Testing**

1. **Run Tests**:
   ```
   pytest
   ```

2. **Run Tests with Coverage**:
   ```
   pytest --cov=. --cov-report=html
   ```
   The HTML report will be saved in the `htmlcov/` directory.

---

## **Code Formatting**

### **Using Black**
1. Check code formatting:
   ```
   black --check .
   ```

2. Automatically format the code:
   ```
   black .
   ```

---

## **CI/CD Pipeline**

This project includes a GitHub Actions pipeline for continuous integration. The pipeline performs the following tasks:
1. Checks for code formatting using **Black**.
2. Runs security scans using **Bandit** and **Safety**.
3. Executes tests and generates code coverage reports.
4. Ensures dependency vulnerabilities are checked with GitHub’s **Dependabot**.

---

### **GitHub Actions Workflow**

Here’s a summary of the workflow file:
- **Triggers**:
  - Push to any branch.
  - Pull requests to the main branch.

- **Steps**:
  1. Checkout the code.
  2. Set up Python.
  3. Cache pip dependencies for faster builds.
  4. Install all development dependencies.
  5. Run tests with coverage reports.
  6. Perform security checks with **Safety** and **Bandit**.
  7. Check code formatting with **Black**.
  8. Optionally upload coverage to Codecov.

---

## **Deployment**

For production deployment:
1. Install only runtime dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the Flask application:
   ```
   python app.py
   ```

---

