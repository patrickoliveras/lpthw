from orders import *
from people import *
from random import randint, choice
from textwrap import dedent
from food import *
import os

class Engine(object):

    total_turns = 60
    current_turn = 0
    money = 0
    backlog = {}

    classmates = {
        'Sandy':    Classmate('Sandy'),
        'Josh':     Classmate('Josh'),
        'Gus':      Classmate('Gus'),
        'Katy':     Classmate('Katy'),
        'Karla':    Classmate('Karla'),
        'Antonio':  Classmate('Antonio'),
        'Richy':    Classmate('Richy'),
        'Stimpy':   Classmate('Stimpy'),
    }

    menu = {
        'a': 'Sandwich',
        'b': 'Juice Box',
        'c': 'Warm Milk',
        'd': 'Muffin',
        'e': 'Chips',
        'f': 'Soda',
    }

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while self.current_turn < self.total_turns:
            print("\n" * 2, "-" * 20, sep="")

            self.status()

            print(dedent("""
                What do you want to do?
                1. Look for a customer.
                2. Order food.
                3. Deliver food.
                """), end="")

            options = ['1','2','3']
            student_finds_you = True
            student = self.classmates['Sandy'].name

            if student_finds_you:
                print(f"4. Take {student}'s order.")
                options.append('4')

            option = self.option_query(options, text)

            if not action.isnumeric():
                print("What?")

            elif int(action) == 1:
                self.clear_and_break()
                self.search_for_student()
                turns_used = 1
                break

            elif int(action) == 2:
                self.clear_and_break()
                turns_used = self.order_food()
                break

            elif int(action) == 3:
                self.clear_and_break()
                self.deliver_food()
                break

            else:
                print("I can't believe you've done this.")

            self.current_turn += turns_used


    def search_for_student(self):
        print("You wander around school a bit looking for customers. ", end="")

        found = randint(0,1)

        if not found == 1:
            print("But you only get weird looks.")
            return

        classmate = self.classmates[choice(list(self.classmates.keys()))]

        print(dedent(f"You meet {classmate.name}"), end="")

        if not classmate.name in self.backlog:
            food = Food(choice(list(self.menu.keys())))
            order = Order(food)

            self.backlog[classmate.name] = order

            print(f", who wants {self.menu[food.name]}. \n\tOrder added!")

        else:
            print(", who already has an order with you.")


    def order_food(self):
        if len(self.backlog.items()) == 0:
            print("First find some orders to fulfill, ya numbnuts")
            return 0

        print("Where do you want to go?")
        print(dedent("""
            1. Dona Maria's
            2. School Cafeteria
            3. Posh McGuire's Sautees and Coffee
            4. Jims Over The Fence Food Friends
            5. Tim's House
        """))

        option = self.option_query(["1","2","3","4","5"], 'What?')


        return 1


    def deliver_food(self):
        pass

    def take_order(self):
        pass


# GAME PRINTING FUNCTIONS


    def status(self):
        print(dedent(f"""

        Turns left:\t{self.total_turns - self.current_turn}
        Money:\t\t${self.money}
        """))

        self.list_orders()

        print("\n" * 2)


    def list_orders(self):
        self.table_cap()
        print(self.line(self.fill())        , sep="")
        print(self.line(self.fill("ORDERS")), sep="")
        print(self.line(self.fill())        , sep="")

        if len(self.backlog.items()) == 0:
            print(self.line(self.fill("  None")), sep="")

        for key, order in self.backlog.items():
            print(self.line(self.fill(self.tab(key,self.menu[order.food.name]))), sep="")

        print(self.line(self.fill())      , sep="")
        self.table_cap()




# MISC PRINTING FUNCTIONS

    def fill(self, string=""):
        return string + (" " * ((50-1)-len(string)))


    def tab(self, key, string):
        return f"{key}:" + (" " * (12 - (len(key)))) + string


    def line(self, string):
        return "| " + string + " |"


    def table_cap(self):
        print("+", "-" * (50+1), "+", sep="")


    def clear_and_break(self):
        os.system('cls||clear')
        print("-" * 20)
        print("\n")

    def option_query(self, options, text):
        option = None

        while not option in options:
            option = input("> ")

            if not option in options:
                print(text)

        return option
