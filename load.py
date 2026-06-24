import pandas as pd
from database import db

time_df = pd.read_csv("time_dimension.csv")
countries_df = pd.read_csv("countries_dimension.csv")
sex_df = pd.read_csv("sex_dimension.csv")
age_df = pd.read_csv("age_dimension.csv")
fact_df = pd.read_csv("fact_table.csv")

# Очистить коллекции
db.time_dimension.delete_many({})
db.countries_dimension.delete_many({})
db.sex_dimension.delete_many({})
db.age_dimension.delete_many({})
db.fact_table.delete_many({})

# Загрузить данные
db.time_dimension.insert_many(time_df.to_dict("records"))
db.countries_dimension.insert_many(countries_df.to_dict("records"))
db.sex_dimension.insert_many(sex_df.to_dict("records"))
db.age_dimension.insert_many(age_df.to_dict("records"))
db.fact_table.insert_many(fact_df.to_dict("records"))

print("Data loaded successfully!")