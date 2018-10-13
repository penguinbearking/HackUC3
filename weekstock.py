from iexfinance import *
from datetime import *
import matplotlib.pyplot as plt
import requests
import pandas
import json


while True:
    userquit = input("Type quit to exit the program")
    if userquit.lower() == ("quit"):
        break
    
    stock = input("Enter your ticker symbol: " )


    today = date.today()
    lastweek = date.today() - timedelta(7)

    print(lastweek)
    print(today)

    lastmonth = date.today() - timedelta(30)
    lastyear = date.today() - timedelta(365)

    period = input("Enter time period: (week, month, and year)")
    if (period == "week"):
      start = lastweek
    if (period == "month"):
      start = lastmonth
    if (period == "year"):
      start = lastyear
    end = today

    data = get_historical_data(stock, start, end, output_format='pandas')
    a = type(data)
    print(a)

    datalist = data.values.tolist()
    print(datalist)

    i = 0
    for i in range(len(datalist[4])):
        j = (date.today() - timedelta(i)).weekday()
        if j == 5 or j == 6:
            datalist[4].pop(i)
            print ("weekend")
            i +=1

    plt.plot(data["close"])

    plt.title('Time series chart for ' + (stock))

    plt.show()

exit()
