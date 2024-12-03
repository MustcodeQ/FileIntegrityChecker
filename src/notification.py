import smtplib
from email.mime.text import MIMEText

def send_email_alert(recipient, subject, message):
    """Sends an email alert."""
    sender = "your_email@example.com"
    password = "your_password"

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.send_message(msg)
            print(f"Alert sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email: {e}")
