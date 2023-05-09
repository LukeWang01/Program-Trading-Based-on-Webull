import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from env_k._secrete import LukeLab_Email_Pwd, LukeLab_Email


def send_email(from_, to, msg_subject, msg_body):
    # create message
    msg = MIMEMultipart()
    msg['From'] = from_
    msg['To'] = to
    msg['Subject'] = msg_subject

    # add text to message
    msg.attach(MIMEText(msg_body))

    # setup gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = LukeLab_Email
    smtp_password = LukeLab_Email_Pwd

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)




