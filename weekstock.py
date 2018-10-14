from iexfinance import *
from datetime import *
import matplotlib.pyplot as plt
import requests
import pandas
import json
import algorithm
import random
import numpy


while True:

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
      p = 7
    if (period == "month"):
      start = lastmonth
      p = 30
    if (period == "year"):
      start = lastyear
      p = 365
    end = today

    data = get_historical_data(stock, datetime(2015, 1, 1), end, output_format='pandas')
    print(data)
    a = type(data)
    print(a)

    data = data.values.tolist()
    datalist = []
    for i in range(len(data[0])):
        datalist.append([])
    for i in range(len(datalist)):
        for j in range(len(data)):
            datalist[i].append(0)
    for i in range(len(datalist)):
        for j in range(len(datalist[i])):
            datalist[i][j]=data[j][i]
    print(datalist[3])
    predictiondata = algorithm.projections(datalist[3], p)
    #print(datalist)
    print(predictiondata)

    i = 0
    k = 0
    for i in range(len(datalist[3])):
        j = (date.today() - timedelta(i)).weekday()
        if j == 5 or j == 6:
            #print(i)
            datalist[3][i]=-1
            k+=1
            
    for j in range(k):
        datalist[3].remove(-1)

    concatlist = datalist[3] + predictiondata
    plt.plot(concatlist)

    plt.title('Time Series Chart For ' + (stock))
    plt.show()
    
    userquit = input("Type quit to exit the program")
    if userquit.lower() == ("quit"):
        break

exit()

