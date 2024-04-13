# with open("weather_data.csv") as f:
#     contents = f.readlines()

# print(contents)
# import csv
# with open("weather_data.csv") as f:
#     contents = csv.reader(f)
#     temperature = []
#     for content in contents:
#         if content[1] != 'temp':
#             temperature.append(int(content[1]))
#     print(temperature)
import pandas as pd
data = pd.read_csv("weather_data.csv")
avg_temperature = data["temp"].mean()
print(avg_temperature)
max_temperature = data["temp"].max()
print(max_temperature)
print(data[data["temp"] == max_temperature])

def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32

data["fahrenheit"] = data["temp"].apply(celsius_to_fahrenheit)
print(data["fahrenheit"])