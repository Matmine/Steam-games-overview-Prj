import pandas as pd

df = pd.read_csv('steam_data_mathis.csv')
df = df.sort_values(by='Current Players', ascending=False)

print(df)
