import numpy as np
from scipy.signal import find_peaks_cwt

class Functions:

    def mean_average(self,x, N):
        out = np.zeros_like(x, dtype=np.float64)
        dim_len = x.shape[0]
        for i in range(dim_len):
            if N % 2 == 0:
                a, b = i - (N - 1) // 2, i + (N - 1) // 2 + 2
            else:
                a, b = i - (N - 1) // 2, i + (N - 1) // 2 + 1

            # cap indices to min and max indices
            a = max(0, a)
            b = min(dim_len, b)
            out[i] = np.mean(x[a:b])
        return out

    def MaxGetters(self,data,range):    #use scipy to get the mountains given a list of values
        indexes = find_peaks_cwt(-1*data, np.arange(1, range))
        return indexes

    def MinGetters(self,data,range):    #use scipy to get the valleys given a list of values
        indexes = find_peaks_cwt(data,np.arange(1,range))
        return indexes
