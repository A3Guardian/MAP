import requests
from bs4 import BeautifulSoup
from money_parser import price_str
import time
import smtplib
from hashlib import new
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open(
    "C:\\Users\\Edutu\\Desktop\\IFR\\an_2\\MAP\\curs_2\\parola_google.txt"
) as fisier:
    parola_google = fisier.read().strip()

sender_email = "astefanoaieduard@gmail.com"
receiver_email = "astefanoaieduard@gmail.com"
cc_list = []
subiect = "A scazut pretul produsului dorit"

url = "https://www.emag.ro/drujba-motofierastrau-cu-lant-pe-benzina-husqvarna-372xp-5-5-cp-71-cc-lungime-lama-45-cm-965968118/pd/DM51HVBBM/?X-Search-Id=8e15c2b167e2471d34cc&X-Product-Id=40227442&X-Search-Page=1&X-Search-Position=2&X-Section=search&X-MB=0&X-Search-Action=view"
raspuns = requests.get(url)
raspuns2 = BeautifulSoup(raspuns.text, "html.parser")

pret_de_referinta = "3750"

# Metoda 1 trimtere email
# def trimite_email(sender, message, subiect, catre_cine, cc_list=[]):
#     try:
#         smtpserver = "smtp.gmail.com:587"
#         header = "From: %s\n" % sender
#         header += "To: %s\n" % ",".join(catre_cine)
#         header += "Cc: %s\n" % ",".join(cc_list)
#         header += "Subject: %s\n\n" % subiect
#         message = header + message
#         server = smtplib.SMTP(smtpserver)
#         server.starttls()
#         server.login(sender, parola_google)
#         problems = server.sendmail(sender, catre_cine, message)
#         server.quit()
#         return True
#     except:
#         print("Nu am putut trimite emailul")
#         print("Problems", problems)
#         return False

# Metoda 2 trimtere email
# def send_email(nume, pret):

#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = receiver_email
#     message["Subject"] = f"Product Update: {nume}"

#     body = f"Product Name: {nume}\nPrice: {pret}"
#     message.attach(MIMEText(body, "plain"))

#     try:
#         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#             server.login(sender_email, parola_google)
#             server.sendmail(sender_email, receiver_email, message.as_string())
#         print("Email sent successfully!")
#     except Exception as e:
#         print("Error sending email:", e)


# def verificare_trimitere_email():
#     pretul_drujbei = pret_drujba()
#     numele_drujbei = nume_drujba()
#     if pret_de_referinta > pretul_drujbei:
#         print("Pretul este mai mic !")
#         send_email(numele_drujbei, pretul_drujbei)


# def info_drujba():
#     print(raspuns.status_code)
#     print(raspuns2.prettify())


# def pret_drujba():
#     pret = raspuns2.find("p", attrs={"class": "product-new-price"}).text
#     pret = price_str(pret)
#     return pret


# def nume_drujba():
#     nume = raspuns2.find("h1", attrs={"class": "page-title"}).text
#     nume = nume.strip()
#     return nume


# def recenzii_drujba():
#     recenzii = raspuns2.find("p", attrs={"class": "review-rating-data"}).text
#     recenzii = recenzii.strip()
#     return recenzii

# verificare_trimitere_email()
# pretul_drujbei = pret_drujba()
# numele_drujbei = nume_drujba()
# recenziile_drujbei = recenzii_drujba()
# print(numele_drujbei, "\n", pretul_drujbei, "\n")
# info_drujba()
