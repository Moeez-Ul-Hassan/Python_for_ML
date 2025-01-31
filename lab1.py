#    1---------Including the Libraries
import pandas as pd
import numpy as np
import os

#Reading the file
url="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df=pd.read_csv(url,header=None)

print('Here are the last 10 rows of the dataframe');
#print(df.tail(10));


#     2---------Adding Headers
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns= headers

#print(df.tail(10));


#     3---------Replacing "?" with NaN

df1=df.replace('?',np.nan)

#     4---------Dropping the  missing values

df=df1.dropna(subset=["price"],axis=0) #For dropping the Row having Nan,nan values corresponding to the following column
#df=df1.dropna(axis=0) #for dropping whole rows having Nan values
#df=df1.dropna(axis=1) #for dropping whole columns having Nan values

#print(df.head(20))



#      5---------Saving the file

path=r"D:\files"
file_path = os.path.join(path, "example.csv")

"""
try:
    df.to_csv(file_path, index=False)
    print(f"File saved successfully at: {file_path}")
except PermissionError:
    print("Permission denied. Please check file permissions or close the file if it's open elsewhere.")

"""
#      6---------Data Types

#print(df.dtypes)

#      7---------Description
#print(df.describe())
#print(df.describe(include="all"))

#      8---------Info
#print(df.info())

#      9---------Datatype changing 
df["symboling"]=df["symboling"].astype(float)
print(df.dtypes)

