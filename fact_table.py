import pandas as pd

df = pd.read_csv("countries.csv")

df.columns = ["country_code", "country"]

df.insert(0, "country_id", range(len(df)))

df.to_csv("countries_dimension.csv", index=False)

print(df.head())