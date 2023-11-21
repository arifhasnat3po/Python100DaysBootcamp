# import smtplib


# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_mail, password=password)
# connection.sendmail(from_addr=my_mail,
#                     to_addrs="ccesaintmartintour2023@gmail.com", msg="Subject: Test mail\n\nHello World!")

# connection.close()
import datetime as dt

now = dt.datetime.now()
hour = now.hour
year = now.year
month = now.month
day = now.day

print(hour)
print(day)
print(now)

date_of_birth = dt.datetime(year=1999, month=5, day=2)
print(date_of_birth)
