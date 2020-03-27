#from yahoo_fin import stock_info as si
#si.get_live_price("appl")
#API Key P6Qq2bpJ8nZgCkjyoRq9
# import quandl
# quandl.ApiConfig.api_key = "P6Qq2bpJ8nZgCkjyoRq9"
# data = quandl.get("FRED/GDP", start_date="2001-12-31", end_date="2005-12-31")
from finnhub import client as Finnhub
import pprint
#Imports as dictionary
client = Finnhub.Client(api_key="bpv6h7vrh5rabkt31o30")
#TO_Stocks = client.stock_symbol(exchange="TO")

#pprint.pprint(client.company_profile(symbol="SRT-UN.TO"))
#print("PRICE")
print(client.price_target(symbol="SRT-UN.TO"))