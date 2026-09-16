import pandas as pd

# CSV_PATH = r"C:\Users\Administrator\Desktop\python_practise\data.csv"
# df= pd.read_csv(CSV_PATH)
# # print(df)

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


CSV_PATH = r"C:\Users\Administrator\Desktop\python_practise\data.csv"
df = pd.read_csv(CSV_PATH)
# print(df)
# print(df.columns)
# print(df[df['Department'] == 'IT'])
# print(df["Salary"])
# print(df)
# print(df.sort_index())

# print(df.sort_values(by='Salary',ascending=True))

# df['Age']= df['Age'].replace('Missing',0)
# df['Age'] = df['Age'].astype('float')
# print(df['Age'].mean())

# print(df.dtypes)
# print(df["Salary"])
# df['Salary'] =pd.to_numeric(df['Salary'],errors='coerce')
# print(df['Salary'].mean())
# print(df)
# print(df.drop(columns='Experience'))
# print(df.drop_duplicates())
# print(df['Age'].mean().round(2))
# df['Salary'] =pd.to_numeric(df['Salary'],errors='coerce')
# print(df.loc[df['Salary'] >25000])
# print(df.sort_values(by='Salary',ascending=False))
# print(df.isna().sum())
# df.dropna(inplace=True)
# print(df)
# print(df.fillna(0))
# print(df[df.duplicated()])
