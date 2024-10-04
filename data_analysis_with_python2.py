import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

df = sns.load_dataset("titanic")


# print(df.head())


"""isnull = df.isnull().values.any()

print(isnull)

print(df.isnull().sum())
"""


def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

# check_df(df)




# print(df.info())





"""
print(cat_cols)


print(str(df["sex"].dtypes) in ["object"])
"""






# print(df.head(10))

# print(df[cat_cols].nunique())



def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),"Ratio": 100 * dataframe[col_name].value_counts() /len(dataframe)}))
    print("##########################################")


# cat_summary(df, "age")

# print(df.head(5))


"""for col in cat_cols:
    print(cat_summary(df, col))
"""


"""def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),"Ratio": 100 * dataframe[col_name].value_counts() /len(dataframe)}))
    print("##########################################")

    
    if df[col_name].dtypes == bool:
        pass
    else:
        if plot:
            sns.countplot(x=dataframe[col_name], )
            plt.show(block=True)
        





cat_summary(df, "sex", plot = True)


for col in cat_cols:
        print(cat_summary(df, col, plot = True))"""






# print(df.describe().T)



selected_col = [col for col in df.columns if df[col].dtypes in ["int", "float"]]


# print(selected_col)


# print(df[["age","fare"]].describe().T)



# print(df[["age","fare"]].info())


cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["object", "category", "bool"]]


num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]

# print(num_but_cat)


cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["object", "category"]]
cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in df.columns if col not in cat_but_car]



# print(df[["age", "fare"]].describe().T)

num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]

# print(numeric_col)

num_cols = [col for col in num_cols if col not in cat_cols]

"""print(num_cols)
print(cat_cols)
print(cat_but_car)"""



def num_summary(dataframe, numerical_col):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)
    print("##########################################")


# num_summary(df, "age")



for col in num_cols:
    print(num_summary(df, col))






def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)



    if plot:
        sns.histplot(dataframe[numerical_col])
        plt.xlabel(numerical_col)
        plt.ylabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


num_summary(df, "age", plot=True)


for col in num_cols:
    print(num_summary(df, col, plot=True))



def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),"Ratio": 100 * dataframe[col_name].value_counts() /len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], )
        plt.show(block=True)

for col in cat_cols:
    print(cat_summary(df, col, plot=True))



















    