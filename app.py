from flask import Flask, render_template, request, redirect, url_for, flash
from db import init_db, get_db_connection
import secrets

from validators import validate_booking_form, validate_contact_form

app = Flask(__name__)

# Set a secret key for session management and flash messages
app.secret_key = secrets.token_hex(
    16
)  # Generate a random secret key for session and flash messages


# Home route (index page)
@app.route("/")
def index():
    return render_template("index.html")


# Booking route
@app.route("/book", methods=["GET", "POST"])
def book():
    if request.method == "POST":
        # Get form data
        form_data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "phone": request.form["phone"],
            "experience": request.form.get("experience", ""),
            "trial_date": request.form["trial_date"],
            "trial_time": request.form["trial_time"],
        }

        # Validate the form data
        is_valid, error_message = validate_booking_form(form_data)
        if not is_valid:
            flash(error_message, "error")
            return redirect(url_for("bookings"))

        # Insert validated data into the database
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO bookings (name, email, phone_number, experience, trial_date, trial_time)
                VALUES (?, ?, ?, ?, ?, ?)
            """,
                (
                    form_data["name"],
                    form_data["email"],
                    form_data["phone"],
                    form_data["experience"],
                    form_data["trial_date"],
                    form_data["trial_time"],
                ),
            )
            conn.commit()

        # Flash success message
        flash(
            "Your booking has been confirmed! A confirmation email has been sent.",
            "success",
        )
        return redirect(url_for("index"))  # Redirect back to home page

    return render_template("index.html")  # Render booking form


# Contact route
@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Handle contact form submissions."""
    if request.method == "POST":
        # Collect form data
        form_data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "message": request.form["message"],
        }

        # Validate the form data
        is_valid, error_message = validate_contact_form(form_data)
        if not is_valid:
            flash(error_message, "error")
            return redirect(url_for("contact"))

        # Save validated contact message to SQLite database
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO contact_messages (name, email, message)
                VALUES (?, ?, ?)
            """,
                (form_data["name"], form_data["email"], form_data["message"]),
            )
            conn.commit()

        flash("Your message has been sent successfully!", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")


# About route
@app.route("/about")
def about():
    return render_template("about.html")


# Trainers route
@app.route("/trainers")
def trainers():
    return render_template("trainers.html")


# Schedule route
@app.route("/schedule")
def schedule():
    return render_template("schedule.html")


if __name__ == "__main__":
    # Initialize the database when the app starts
    init_db()
    app.run(debug=True)
