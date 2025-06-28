import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from forms import ContactForm
from translations import get_translations
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the Flask application
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

# Routes


@app.route('/')
def index():
    lang = session.get('lang', 'en')
    translations = get_translations(lang)
    return render_template('index.html', translations=translations, active_page='home')


@app.route('/about')
def about():
    lang = session.get('lang', 'en')
    translations = get_translations(lang)
    return render_template('about.html', translations=translations, active_page='about')


@app.route('/gallery')
def gallery():
    lang = session.get('lang', 'en')
    translations = get_translations(lang)
    return render_template('gallery.html', translations=translations, active_page='gallery')


@app.route('/pricing')
def pricing():
    lang = session.get('lang', 'en')
    translations = get_translations(lang)
    return render_template('pricing.html', translations=translations, active_page='pricing')


@app.route('/privacypolicy')
def privacypolicy():
    lang = session.get('lang', 'en')
    translations = get_translations(lang)
    return render_template('privacypolicy.html', translations=translations, active_page='privacypolicy')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    lang = session.get('lang', 'en')
    translations = get_translations(lang)
    form = ContactForm()

    if form.validate_on_submit():
        try:
            # Get form data
            name = form.name.data
            email = form.email.data
            phone = form.phone.data
            message = form.message.data

            # Send email (this is a placeholder - you'd need to configure your email server)
            send_email(name, email, phone, message)

            flash(translations['contact_success'], 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            logging.error(f"Error sending email: {e}")
            flash(translations['contact_error'], 'danger')

    return render_template('contact.html', form=form, translations=translations, active_page='contact')


@app.route('/set-language/<lang>')
def set_language(lang):
    session['lang'] = lang
    return redirect(request.referrer or url_for('index'))


def send_email(name, email, phone, message):
    # This function would be implemented with your email sending logic
    # For example using Flask-Mail or smtplib
    sender_email = os.environ.get("EMAIL_SENDER", "info@essawaw.pl")
    receiver_email = os.environ.get("EMAIL_RECEIVER", "info@essawaw.pl")
    password = os.environ.get("EMAIL_PASSWORD", "")

    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f"ESSA Website Contact: {name}"

    body = f"""
    New contact from ESSA website:
    
    Name: {name}
    Email: {email}
    Phone: {phone}
    
    Message:
    {message}
    """

    msg.attach(MIMEText(body, 'plain'))

    # In production, uncomment this to send the email
    """
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
    """

    # For development, just log the email
    logging.info(f"Would send email: {body}")

    return True

# Error handlers


@app.errorhandler(404)
def page_not_found(e):
    lang = session.get('lang', 'en')
    translations = get_translations(lang)
    return render_template('404.html', translations=translations), 404


@app.errorhandler(500)
def server_error(e):
    lang = session.get('lang', 'en')
    translations = get_translations(lang)
    return render_template('500.html', translations=translations), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
