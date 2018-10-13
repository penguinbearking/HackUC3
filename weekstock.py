from iexfinance import *
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

data = get_historical_data(stock, start, end, output_format='pandas')
a = type(data)
print(a)

datalist = data.values.tolist()
print(datalist)

"""
i = 0
for i in range(len(data)):
    j = (date.today() - timedelta(i)).weekday()
    if j == 5 or j == 6:
        data.pop(i)
        print ("weekend")
        i +=1

plt.plot(data["close"])

plt.title('Time series chart for ' + (stock))

plt.show()
"""
