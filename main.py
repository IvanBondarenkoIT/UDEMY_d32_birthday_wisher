from random import randint as rd
from datetime import datetime as dt
from smtplib import SMTP as smt
from pandas import read_csv as pd
from config import gmail_smtp, my_email, app_password


def send_mail(to_email: str, subject: str, massage: str) -> None:
    with smt.SMTP(gmail_smtp) as connection:
        connection.starttls()
        connection.login(user=my_email,
                         password=app_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject:{subject}\n\n{massage}")


def send_mail_heppy_birthday(current_month_day: tuple) -> None:
    # 1. Update the birthdays.csv
    data_frame = pd.read_csv("birthdays.csv")
    birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data_frame.iterrows()}

    # 2. Check if today matches a birthday in the birthdays.csv
    if current_month_day in birthdays_dict:

        # 3.1 If step 2 is true, pick a random letter from letter templates
        with open(f"letter_templates/letter_{rd.randint(1, 3)}.txt", ) as letter_file:
            letter_text = letter_file.read()

            # 3.2 and replace the [NAME] with the person's actual name from birthdays.csv
            letter_text = letter_text.replace("[NAME]", birthdays_dict[current_month_day]["name"])

        # 4. Send the letter generated in step 3 to that person's email address.
        send_mail(to_email=birthdays_dict[current_month_day]["email"],
                  subject=f"Heppy birthday,{birthdays_dict[current_month_day]['name']}!",
                  massage=letter_text)


##################### Extra Hard Starting Project ######################

if __name__ == "__main__":
    send_mail_heppy_birthday((dt.datetime.now().month, dt.datetime.now().day))