from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# === Mail Configuration ===
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'infinitetechnology06@gmail.com'  # Your Gmail address
app.config['MAIL_PASSWORD'] = 'dbccuahkabuwzrdn'      # Your Gmail App Password here

mail = Mail(app)

# === Page Routes ===
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('aboutus.html')

@app.route('/service')
def services():
    return render_template('services.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('site.xml')

@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        phone = request.form.get('phone', 'N/A')
        message_body = request.form.get('message')

        message = Message(
            subject="New Contact Form Submission",
            sender=app.config['MAIL_USERNAME'],
            recipients=["infinitetechnology06@gmail.com"],
            body=f"""
New Inquiry from Contact Form:

First Name: {firstname}
Last Name: {lastname}
Email: {email}
Phone: {phone}
Message:
{message_body}
"""
        )

        try:
            mail.send(message)
            flash('✅ Your message has been sent successfully!', 'success')
        except Exception as e:
            print(f"Mail sending error: {e}")
            flash('❌ There was an error sending your message. Please try again later.', 'danger')

        return redirect(url_for('contact_page'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
