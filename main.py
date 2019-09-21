from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import smtplib
import time
#import db_connection

url = 'https://www.amazon.de/Apple-AirPods-Ladecase-Neuestes-Modell/dp/B07PZR3PVB'
price_map = {'2016-12-13': '180'}
date = time.strftime("%d %b %Y", time.gmtime())


# Opening connection
uClient = uReq(url)
page_html = uClient.read()
uClient.close() 

page_soup = soup(page_html, 'html.parser')
title = page_soup.find(id="productTitle").get_text()
price = page_soup.find(id="priceblock_ourprice").get_text()
#price = price.replace(",",".").replace("€","").strip()
# FIX price = float(price.replace("€", ""))
converted_price = float(price[0:3])


# Create spreadsheet
filename = "airpods.csv"
f = open(filename, "w")
headers = "date, price\n"
f.write(headers)
f.write('2016-12-13, 180\n')


def check_price():
    if(converted_price < 140):
        send_mail()

    print(converted_price)
    print(title.strip())

    # Sets date to the current date
    date = time.strftime("%d %b %Y", time.gmtime())
    price_map[date] = converted_price
    f_price = str(converted_price)
    f.write(date.replace(",", " ") + "," + f_price + "\n")
    f.close()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('pasquarelli.le@gmail.com', 'ggdrjlfnwyzdksog')

    subject = 'Price fell down!'
    body = 'Check the amazon link: ' + url

    msg = f"Subject : {subject}\n\n{body}"

    server.sendmail('pasquarelli.le@gmail.com', 'pasquarelli.le@gmail.com', msg)

    print("Mail has been sent")
    server.quit



while(True):
    check_price()
    print(price_map)
    #db_connection.insert_date()
    time.sleep(86400)