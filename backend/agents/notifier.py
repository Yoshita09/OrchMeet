import smtplib
from email.mime.text import MIMEText

def send_notification(summary, tasks):
    body = f"Meeting Summary:\n{summary}\n\nTasks:\n{tasks}"
    msg = MIMEText(body)
    msg['Subject'] = 'OrchMeet Summary & Tasks'
    msg['From'] = 'you@example.com'
    msg['To'] = 'participant@example.com'

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login("you@example.com", "your-password")
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
