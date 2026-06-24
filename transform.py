import requests
import pandas as pd

url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/une_rt_m"

data = requests.get(url).json()

countries = data["dimension"]["geo"]["category"]["label"]
months = data["dimension"]["time"]["category"]["label"]

df_countries = pd.DataFrame(
    countries.items(),
    columns=["Country_Code", "Country"]
)

df_months = pd.DataFrame(
    months.items(),
    columns=["Month_ID", "Month"]
)

df_countries.to_csv("countries.csv", index=False)
df_months.to_csv("months.csv", index=False)

print("Files created:")
print("countries.csv")
print("months.csv")