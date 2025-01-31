#Importing Libraries:

import pandas as pd
import numpy as np

#Reading CSV File:
url="laptops_test.csv"
df=pd.read_csv(url,header=None)
#print(df.head(10))


#Adding Headers:
headers=["Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core",
"Screen_Size_inch", "CPU_frequency", "RAM_GB", "Storage_GB_SSD", "Weight_kg", "Price_Euro", "Rating"]
df.columns=headers
#print(df.head(10))


#Replacing '?' with Nan:
df1=df.replace('?',np.nan)
print(df1.head(10))

"""
#Removing all rows having 'Nan':
df=df1.dropna(axis=0)
#print(df.head(10))
"""
"""
#Printing the datatypes of coloumns
#print(df.dtypes)
"""

#print(df.describe(include="all"))

#print(df.info())