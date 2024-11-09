import requests
import time
import smtplib
from hashlib import new
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apscheduler.schedulers.blocking import BlockingScheduler

with open(
    "C:\\Users\\Edutu\\Desktop\\IFR\\an_2\\MAP\\curs_2\\cheie_api_vreme.txt"
) as fisier:
    API_KEY = fisier.read().strip()

with open(
    "C:\\Users\\Edutu\\Desktop\\IFR\\an_2\\MAP\\curs_2\\parola_google.txt"
) as fisier:
    parola_google = fisier.read().strip()

URL_API = "https://api.openweathermap.org/data/2.5/weather"
units = "metric"  # Options: metric (°C), imperial (°F), or standard (K)
sender_email = "astefanoaieduard@gmail.com"
receiver_email = "astefanoaieduard@gmail.com"
cc_list = []
subiect = "A scazut pretul produsului dorit"
oras = "Pascani"
# oras = input("Introdu numele orasului: ")

request_url = f"{URL_API}?q={oras}&appid={API_KEY}&units={units}"
raspuns = requests.get(request_url)
if raspuns.status_code == 200:
    data = raspuns.json()

    city = data["name"]
    country = data["sys"]["country"]
    weather_description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    continut_fisier = f"\nVremea in {city}, {country}:\n"
    continut_fisier += f"- Descriere: {weather_description.capitalize()}\n"
    continut_fisier += f"- Temperatura: {temperature}°C (Se resimt: {feels_like}°C)\n"
    continut_fisier += f"- Umiditatea: {humidity}%\n"
    continut_fisier += f"- Viteza vantului: {wind_speed} m/s\n"

    print(continut_fisier)

    file_path = f"C:\\Users\\Edutu\\Desktop\\IFR\\an_2\\MAP\\curs_2\\starea_vremii_in_{city}.txt"
    with open(file_path, "w", encoding="utf-8") as fisier_iesire:
        fisier_iesire.write(continut_fisier)

else:
    print("Eroare pentru request-ul tau !")


def send_email(city, body):

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = f"Starea vremii in {city}"

    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, parola_google)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)


def verificare_trimitere_email():
    print("Prognoza meteo !")
    send_email(city, continut_fisier)


apelare_interval_timp = BlockingScheduler()
# apelare_interval_timp.add_job(verificare_trimitere_email, "interval", seconds=10)
apelare_interval_timp.add_job(verificare_trimitere_email, "cron", hour=15, minute=42)
apelare_interval_timp.start()
