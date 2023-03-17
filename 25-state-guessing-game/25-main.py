# Part 1
#import csv
# with open('weather_data.csv', mode='r') as f:
#     names = f.readlines()
#
# print(data[2])
# with open('weather_data.csv', mode='r') as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
# print(temperatures)

# Part 2
import pandas

data = pandas.read_csv('weather_data.csv')

print(data)
print(data['temp'])
