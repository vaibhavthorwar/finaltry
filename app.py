from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Configure email sender and receiver
EMAIL_ADDRESS = " ashghadi7@gmail.com "  # Replace with your Gmail address
EMAIL_PASSWORD = "gtkg vjzx hfbz ejpj"  # Replace with your Gmail password or App Password
RECEIVER_EMAIL = " ashghadi7@gmail.com "  # Replace with the receiver's email

@app.route("/")
def home():
    return render_template("index.html")  # Render the provided HTML file (index.html)

@app.route("/send-email", methods=["POST"])
def send_email():
    try:
        # Get form data
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Prepare email content
        subject = "New Contact Form Submission"
        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        # Create email
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = RECEIVER_EMAIL
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Send email via SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Start TLS encryption
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login to Gmail
            server.sendmail(EMAIL_ADDRESS, RECEIVER_EMAIL, msg.as_string())  # Send the email

        return "Thank you for visiting! Your message has been sent."
    except Exception as e:
        return f"Failed to send email: {e}"

if __name__ == "__main__":
    app.run(debug=True)
