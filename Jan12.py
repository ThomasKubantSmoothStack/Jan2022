# Assignment 1 "Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included). Go to the editor"
from lib2to3.pytree import convert
import random
from tracemalloc import start


answers = []
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        answers.append(i)
print(answers)

# Assignment 2 "Write a Python program to convert temperatures to and from celsius, fahrenheit"
def temp_converter():
    conversion_type = input("Input starting temperature unit: (F or C)").upper()
    starting_temp = input("Input temperature to be converted")
    if type(starting_temp) == int or type(starting_temp) == float:
        if conversion_type == "F":
            result = ((starting_temp - 32) * 5) / 9
        elif conversion_type == "C":
            result = ((starting_temp * 1.8) + 32)
        else:
            print("Temperature unit isn't valid, please input 'F' or 'C'")
    else:
        print("Temperature inputted is not a number")
    print(result)

# Assignment 3 "Write a Python program to guess a number between 1 to 9"
def random_number_guesser():
    random_number = random.randint(1, 9)
    correct = False
    while not correct:
        user_guess = int(input("Guess a number between 1 and 9: "))
        if user_guess == random_number:
            correct = True
        else:
            print("Your guess is incorrect. Try again!")
    print("Well guessed!")

# Assignment 4 "Write a Python program to construct the following pattern, using a nested for loop."
def triangle():
    for i in range(0, 5):  
        for j in range(0, i):  
            print("*", end=' ')   
        print(" ")  
    for i in range(5 + 1, 0, -1):  
        for j in range(0, i - 1):  
            print("*", end=' ')  
        print(" ")  
# triangle()
        
# Assignment 5 "Write a Python program that accepts a word from the user and reverse it"
def reverse_word():
    word = input("Input a word to reverse it: ")
    print(word[::-1])
# reverse_word()

# Assignment 6 "Write a Python program to count the number of even and odd numbers from a series of numbers"
def even_odd_counter():
    start_number = int(input("Enter start number: "))
    end_number = int(input("Enter end number: "))
    even_count = 0
    odd_count = 0
    for i in range(start_number, end_number + 1):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print("Number of even numbers:" + str(even_count))
    print("Number of odd numbers:" + str(odd_count))
# even_odd_counter()

# Assignment 7 "Write a Python program that prints each item and its corresponding type from the following list."
def list_printer(list):
    for x in list:
        print(x, type(x))
list_printer([1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}])

# Assignment 8 "Write a Python program that prints all the numbers from 0 to 6 except 3 and 6."
def number_printer():
    result = ""
    for i in range(7):
        if i == 3 or i == 6:
            continue
        result = result + str(i) + " "
    print(result)
number_printer()