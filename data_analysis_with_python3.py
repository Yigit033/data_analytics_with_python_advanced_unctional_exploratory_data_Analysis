


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head(10)
df.info()


# docstring içindeki yazılar 3 tırnak ("""""")işareti ile yazdıklarımıza denir
# docstring içindeki yazılar fonksiyonun ne işe yaradığını anlatır. Eğer başkası bizim fonksiyonumuzu kullanacaksa docstring içindeki yazıları okuyarak fonksiyonu nasıl kullanacağını anlar.

def grab_col_names(dataframe, cat_th=10, car_th=20):
    """
    Veri setindeki katagorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.
    
    
    Parameters
    ------
    dataframe: dataframe
    cat_th: int, float
        numerik fakat katagorik olan değişkenler için sınıf eşik değeri
    car_th: int, float
        katagorik fakat kardinal olan değişkenler için sınıf eşik değeri

    Returns
    -------
    cat_cols: list
        Kategorik değişken listesi
    num_cols: list
        Numerik değişken listesi
    cat_but_car: list
        Kategorik görünümlü kardinal değişken listesi

    Notes
    -------
    cat_cols + num_cols + cat_but_car = toplam değişken sayısı
    num_but_cat cat_cols'un içersinde.
    Retrun olan 3 liste toplamı toplam değişken sayısına eşittir: cat_cols + num_cols 





    """



    


    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["object", "category", "bool"]]
    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
    cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in df.columns if col not in cat_but_car]


    num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]


    print(f"Observations: {df.shape[0]}")
    print(f"Variables: {df.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f"num_but_cat: {len(num_but_cat)}")
    print(cat_cols, num_cols, cat_but_car)


    return cat_cols, num_cols, cat_but_car




cat_cols, num_cols, cat_but_car = grab_col_names(df)


def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),"Ratio": 100 * dataframe[col_name].value_counts() /len(dataframe)}))
    print("##########################################")


cat_summary(df, "sex")


for col in cat_cols:
    cat_summary(df, col)




def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)



    if plot:
        sns.histplot(dataframe[numerical_col])
        plt.xlabel(numerical_col)
        plt.ylabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


for col in num_cols:
    num_summary(df, col, plot=True)



#bonus:

df = sns.load_dataset("titanic")


for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)


cat_cols, num_cols, cat_but_car = grab_col_names(df)




































89