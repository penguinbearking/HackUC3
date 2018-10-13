import iexfinance
from datetime import datetime
import matplotlib.pyplot as plt
import requests
import pandas
import json

stock.upper() = input("Enter your desired ticker symbol: ")
stock = Stock((stock), output_format='pandas')
stock.get_quote().head()
stock.change_output_format('json')
quote = input("Input your quote: (avgTotalVolume, calculationPrice, change, changePercent, or close)")
stock.get_quote()[quote]