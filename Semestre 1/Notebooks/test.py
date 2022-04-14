import pandas as pan

from sklearn.model_selection import train_test_split

df = pan.read_csv( 'trdAll.csv')
a = df.loc[:, "TRD21"]
b = df.loc[:, "TRD22"]
x = list(zip(a, b))
y = df.loc[:, "species"]
df.head()

