#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Method number 1: An example of reversing a string using a loop.
string = "Enter the text you would like to reverse here."
revString = ""

for char in string[:]:
   revString = char + revString
rint(revString)  


# Method number 2: How-to reverse a string upon printing it out. 
string = "Enter the text you would like to reverse here."
print(string[::-1])


# Method number 3: How-to reverse a string using the reversed() function.
string = "Enter the text you would like to reverse here."
print(''.join(reversed(string)))

