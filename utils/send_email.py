import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from env._secrete import LukeLab_Email_Pwd, LukeLab_Email


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


def send_emails(from_, to: list, msg_subject, msg_body):
    # send an email to multiple recipients
    sender_email = from_
    receiver_emails = to    # ['recipient1@example.com', 'recipient2@example.com']
    message = msg_body

    msg = MIMEText(message)
    msg['Subject'] = msg_subject
    msg['From'] = sender_email
    msg['To'] = LukeLab_Email
    # msg["Cc"] = ''
    # msg['Bcc'] = ', '.join(receiver_emails)
    # toaddrs = [msg['To']] + [msg['Bcc']]

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(LukeLab_Email, LukeLab_Email_Pwd)
        server.sendmail(LukeLab_Email, [LukeLab_Email] + receiver_emails, msg.as_string())

