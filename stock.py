import iexfinance
from datetime import datetime
import matplotlib.pyplot as plt
import requests
import pandas
import json

start = datetime(2017, 2, 9)

end = datetime(2017, 5, 24)

f = get_historical_data("AAPL", start, end, output_format='pandas')

plt.plot(f["close"])

plt.title('Time series chart for AAPL')

plt.show()
