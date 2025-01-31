import pandas as pd # type: ignore

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url, header=None)

print(df.head(5))
path="C:\Users\Admin\OneDrive - FAST National University\Desktop\SEMESTER 6\Python_for_ML"
df.to_csv(path)