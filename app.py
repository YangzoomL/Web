from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os
import secrets

app = Flask(__name__)

# Set a secret key for session management and flash messages
app.secret_key = secrets.token_hex(16)  # Generate a random secret key for session and flash messages

# Initialize SQLite database for bookings and contact form
def init_db():
    if not os.path.exists('karate.db'):
        with sqlite3.connect('karate.db') as conn:
            cursor = conn.cursor()
            # Create bookings table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS bookings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone_number TEXT NOT NULL,
                    experience TEXT,
                    trial_date TEXT NOT NULL,
                    trial_time TEXT NOT NULL
                )
            ''')
            conn.commit()

# Get SQLite DB connection
def get_db_connection():
    conn = sqlite3.connect('karate.db')
    return conn

# Home route (index page)
@app.route('/')
def index():
    return render_template('index.html')

# Booking route
@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        experience = request.form['experience']
        trial_date = request.form['trial_date']
        trial_time = request.form['trial_time']
        
        # Save booking to SQLite database
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO bookings (name, email, phone_number, experience, trial_date, trial_time)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, email, phone, experience, trial_date, trial_time))
            conn.commit()

        # Flash success message
        flash("Your booking has been confirmed! A confirmation email has been sent.", "success")
        return redirect(url_for('index'))  # Redirect back to home page

    return render_template('index.html')  # Render booking form

# Contact route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Save contact message to SQLite database
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO contact_messages (name, email, message) VALUES (?, ?, ?)", (name, email, message))
            conn.commit()
        
        # Flash a success message
        flash("We will reach out to you very soon!", "success")
        
        # After form submission, redirect to the homepage
        return redirect(url_for('index'))  # Redirect back to home page
    
    return render_template('contact.html')


# About route
@app.route('/about')
def about():
    return render_template('about.html')

# Trainers route
@app.route('/trainers')
def trainers():
    return render_template('trainers.html')

# Schedule route
@app.route('/schedule')
def schedule():
    return render_template('schedule.html')


if __name__ == '__main__':
    # Initialize the database when the app starts
    init_db()
    app.run(debug=True)
