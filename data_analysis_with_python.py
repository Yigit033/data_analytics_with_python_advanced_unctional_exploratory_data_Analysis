
import numpy as np


"""fonksiyonun "#" ile yorum satiri olmasi lazim"""

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10


"""a = [[5,1],[1,3]]
b = [12,10]


solve = np.linalg.solve(a,b)

print(solve)"""


###################33

import pandas as pd
import seaborn as sns

"""pandas_series = pd.Series([1,3,5,7,9])

print(type(pandas_series))"""



"""df = pd.read_csv("datasets/advertising.csv")


print(df.head(10))
print(df.info())
"""


"""df1 = sns.load_dataset("titanic")
"""
"""print(df1["age"].mean())
print(df1.isnull().values.any())
print(df1.isnull().sum())
print(df1["sex"].value_counts())
"""

"""print(df1["age"])"""

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")

print(df.head())

print(df["age"].mean())

## Bu iki kullanımdan aşağıdaki çok daha önemli çünkü bir gurup için mesela sex(cinsiyet) için age(yaş) parametresinin birden fazla özelliğini gösterebiliyoruz mesela toplamı, ortalamaları, büyüklükleri gibi!!!
print(df.groupby("sex")["age"].mean())
print(df.groupby("sex").agg({"age":["mean", "sum", "size", "count"]}))

print(df.groupby("sex").agg({"age": ["mean", "sum", "size", "count"], "embark_town": "count", "survived": "mean", "alive": "count"}))


