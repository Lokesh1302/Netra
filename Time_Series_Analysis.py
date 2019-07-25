# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 14:53:27 2019

@author: lodogga
"""

import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
import matplotlib

matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'

df = pd.read_excel("C://Users//lodogga//Downloads//Blink_Data.xlsx")
User = df.loc[df['Name'] == 'Lokesh']

User['Time'].min(), User['Time'].max()

User = User.sort_values('Time')
User.isnull().sum()
User = User.groupby('Time')['Blink'].sum().reset_index()

User = User.set_index('Time')
User.index

y = User['Blink'].resample('5min').mean()

y.plot(figsize=(5, 5))
plt.show()