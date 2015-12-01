import pandas as pd
#import pandas.io.data as iod
from pandas_datareader import data
#Also import numpy and matplotlib. Because ....
print(pd.__version__)
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp

data_frame = pd.read_csv('aapl.csv')
print(data_frame)
