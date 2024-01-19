import requests
import datetime as d
import calendar as c

btc = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
data = btc.text[1:-1].replace('"',"").split(",")
price = float(dict(pair.split(":") for pair in data)['price'])
date = d.datetime.today()
month = c.month_name[date.month]
year = date.year
day = date.day

with open("dataSheet.txt","a") as f:
    f.write(f"{month, day, year}, {'':>3}PRICE: {price:,.2f}\n")

with open("dataSheet.txt","r") as fr:
    content = fr.read()

print(content)
