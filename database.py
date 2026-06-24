from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["european_unemployment"]

fact_table = db["fact_table"]
countries_dimension = db["countries_dimension"]
time_dimension = db["time_dimension"]
sex_dimension = db["sex_dimension"]
age_dimension = db["age_dimension"]

print("Connected successfully!")