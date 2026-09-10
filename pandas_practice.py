import pandas as pd

CSV_PATH = r"C:\Users\Administrator\Desktop\python_practise\data.csv"
df= pd.read_csv(CSV_PATH)
# print(df)

# print(df.loc[df["salary"] >37000])

# print(df.loc[df['salary'] > 50000])

# print(df.loc[(df["age"] > 21) & (df["age"]< 54 )])

# print(df["salary"].sum())

# print(df['salary'].mean())

# print(df['salary'].max())

# print(df['salary'].min())

# print(df['name'])

# print(df[["salary","name"]])

# print(df.loc[df["age"] > 21])

# print(df.loc[df["salary"] >50000 ])

# print(df.iloc[:2])