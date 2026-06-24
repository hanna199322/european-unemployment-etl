import requests

url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/une_rt_m"

data = requests.get(url).json()

print(data["dimension"]["time"]["category"]["index"]["2025-01"])
print(data["dimension"]["time"]["category"]["index"]["2025-12"])

print(data["dimension"]["geo"]["category"]["index"]["DE"])
print(data["dimension"]["geo"]["category"]["index"]["FR"])
print(data["dimension"]["geo"]["category"]["index"]["IT"])
print(data["dimension"]["geo"]["category"]["index"]["ES"])
print(data["dimension"]["geo"]["category"]["index"]["NL"])