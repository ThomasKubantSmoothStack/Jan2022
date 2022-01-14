# Assignment 1 "Create a function func() which prints a text ‘Hello World’"
from hashlib import new


def func():
    print("Hello World")

# Assignment 2 "Create a function which func1(name)  which takes a value name and prints the output “Hi My name is Google’"
def func1(name):
    print(f"Hi my name is {name}")
# Assignment 3 "Define a function func3(x,y,z) that takes three arguments x,y,z where z is true it will return x and when z is false it should return y."
def func3(x, y, z):
    if z:
        return x
    else:
        return y

# Assignment 4 "define a function func4(x,y) which returns the product of both the values."
def func4(x, y):
    return x*y

# Assignment 5 "define a function called as is_even that takes one argument , which returns true when even values is passed and false if it is not."
def is_even(val):
    if val % 2 == 0:
        return True
    else:
        return False

# Assignment 6 "define a function that takes two arguments ,and returns true if the first value is greater than the second value and returns false if it is less than or equal to the second."
def greater_than_check(x, y):
    if x > y:
        return True
    else:
        return False

# Assignment 7 "Define a function which takes arbitrary number of arguments and returns the sum of the arguments."
def adder(*args):
    return sum(args)

# Assignment 8 "Define a function which takes arbitrary number of arguments and returns a list containing only the arguments that are even."
def even_list(*args):
    return list(filter(lambda x: x % 2 == 0, args ))

# Assignment 9 "Define a function that takes a string and returns a matching string where every even letter is uppercase and every odd letter is lowercase"
def alternate_casing(s):
    result = [letter.upper() if not i % 2 else letter.lower() for i, letter in enumerate(s)]
    result = "".join(result)
    return result

# Assignment 10 "Write a function which gives lesser of a given numbers if both the numbers are even, but returns greater if one or both or odd."
def func6(x, y):
    if (x + y) % 2 == 0:
        return min(x, y)
    else:
        return max(x, y)

# Assignment 11 "Write a function which takes  two-strings and returns true if both the strings start with the same letter."
def first_letter(s1, s2):
    if s1[0].lower() == s2[0].lower():
        return True
    else:
        return False

# Assignment 12 "Given a value,return a value which is twice as far as other side of 7"
def square(x):
    return x**2

# Assignment 13 "A function that capitalizes first and fourth character of a word in a string."
def capitalizer(s):
    result = list(s)
    result[0] = result[0].upper()
    result[3] = result[3].upper()
    return ''.join(result)

# START OF DAY_4_B
book_shop_list = [
    [34587, "Learning Python, Mark Lutz", 4, 40.95],
    [98762, "Programming Python, Mark Lutz", 5, 56.80], 
    [77226, "Head First Python, Paul Barry", 3, 32.95], 
    [88112, "Einführung in Python3, Bernd Klein", 3, 24.99]
]

new_list = list(map(lambda x: (x[0], x[2], x[3] + 10 if x[2] * x[3] <= 100 else x[3])  , book_shop_list))

print(new_list)

new_book_shop_list = [
    [34587, ("Learning Python, Mark Lutz", 4, 40.95)],
    [98762, ("Programming Python, Mark Lutz", 5, 56.80)], 
    [77226, ("Head First Python, Paul Barry", 3, 32.95)], 
    [88112, ("Einführung in Python3, Bernd Klein", 3, 24.99)]
]

new_new_list = list(map(lambda x: (x[0], (x[1][1] * x[1][2]) + (10 if x[1][1] * x[1][2] <= 100 else 0)), new_book_shop_list))

print(new_new_list)