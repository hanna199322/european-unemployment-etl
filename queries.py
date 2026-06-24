import pandas as pd

fact_df = pd.read_csv("fact_table.csv")
country_df = pd.read_csv("countries_dimension.csv")
time_df = pd.read_csv("time_dimension.csv")
sex_df = pd.read_csv("sex_dimension.csv")
age_df = pd.read_csv("age_dimension.csv")
df = fact_df.merge(time_df, on="time_id")
df = df.merge(country_df, on="country_id")
df = df.merge(sex_df, on="sex_id")
df = df.merge(age_df, on="age_id")

print(df.head())
print(country_df.columns)
print(country_df.head())
print("FACT:")
print(fact_df.columns)

print()

print("COUNTRIES:")
print(country_df.columns)
df.to_csv("final_table.csv", index=False)

print("Done!")