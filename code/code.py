


import pandas as pd
import numpy as np

df = pd.read_csv("./data/output.csv")
## explore the data
df.describe()
print(df.head())
print(df.columns)
print(df.info())
null_counts = df.isnull().sum()
print(null_counts)

#evaluate str data sample
for col in df.columns:
    if df[col].dtype == 'str':
        print(f"Column: {col}")
        print(df[col].unique())
        print("\n")

# change Feature4 dtype to graded categorical 
order4 = ['A', 'B', 'C', 'D']
df['Feature4'] = pd.Categorical(df['Feature4'], categories=order4, ordered=True)
# check if the change was successful
print(df['Feature4'].dtype)

# change Feature19 dtype to graded categorical 
order19 = ['Low', 'Medium', 'High']
df['Feature19'] = pd.Categorical(df['Feature19'], categories=order19, ordered=True)
# check if the change was successful
print(df['Feature19'].dtype)

# %%
# visualize the distribution of Feature4 and Feature19
import matplotlib.pyplot as plt
print(df.iloc[:, 3])
values = df.iloc[:, 3].value_counts().sort_index()
print(values)
values.plot.bar(title='Distribution of Feature4')
values.plot(kind='bar', title='Distribution of Feature4')
plt.show()
