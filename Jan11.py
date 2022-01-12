# Assignment 1 "Write a string that returns just the letter ‘r’ from ‘Hello World’"
print("Hello World"[8])

# Assignment 2 "String slicing to grab the word ‘ink’ from the word ‘thinker’"
print("thinker"[2:5])

# S=’hello’,what is the output of h[1] ANSWER: "e"

# S=’Sammy’ what is the output of s[2:] ANSWER: "mmy"

# Assignment 3 "With a single set function can you turn the word ‘Mississippi’ to distinct character word."
print(''.join(set('Mississippi')))

# Assignment 4 "determine whether the phrase represents a palindrome or not."
def palindrome():
    answers = []
    lines = int(input("Enter number of phrases:"))
    for i in range(0, lines):
        phrase = input("Enter phrase:")
        phrase = [ character.lower() for character in phrase if character.isalnum ]
        if (phrase == phrase[::-1]):
            answers.append("Y")
        else:
            answers.append("N")
    print(" ".join(answers))

# Assignment 5 "Create a list with one number, one word and one float value. Display the output of the list."
list = [2, "two", 2.0]
print(list)

# Assignment 6 "I have a nested list [1,1[1,2]], how to grab the value of 2 from the list."
nested_list = [1, 1, [1, 2]]
print(nested_list[2][1])

# Assignment 7 
# lst=['a','b','c'] What is the result of lst[1:]?
# RESULT: ['b', 'c']

# Assignment 8 "Create a dictionary with weekdays an keys and week index numbers as values.do assign dictionary to a variable"
dictionary = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

# Assignment 9 
# D={‘k1’:[1,2,3]} what is the output of D[k1][1]
# output: 2

# Assignment 10 "Can you create a list [1,[2,3]] into a tuple"
tuple = (1, (2, 3))
# OR 
list = [1, [2, 3]]
tuple(list)

# Assignment 11 "With a single set function can you turn the word ‘Mississippi’ to distinct character word. Can you add an element ‘X’ to the above created set"
print(''.join(set('MississippiX')))

# Assignment 12
# Output of set([1,1,2,3])
# Output: [1, 2, 3]

# Assignment 13 "Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included)."
assignment_13_answers = []
for i in range(2000, 3200):
    if i % 7 == 0 and i % 5 != 0:
        assignment_13_answers.append(i);
print(assignment_13_answers);

# Assignment 14 "Write a program which can compute the factorial of a given numbers."
def factorial():
    num = int(input("Input number:"))
    answer = num
    for i in range(1, num):
        answer *= i
    print(answer)

# Assignment 15 "With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary."
def dictionary():
    result = {}
    num = int(input("Input number:"))
    for i in range(1, num + 1):
        result.update({i: i*i})
    print (result)

# Assignment 16 "Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number."
def list_and_tuple():
    numbers = input("Input numbers seperated by commas: ")
    l = numbers.split(",")
    t = tuple(l)
    print(l)
    print(t)

# Assignment 17 "Define a class which has at least two methods:
#	getString: to get a string from console input
#	printString: to print the string in upper case.
#	Also please include simple test function to test the class methods."
class InputOutputString(object):
    def __init__(self):
        self.s=""
    
    def getString(self):
        self.s=input()

    def printString(self):
        print(self.s)

strObj = InputOutputString()
strObj.getString()
strObj.printString()

# Assignment 18 "THREES A CROWD"
def crowd_test(l):
    if(len(l) > 3):
        print("The room is too crowded!")
people = ["Thomas", "Justin", "Aidan", "Kensen"]
crowd_test(people)
people.pop()
crowd_test(people)
    
# Assignment 19 "THREES A CROWD 2"
def crowd_test2(l):
    if(len(l) > 3):
        print("The room is too crowded!")
    else:
        print("The room isn't too crowded.")
people = ["Thomas", "Justin", "Aidan", "Kensen"]
crowd_test(people)
people.pop()
crowd_test(people)

# Assignment 20 "SIX IS A MOB"
def crowd_test3(l):
    if len(l) > 5:
        print("There is a mob in this room!")
    elif len(l) >= 3 and len(l) <= 5:
        print("The room is too crowded!")
    elif len(l) >= 1 and len(l) <= 2:
        print("The room isn't too crowded.")
    else:
        print("The room is empty")

people2 = ["Thomas", "Justin", "Aidan", "Kensen", "John", "Bobert"]

crowd_test(people2)
people2.pop()
crowd_test(people2)
people2 = people2[:1]
crowd_test(people2)
people2.clear()
crowd_test(people2)