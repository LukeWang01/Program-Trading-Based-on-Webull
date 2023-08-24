import re


def is_valid_email(email):
    # TODO: check email if is a list of emails
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def is_valid_phone_number(phone_number):
    # phone must be in format +[country_code]-[your number]
    pattern = r'^\+\d+-\d+$'
    return re.match(pattern, phone_number) is not None


def is_valid_pid(pid):
    return pid.isdigit() and len(pid) == 6
