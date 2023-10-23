with open(r"C:\Users\ahpar\Documents\100daysofPython\Day -25\weather_data.csv") as weather_data:
    data = weather_data.readlines()
    print(data)


import csv
with open(r"C:\Users\ahpar\Documents\100daysofPython\Day -25\weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []

    for row in data:
        if row[1] != "temp":

            temperatures.append(int(row[1]))

    print(temperatures)
            
import pandas as pd
data = pd.read_csv("Weather_data.csv")
print(type(data))
data["temp"]
print(data["temp"])
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
average = sum(temp_list)/len(temp_list)
print(average)
print(data["temp"].mean())
print(data["temp"].max())
print(temp_list)


print(data.condition)
# print(data["condition"]) #same as the uppper line 


#get the data from row

print(data[data.day == "Monday"])
max_temp = data['temp'].max()
print(data[data.temp == max_temp])
monday = data[data.day == "Monday"]
Temperature_Celsius = monday.temp
Temperature_Fahrenheit = (Temperature_Celsius* 9/5) + 32
print(Temperature_Fahrenheit)

#create a dataframe from scratch

