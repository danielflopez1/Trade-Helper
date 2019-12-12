import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import Functions as FN
import VectorData
from scipy.signal import find_peaks_cwt
class TradingStrategy:
    def __init__(self):
        self.peak_window = 20
        vd = VectorData.VectorData()
        data = vd.get_data(symbol = "MSFT",value = "close",times = "1")  #aquire stock data
        data = data[len(data)-200:]                             #total data takes a long time so it is cut to the last 200 stock values
        partial_data =[]
        for i,value in enumerate(data):
            partial_data.append(value)
            if(i<10):continue
            max_indexes = []
            min_indexes = []
            for x_window in range(3, 10, 1): #make sure the hills and valleys are reiterated over multiple moving averages
                meanavg = FN.Functions.mean_average(FN,np.array(partial_data),x_window)
                max_indexes = max_indexes+ list(FN.Functions.MaxGetters(FN,meanavg,x_window))
                min_indexes = min_indexes + list(FN.Functions.MinGetters(FN, meanavg, x_window))

        total_min_indexes = sorted(min_indexes)         # get the mountains and valleys in the stock values
        total_max_indexes = sorted(max_indexes)
        #final_min_index = []
        #final_max_index = []
                                                        #secure the values taken are not noise of local minimas
        mod_number = 5
        mod_val = 4
        for i,index in enumerate(total_min_indexes[:-mod_number]):
            if(all(total_min_indexes[i:i+mod_number]>=index) and all(total_min_indexes[i:i+mod_number]<=index+mod_val)):
                #final_min_index.append(np.mean(total_min_indexes[i:i + mod_number]))  #get the mountain and valley data
                plt.axvline(x=np.mean(total_min_indexes[i:i + mod_number]), color='b') #show the data in plot
        for j, index in enumerate(total_max_indexes):
            if (all(total_max_indexes[i:i + mod_number] >= index) and all(total_max_indexes[i:i + mod_number] <= index + mod_val)):
                #final_max_index.append(np.mean(total_min_indexes[i:i + mod_number]))
                plt.axvline(x=np.mean(total_min_indexes[i:i + mod_number]), color='r')
            '''
        for i, xc in enumerate(final_max_index):
            plt.axvline(x=xc, color='r')

        for i, xc in enumerate(final_min_index):
            plt.axvline(x=xc, color='b')
        
        segments = {0.91: [(0, 500),
                        (915, 1000)],
                    0.92: [(0, 250),
                        (500, 1000)]}

        colors = {0.91: 'g', 0.92: 'r'}


        for y in segments:
            col = colors.get(y, 'k')
            for seg in segments[y]:
                plt.plot(seg, [y, y], color=col)
        # plt.plot(indexes,np.arange(1,len(data)))
        '''

        #print(max_indexes,min_indexes)
        plt.plot(data, color='k')  #show the data in black
        plt.plot(meanavg, color='g') #show moving average in green
        plt.show()


if __name__=='__main__':
    ts = TradingStrategy()
