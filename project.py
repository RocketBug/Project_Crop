import pandas as pd
import numpy as np
import statistics
from matplotlib import pyplot as plt

plt.style.use('seaborn')


df = pd.read_csv('apy.csv')

df = df[df['Production'] != '=']
convert_dict = {'Production':float}
df = df.astype(convert_dict)


cond = df['State_Name'] == 'Andhra Pradesh' 
cond1 = df['District_Name'] == 'ANANTAPUR'
cond2 = df['Crop'] == 'Rice'
cond3 = df['Crop_Year'] == 1997
cond4 = df['Season'] == "Rabi       "
cond5 = df['Season'] == "Kharif     "

y_prod_rabi = list(df.loc[cond & cond1 & cond2 & cond4, 'Production'])

x_year = list(df.loc[cond & cond1 & cond2 & cond4, 'Crop_Year'])
plt.xticks(np.arange(1997, 2014, 1))

plt.plot(x_year, y_prod_rabi)
plt.show()