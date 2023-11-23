import smtplib
import pandas as pd
import random
import datetime as dt
import csv

today = dt.datetime.now().date()
today_month, today_day = today.month, today.day
today_tuple = (today_month, today_day)

with open("birthdays.csv", "r") as csvfile:
    birthdays = pd.read_csv(csvfile)
    # print(birthdays)

    birthdays_dict = {(row['month'], row['day'])
                       : row for _, row in birthdays.iterrows()}

print(birthdays_dict)


# HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today_tuple in birthdays_dict:
    random_letter = random.randint(1, 3)
    letter_path = f"letter_templates/letter_{random_letter}.txt"
    with open(letter_path, "r") as letter_file:
        letter_content = letter_file.read()

    name_to_replace = birthdays_dict[today_tuple]['name']
    letter_content = letter_content.replace('[NAME]', name_to_replace)

    print(letter_content)

my_mail = "anikansky0@gmail.com"
password = "xxcj wjyx gqks zubt"
Subject = "Subject:Happy Birthday\n\n"
body = letter_content
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(my_mail, password=password)
connection.sendmail(
    from_addr=my_mail, to_addrs=birthdays_dict[today_tuple]['email'], msg=Subject+body)
connection.close()
