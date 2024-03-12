import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# password is generated for an email address to give access to third party services.
# Over here generate your password from this.. "https://myaccount.google.com/apppasswords"

def send_mail():
    sender_email = "example@gmail.com"
    receiver_email = "example@gmail.com"
    password = "xxxx xxxx xxxx xxxx"
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Gondola Booking Notification"
    
    body = "Gondola booking slot is available for x/y/zzzz ! Visit the website now."
    msg.attach(MIMEText(body, 'plain'))
    
    # Send email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp_server:
        smtp_server.starttls()
        smtp_server.login(sender_email, password)
        smtp_server.send_message(msg)
        return True
