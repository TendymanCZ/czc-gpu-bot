from bs4 import BeautifulSoup
import requests
import threading
import time
from threading import Timer

while 1==1:
    unavailible = "Neznámácena"
    html_text = requests.get("https://www.czc.cz/herni-graficke-karty/produkty?q-c-0-f_2027483=sGeForce%20RTX%203060%20Ti&q-c-1-f_2027483=sGeForce%20RTX%203070").text
    time.sleep(10)
    soup = BeautifulSoup(html_text, "lxml")
    avail = soup.find_all("div", class_ = "new-tile")
    for item in avail:
        item_tile = item.find("div", class_ = "tile-title").text.replace(' ', '')
        price = item.find("div", class_ = "total-price").text.replace(' ','')
        item_link = item.div.a["href"]
        if unavailible not in price:
            print(f" ")
            print(f"GPU: {item_tile.strip()}")
            print(f"Link: https://www.czc.cz{item_link}")
            print(f"Price: {price.strip()}")




