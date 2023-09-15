from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

headers = {'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/116.0.0.0 Safari/537.36'
           }

url = "https://www.amazon.in/Wakefit-Organza-Engineered-Wardrobe-Hanging/dp/B09DG37LNP/ref=sr_1_4?" \
      "keywords=wardrobe&pf_rd_i=1380441031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=e02b4eeb-76a9-4229-a581-" \
      "28aa906d6be2&pf_rd_r=S7037V69SCMQ2RQZTTR0&pf_rd_s=merchandised-search-1&qid=1694770737&s=" \
      "kitchen&sr=1-4"
response = requests.get(url=url, headers=headers)
webpage = response.text
# print(webpage)
soup = BeautifulSoup(webpage, 'html.parser')

# ------ SCRAPING PRODUCT TITLE AND PRICE -------------#
title = soup.find(id='productTitle').getText().strip()
price = soup.find(name='span', class_="a-price-whole")
price = price.text.split(',')
new_price = ''
for _ in price:
    new_price += _

new_price = float(new_price)

# PRICE YOU WANT
base_price = 10000.0


# ------SENDING THE EMAIL USING SMTPLIB -----#
port = 587  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = ""  # Enter your address
receiver_email = ""  # # Enter receiver address
password = " " # insert your 16 digit App password here

if new_price <= base_price:
    message = f"{title} is now {new_price}"

    with smtplib.SMTP(smtp_server, port=port) as connection:
        connection.starttls()
        result = connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=receiver_email,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
