from iexfinance import get_historical_data
from datetime import *
import matplotlib.pyplot as plt
import requests
import pandas
import json

stock = input("Enter your ticker symbol: " )

today = date.today()
lastweek = date.today() - timedelta(8)

print(lastweek)
print(today)

start = lastweek

end = today

f = get_historical_data(stock, start, end, output_format='pandas')

plt.plot(f["close"])

plt.title('Time series chart for ' + (stock))

plt.show()
