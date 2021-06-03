from time import sleep
from requests_html import HTMLSession, AsyncHTMLSession

url = "https://www.pccomponentes.com/zotac-geforce-gtx-1660-twin-fan-6gb-gddr5"

session = HTMLSession()
r = session.get(url)

while True:
    buy_zone = r.html.find("#btnsWishAddBuy")
    if len(buy_zone) > 0:
        print("Hay Stock!!")
        break
    else:
        print("Sigue sin haber stock :(")

    sleep(30)