import requests
from bs4 import BeautifulSoup
import smtplib



URL = "https://www.amazon.com/Sony-Wireless-Bluetooth-Headphones-Ear/dp/B0BTJCRW9L/ref=sr_1_7?crid=1C6MUQXR13VQU&keywords=sony%2Bheadphones&qid=1703884951&sprefix=son%2Caps%2C337&sr=8-7&th=1&language=en_US&currency=USD"


response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
amason_price = soup.find(name="span", class_="a-price-whole")
price_as_float = float(amason_price.get_text(strip=True))

# print(amason_price.get_text(strip=True))
# print(price_as_float)




Subject = "Subject: Amazon Price Alert!\n\n"
body = "Sony Wireless Bluetooth Headphones - Up to 50 Hours Battery Life with Quick Charge Function, On-Ear Model - WH-CH520W.CE7 - Limited Edition is $60 now"
if price_as_float <= 70:
    # send email notification
    my_mail = "anikansky0@gmail.com"
    password = "xxcj wjyx gqks zubt"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(from_addr=my_mail,
                        to_addrs="ccesaintmartintour2023@gmail.com", msg=Subject + body)

    connection.close()
    print("Connection successful")
    


