# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 01:49:44 2022

@author: abhi575
"""

# 100 days of Python day 2 exercises/assignments

# Excercise 2.1 (Subscripting usage and Type Casting)

two_digit_number = input("Type a two digit number: ")

print(type(two_digit_number)) # you are working with a string data type

# below use subscripting to help with adding the two digit number and use type casting to turn
# it into a number. 

Digit_1 = int(two_digit_number[0])
Digit_2 = int(two_digit_number[1])

# above [] allows us to treat each digit entry and indexes while int() converts the data type to integer from string

print(Digit_1 + Digit_2)

# Excersie 2.2 (Mathematical Operations and PEMDAS usage with Left to Right rule)
# Using BMI (Body Mass Index Calculation)
# BMI = weight(kg)/(height**2(m^2)) or for US: BMI = (weight(lb)*703)/(height**2(in^2))

height = input("enter your height in inches: ")
weight = input("enter your weight in pounds(Lbs): ")

H = float(height)
W = float(weight)

BMI = int((W * 703)/(H**2))

print(BMI)

# Exercise 2.3 (Your life in Weeks) (Usage of f-strings, and Number Manipulation)
# Find out how many days weeks and months you have left if you are going to live till 90

age = input("What is your current age?")

age_int = int(age) # age needs to remain an integer

years_remaining = 90 - age_int # to find out exactly how many years remaining till 90

Days = years_remaining * 365 # helps find Days
Weeks = years_remaining * 52 # helps find Weeks
Months = years_remaining * 12 # helps find Months

print(f"You have {Days} days, {Weeks} weeks, and {Months} months left.")
#f-string usage above helps us combine and print that whole statement as a string. 


