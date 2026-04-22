import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from logger import logger

def send_email(sender, receiver, subject, body, smtp_config):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender["email"]
        msg['To'] = receiver
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(*smtp_config)
        server.starttls()
        server.login(sender["email"], sender["password"])
        server.sendmail(sender["email"], receiver, msg.as_string())
        server.quit()

        logger.info(f"SUCCESS {sender['email']} → {receiver}")
        return True

    except Exception as e:
        logger.error(f"ERROR {sender['email']} → {receiver} | {e}")
        return False
