import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import datetime

def send_email():
    # Set up the SMTP server
    smtp_server = 'smtp.example.com'
    port = 587  # or 465 if using SSL
    sender_email = 'your_email@example.com'
    password = 'your_password'
    
    # Create a multipart message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = 'recipient@example.com'
    message['Subject'] = 'Daily Report - ' + str(datetime.date.today())

    # Add body to email
    body = "This is the daily report."
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, message['To'], message.as_string())

# Schedule the email to be sent daily at a specific time (e.g., 8:00 AM)
schedule.every().day.at("08:00").do(send_email)

# Infinite loop to run the scheduler
while True:
    schedule.run_pending()
