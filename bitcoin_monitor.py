import smtplib, requests
from bs4 import BeautifulSoup
import time

#website to webscrap
coinbase_url = "https://www.coinbase.com/price/bitcoin"

#header -- search in google for my computer user agent
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}

def check_price():
    #use request module to download web page from coinbase weblink
    page = requests.get(coinbase_url, headers=headers)

    #use beautiful soup  module to from webpage and parse html
    soup = BeautifulSoup(page.content, "html.parser")

    #from coinbase website, find e.g id or wrap to
    price = soup.find(wrap="wrap").get_text()
    converted_price = price[1:6]

    if converted_price == converted_price:
        send_mail()

    print(price)
    print(converted_price)


def send_mail():
    #smtplib module for outlook and server port/domain name
    server = smtplib.SMTP("smtp-mail.outlook.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    user_name_email = str("")
    pass_word = str("")
    receiver_email = str("")
    server.login(user_name_email, pass_word)

    subject = "Price Change!!"
    body = "Check the link https://www.coinbase.com/price/bitcoin"

    msg = f"Subject: {subject}\n\n{body}"

    #send mail
    server.sendmail(user_name_email, receiver_email, msg)

    print("Hey Hey, email has been sent!!")

    server.quit()

while(True):
    check_price()
    time.sleep(14400)
