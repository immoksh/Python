# from math import *

# print("hell world")

# print("/___|")
# print("   /|")
# print("  / |")
# print(" /  |")

# character_name = "Tom"
# character_age = "60"
# is_male = True
# print("There once was a man named " + character_name + ", ")
# print("he was " + character_age + " years old. ")
#
# character_name = "Mike"
# print("He really liked the name " + character_name + ", ")
# print("but didn't like being " + character_age + ".")

# print("Setu\nModi")
# print("Setu\"Modi")

# phrase = "Setu Modi"
# print(phrase.upper().isupper())
# print(len(phrase))


# my_num = -6
# print(abs(my_num))
# print(pow(4, 2))
# print(sqrt(64))

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age)

# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = int(num1) + float(num2)
# print(result)


# color = input("Enter a color: ")
# plural_noun = input("Enter a Plural noun: ")
# celebrity = input("Enter a celebrity: ")
#
#
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

# friends = ["Parag", "Nishad", "Nilesh"]


# Lists
# friends = ["Pari","Nilyo","Ishudi","Ghugal","Bhau"]
# friends[4] = "Niha"
# print(friends[-1])
# print(friends[1])
# print(friends[1:])
# print(friends[2:4])


# Lists function

# lucky_numbers = [42,8,14,21,41,50]
# friends = ["Pari","Nilyo","Nilyo","Ishudi","Ghugal","Bhau"]
# friends.extend(lucky_numbers)
# friends.append("Sharma")
# friends.insert(2, "Sharma")
# friends.remove("Ishudi")
# friends.clear()
# friends.pop()
# friends.sort()
# lucky_numbers.reverse()
# print(lucky_numbers)
# friends2 = friends.copy()
# print(friends)
# print(friends2)
# print(friends.index("Ghugal"))
# print(friends.count("Nilyo"))


# Tuples

# You can't change value of tuple and it's notify by round bracket (). We use tuple when data not gonna be change.

# coordinates = (4, 5)
# coordinates = [(4, 5), (6, 7), (58, 76), (90, 45)]
# print(coordinates[1])


# Functions

# def sayhi(name, age):
#     print("Hello " + name + ", you are " + str(age))
#
# sayhi("Mahi", 26)
# sayhi("Moksh", 27)


# Return Statement

# def cube(num):
#     return num*num*num
#
# result = cube(5)
# print(result)


# If statement

# is_male = True
# is_tall = False
#
# if is_male or is_tall:
#     print("You are a male or tall or both")
# else:
#     print("You are neither male nor tall")


# is_male = True
# is_tall = True
#
# if is_male and is_tall:
#     print("You are a tall male")
# elif is_male and not (is_tall):
#     print("You are a short male")
# elif not(is_male) and is_tall:
#     print("You are not a male but are tall")
# else:
#     print("You are not a male and not tall")


# If statements & comparisons

# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
# print(max_num(580, 51, 78))


# Building a better calculator

# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
#
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator")


# Dictionary

# monthConversion = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December"
# }
#
# print(monthConversion["Feb"])
# print(monthConversion.get("asd", "Not a valid key"))


# While loop

# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#
# print("Done with loop")


# Building a guessing game

# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
# print("The word is belongs to name of animal")
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
# if out_of_guesses:
#     print("Out of Guesses, YOU LOSE!")
# else:
#     print("You win!")


# For loop

# for letter in "Setu Modi":
#     print(letter)

# friends = ["Pari", "Nilyo", "Shani"]
# for friend in friends:
#     print(friend)
# for index in range(len(friends)):
#     print(friends[index])

# for index in range(5, 13):
#     print(index)

# for index in range(5):
#     if index == 0:
#         print("First Iteration")
#     else:
#         print("Not first")


# Exponent function

# print(3**4)
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
#
# print(raise_to_power(4, 3))


# 2D lists & nested loops

# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]

# print(number_grid[2][0])

# for row in number_grid:
#     for col in row:
#         print(col)


# Build a translator

# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "S"
#             else:
#                 translation = translation + "s"
#         else:
#             translation = translation + letter
#     return translation
#
#
# print(translate(input("Enter a phrase: ")))


# Comments

# '''
# It's also a comment
# which will not give error
# '''

# This prints out a string
# print("Comments are fun")


# Try / Except

# try:
#     value = 10/0
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("Invalid input")


# Reading files

# employee_file = open("employees.txt", "r")

# print(employee_file.readable())  # give response in true - false,
# print(employee_file.read())  # read whole file
# print(employee_file.readline())  # read line
# print(employee_file.readlines())  # read lines
# print(employee_file.readlines())  # read lines

# for employee in employee_file.readlines():
#     print(employee)

# employee_file.close()


# Writing to files

# append data from last line when mode is "a"
# but if we use "w" mode then it will remove old data and write from 1st line

# employee_file = open("employees.txt", "a")
#
# employee_file.write("\nShraddha - hr")
#
# employee_file.close()


# employee_file = open("index.html", "w")
#
# employee_file.write("<p>This is HTML</p>")
#
# employee_file.close()


# Modules and pip

import useful_stuff

print(useful_stuff.roll_dice(10))