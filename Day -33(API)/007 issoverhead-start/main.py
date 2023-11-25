import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 21.346178  # Your latitude
MY_LONG = 91.793287  # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead and is_night():
        my_mail = "anikansky0@gmail.com"
        password = "xxcj wjyx gqks zubt"
        Subject = "Subject:International Space Station is overhead\n\n"
        body = """I hope this letter finds you well and in good spirits. I wanted to share some thrilling news that I recently discovered – the International Space Station (ISS) is currently orbiting above us in the night sky!

    As I gazed at the stars tonight, I couldn't help but marvel at the thought of the ISS zooming through space, carrying out its incredible mission of scientific research and international collaboration. It's awe-inspiring to think about the astronauts on board, working together to explore the frontiers of space.

    If you have a moment, I encourage you to step outside and look up at the sky. The ISS is visible as a bright, moving light, and it's a truly magical sight. It serves as a reminder of the vastness of the universe and the remarkable achievements of human ingenuity.

    If you're interested, you can check online resources or use smartphone apps to track the ISS's current location and upcoming passes over our area. It's a fantastic way to connect with the cosmos and appreciate the wonders of space exploration.

    I hope you get a chance to witness this extraordinary event. It's a small but significant reminder of the incredible things happening beyond our planet.

    Wishing you clear skies and happy stargazing!"""
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_mail, password=password)
        connection.sendmail(
            from_addr=my_mail, to_addrs="mutantvader@gmail.com", msg=Subject+body)
        connection.close()

        print("The ISS is overhead and it is night.")
