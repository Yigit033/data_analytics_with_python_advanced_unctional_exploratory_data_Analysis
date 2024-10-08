
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt



pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = pd.read_csv("datasets/breast_cancer.csv")
df = df.iloc[:, 1:-1]
# print(df.head(10))



numeric_col = [col for col in df.columns if df[col].dtype in [int, float]]


# print(numeric_col)

corr = df[numeric_col].corr()

# print(corr)




sns.set(rc={"figure.figsize": (12, 12)})
sns.heatmap(corr, cmap="RdBu")
# plt.show()



######################
# Yüksek korelasyonlu değişkenlerin çıkarılması
######################

cor_matrix = df[corr].abs()
# abs() mutlak değere çevirir!!!


# print(df.head(10))


upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool)) 



print(upper_triangle_matrix)




drop_colums_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > 0.90 )]

dropped_df = df.drop(drop_colums_list, axis = 1)


# print(dropped_df.head(10))


print(drop_colums_list)




























