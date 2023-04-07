import random
import datetime as dt
import smtplib
import config


def send_mail(subject, massage):
    with smtplib.SMTP(config.gmail_smtp) as connection:
        connection.starttls()
        connection.login(user=config.my_email,
                         password=config.app_password)
        connection.sendmail(from_addr=config.my_email,
                            to_addrs=config.to_email,
                            msg=f"Subject:{subject}\n\n{massage}")


def get_random_quote(filename):
    with open(filename, 'r') as f:
        return random.choice(f.readlines())


TEST_WEEKDAY = 4
now = dt.datetime.now()
weekday = now.weekday()
if weekday == TEST_WEEKDAY:
    send_mail(subject="Hello", massage=get_random_quote("quotes.txt"))
