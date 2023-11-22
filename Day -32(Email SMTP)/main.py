import datetime as dt
import smtplib
import random
with open("quotes.txt", "r") as f:
    quotes = f.readlines()
    quote_of_the_day = random.choice(quotes)
    print(quote_of_the_day)

Subject = "Subject: Monday Motivational Quote\n\n"
body = quote_of_the_day
day = dt.datetime.today()
week = day.weekday()
# print(week)
if week == 2:
    my_mail = "anikansky0@gmail.com"
    password = "xxcj wjyx gqks zubt"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(from_addr=my_mail,
                        to_addrs="ccesaintmartintour2023@gmail.com", msg=Subject + body)

    connection.close()
