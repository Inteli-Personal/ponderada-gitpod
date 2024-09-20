import pandas as pd
df = pd.read_csv("adult.data.csv", header=0, delimiter=",")
df = df.sort_values(by="hours-per-week", ascending=True).reset_index()
print(df["hours-per-week"][0])
