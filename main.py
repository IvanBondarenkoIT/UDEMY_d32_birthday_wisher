import smtplib
import config


# connection = smtplib.SMTP("smtp.gmail.com")
connection = smtplib.SMTP("smtp.meta.ua:25")
connection.starttls()
connection.login(user=config.my_email, password=config.password)
connection.sendmail(from_addr=config.my_email, to_addrs=config.to_email, msg="Hello")
connection.close()
