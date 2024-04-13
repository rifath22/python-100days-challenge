import pandas as pd

data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


df = data.groupby(["Primary Fur Color"])["Primary Fur Color"].count()
df1= df.to_frame().rename(columns={'Primary Fur Color':'Count'}).reset_index()
df1.rename(columns={'Primary Fur Color': 'Fur Color', 'Count': 'Count'}, inplace=True)
print(df1)
df1.to_csv("squirrel_count.csv")