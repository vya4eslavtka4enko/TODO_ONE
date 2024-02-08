"""
    Coding Exercise 1
    Your task is to create a program that generates a random whole number. Here is how the program should behave:
    As you can see, the program first asks the user to enter a whole number. Then, once the user enters a number,
    the program asks the user again to enter another number.
    Then, the program returns a random number that falls between the two whole numbers. Here is another example:
"""
import random


def random_choise(max,min):
    list_list = range(min,max)
    return random.choice(list)

max = int(input("Enter max bound "))
min = int(input("Enter min bound "))

print(random_choise(max,min))
