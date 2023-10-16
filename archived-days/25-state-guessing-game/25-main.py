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
# import pandas
#
# data = pandas.read_csv('weather_data.csv')
#
# # print(data)
# temp_list = data['temp'].to_list()
# temp_sum = 0
# for temp in temp_list:
#     temp_sum += temp
#
# print(f'{temp_sum / len(temp_list):0.2f}')
#
# print(data['temp'].max())
#
# print(data[data['temp'] == data['temp'].max()])
#
# print(data[data['day'] == 'Monday'].temp * 9/5 + 32)

# Part 3 - Squirrel Census Data
# import pandas
#
# data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# # for col in data.columns:
# #     print(col)
# color_list = data['Primary Fur Color'].to_list()
# black_cnt = len(data[data['Primary Fur Color'] == 'Black'])
# grey_cnt = len(data[data['Primary Fur Color'] == 'Gray'])
# cinn_cnt = len(data[data['Primary Fur Color'] == 'Cinnamon'])
#
#
# print(f'Black: {black_cnt}')
# print(f'Gray: {grey_cnt}')
# print(f'Cinnamon: {cinn_cnt}')
#
# df = pandas.DataFrame({"Fur Color": ["Black", "Gray", "Cinnamon"], "Count": [black_cnt, grey_cnt, cinn_cnt]})
# df.to_csv('squirrel_count.csv')

# Main Program - State Guessing Game
import turtle
import pandas

data = pandas.read_csv('50_states.csv')
data_list = data.values.tolist()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
# print(data_list)
score = 0
guessed_states = []
# writer.goto(x=guess['x'], y=guess['y'])
# writer.write(guess['state'])
while score < 51:
    answer = screen.textinput(title=f'{score}/50 Correct', prompt="What's another state's name?")
    if answer is None:
        score = 99
    elif answer.title() not in guessed_states:
        for row in data_list:
            if answer.title() in row:
                guessed_states.append(answer.title())
                writer.goto(x=row[1], y=row[2])
                writer.write(row[0])
                score += 1

screen.exitonclick()
