# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 01:15:09 2020

@author: Shelly Meter
"""

miles = 26.2
print(miles * 1.61)

"""
print(5)
print(x=5)
print(x+1)

TypeError: 'x' is an invalid keyword argument for this function
"""

print(5)
print("x=5")
int(x=5)
print("x+1=",5+1)


"""Chapter 2 Exercises
Ex 2.1
We’ve seen that n = 42 is legal. What about 42 = n?

42 = n
SyntaxError: can't assign to literal



In some languages every statement ends with a semi-colon, ;. What happens if you put a
semi-colon at the end of a Python statement?

print(5); had no effect but print(5). had SyntaxError: invalid syntax



In math notation you can multiply x and y like this: xy. What happens if you try that in
Python?

print(xy)
NameError: name 'xy' is not defined
"""


"""Chapter 2 Exercises 2.2
1. The volume of a sphere with radius r is 4/3 π r3. What is the volume of a sphere with radius 5?
"""

pi=3.1415926535897932
r=5
v=(4/3)*pi*(r**3)
print("volume of sphere with radius 5 =", v)

""" Chapter 2 Exercises 2.2
2. Suppose the cover price of a book is $24.95, but bookstores get a 40% 
discount. Shipping costs $3 for the first copy and 75 cents for each additional 
copy. What is the total wholesale cost for 60 copies?
"""

cp=24.95
print(0.6*cp)
dp=14.969999999999999

print("cost after discount before shipping", 60*dp)
print("shipping cost", (0.75*59)+3)
print("total wholesale cost = $", 898.1999999999999+47.25)





