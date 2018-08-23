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


#Lists
# friends = ["Pari","Nilyo","Ishudi","Ghugal","Bhau"]
# friends[4] = "Niha"
# print(friends[-1])
# print(friends[1])
# print(friends[1:])
# print(friends[2:4])


#Lists function

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


#Tuples

# You can't change value of tuple and it's notify by round bracket (). We use tuple when data not gonna be change.

# coordinates = (4, 5)
# coordinates = [(4, 5), (6, 7), (58, 76), (90, 45)]
# print(coordinates[1])


#Functions

# def sayhi(name, age):
#     print("Hello " + name + ", you are " + str(age))
#
# sayhi("Mahi", 26)
# sayhi("Moksh", 27)


#Return Statement

# def cube(num):
#     return num*num*num
#
# result = cube(5)
# print(result)


#If statement

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


#Building a better calculator

