# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 00:00:43 2020

@author: Shelly Meter
"""

print("Hello, world!")


""" Exercises 1.9 - 1.1 - 1
In a print statement, what happens if you leave out one of the parentheses, or both?
print("Hello, world!"

SyntaxError: invalid syntax
"""


""" Exercises 1.9 - 1.1 - 2
If you are trying to print a string, what happens if you leave out one of the quotation marks,
or both?
print(Hello, world!)

SyntaxError: invalid syntax

"""

""" Exercises 1.9 - 1.1 - 3
You can use a minus sign to make a negative number like -2. What happens if you put a plus
sign before a number? What about 2++2?

Viewed as 2+(+2) and will do addition
"""

""" Exercises 1.9 - 1.1 - 4
In math notation, leading zeros are ok, as in 09. What happens if you try this in Python?
What about 011?

SyntaxError: invalid token
"""

""" Exercises 1.9 - 1.1 - 5
What happens if you have two values with no operator between them?
ex: 2 2
SyntaxError: invalid syntax
"""

""" Exercises 1.9 - 1.2 - 1
How many seconds are there in 42 minutes 42 seconds?
print("seconds in 42 minutes 42 seconds", (42*60)+42) = 2562
"""

print("seconds in 42 minutes 42 seconds", (42*60)+42)

""" Exercises 1.9 - 1.2 - 2
How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.

print("miles in 10 km", 10/1.61) = 6.211180124223602
"""

print("miles in 10 km", 10/1.61)


""" Exercises 1.9 - 1.2 - 3
If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per
mile in minutes and seconds)? What is your average speed in miles per hour?


seconds in 42 minutes 42 seconds 2562
miles in 10 km 6.211180124223602
hours in 42 min 42 sec 0.7116666666666667 hrs
miles per second 0.0024243482139826703 mi per sec
miles per minute 0.14546089283896022 mi per min
miles per hour 0.0024243482139826703 mph
"""

print("hours in 42 min 42 sec", ((42*60)+42)/(60*60), "hrs")
print("miles per second", 6.211180124223602/2562, "mi per sec")
print("miles per minute", 0.0024243482139826703*60, "mi per min")
print("miles per hour", 0.14546089283896022/60, "mph")















