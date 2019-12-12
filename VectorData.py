import numpy as np
from matplotlib import pyplot as plt
import pandas
import json
from urllib.request import urlopen

class VectorData:
    def __init__(self,filename=''):
        if(filename != ''):             #check if you want to use a document or the API
            self.file = open(filename,'r')
        self.data = []
        self.plot = False
        self.api = "JY8YMPVL6PY86RM6"  #API number selected for the account
        self.index =0

    def read_data(self):            #this function requires a document to be read in csv format
        for i,data in enumerate(self.file):
            if(i>0):
                self.data.append(float(data.split('","')[0]))
        if self.plot==True:
            self.plot_data(np.array(self.data))
        return np.array(self.data)

    def get_data(self,symbol = "MSFT",value = "close", times = "5",give_times = False): #acquire stock data from www.alphavantage.co
        ###
        # You are able to change var symbol to any stock market symbol
        # var value to: open, close, high,low,volume
        # var times has to: 1min, 5min, 15min, 30min, 60min
        # var give_times set to True to get the time and the desired value
        ###
        symbol_data = []
        ticks = []

        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="+symbol+"&interval="+times+"min&outputsize=full&apikey=" + self.api
        f = urlopen(url)

        txt = f.read().decode("utf-8")                              #reads and decodes the json api
        data = json.loads(txt)
        print(data["Meta Data"]['2. Symbol'])
        self.ticks = list(data["Time Series ("+times+"min)"].keys())  #gets the times of the stock values
        for item in data["Time Series ("+times+"min)"]:
            symbol_data.append(data["Time Series ("+times+"min)"][item]['1. open'])   #get the value of the stock
        if(give_times):
            return np.array(symbol_data[::-1]).astype(np.float), self.ticks[::-1]     #decide if you want the time along with values
        else:
            return np.array(symbol_data[::-1]).astype(np.float)                       #or the default of just the values


if __name__=='__main__':
    ###example use of the class
    vd = VectorData(filename='EUR_USD.csv')
    #vd.plot=True
    print(type(vd.read_data()))
    data = vd.get_data(symbol = "MSFT",value = "close",times = "1")
    print(data)

