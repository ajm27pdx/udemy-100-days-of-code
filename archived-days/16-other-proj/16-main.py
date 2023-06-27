# Part 1 - Turtle Graphics
# import turtle
#
# timmy = turtle.Turtle()
# timmy.shape('turtle')
# timmy.color('darkred')
# timmy.forward(100)
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# Part 2 - PrettyTable Library Import
# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
#
# table.align = "l"
#
# print(table)

# Project - OOP Coffee Machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

running = True
my_coffeemaker = CoffeeMaker()
my_menu = Menu()
my_moneymachine = MoneyMachine()
while running:
    choice = input("Make a selection: ")
    if choice == 'report':
        my_coffeemaker.report()
        my_moneymachine.report()
    else:
        order = my_menu.find_drink(choice)
        if my_coffeemaker.is_resource_sufficient(order):
            if my_moneymachine.make_payment(order.cost):
                my_coffeemaker.make_coffee(order)
