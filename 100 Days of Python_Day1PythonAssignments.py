# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 17:16:30 2022

@author: abhi575
"""
# Day 1 coding practice for 100 Days of Python
# Printing Commenting, Debugging, String Manipulation and Variable


# 1.1) Printing Assignment code challenge

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# 1.2) String Manipulation
# These are all examples below to show how you can manipulate Strings
print("Hello world!\nHello world!\nHello world!") # \n gives space and creates new line
print("Hello" + "Angela") # + helps you concatinate the two seperate string
print("Hello" + " Angela") # To add a space you just have to put a space in front of Angela so the words are seperated
print("Hello" + " " + "Angela") # You can also do the same thing as line 21 like this for same result
# Remember spaces are very important in python programing
# IndentationError can happen due to space or tabs. When coding in pythong always start your code at the beginning of the line so there is no IndentationError


# 1.3) Debugging Assignment code challenge

# Debug the following codes below

# print(Day 1 - String Manipulation")
# print("String Concatenation is done with the "+" sign.")
#   print('e.g. print("Hello " + "world")')
# print(("New lines can be created with a backslash and n.")

# 1.3) Below is the debugged codes given above

print("Day 1 - String Manipulation") # This line was missing a " in front of Day
print('String Concatenation is done with the "+" sign.') # This line needed single '' because u are using "" for +
print('e.g. print("Hello " + "world")') # This line had an unexpected indent so need to start at the beginning of the lin. IndentationError
print("New lines can be created with a backslash and n.") # This line has an extra missplaced paranthesis so get rid of it. Syntax Error 

# 1.4) input coding excercise. 
# Below we are writing a coding excercise using input() function
# Whenever you are using input() function, you have to always assign it to a variable otherwise python won't know what is going on
# Using input("What is your name?") is asking the user to put in a name which than replaces the input entry. 
# len() gives you the length of the characters in the string

Name = len(input("What is your name?"))
print(Name)

# you can also write it like this below

print(len(input("What is your name?")))

# 1.5) Variable Assignment Code Challenge
# Here we are using the concept of user inputting values for a and b, 
# but with coding we will switch a's value to b and b's value to a for output
a = input("a:")
b = input("b:")

# 1.5) below we are using a third variable to accomplish the switch

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

# "Side Notes": When you're naming variables, always use useful names. 
# Variables can't have numbers at the beginning
# don't use stuff like print and input as names because those are designated words for python










