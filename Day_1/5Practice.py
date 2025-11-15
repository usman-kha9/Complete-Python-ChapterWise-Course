#"""
# 5Practice.py
# Small practice programs: sum of two numbers, square area, average, and a comparison problem.
# Run: python .\5Practice.py
#"""

#practice question
#1write a program to input 2 numbers and print their sum.

input("enter first number :")
first= int(input("enter first number :"))

input("enter second number :")
second= int(input("enter second :"))

sum = first + second

print("sum =" , first + second)

#2write a program to input side of a square and print its area.

input("enter square side :")
side =float(input("enter square side :"))

print("area =" ,side * side)

#3write a program to input 2 floating point numbers and print their average.
input("enter first number :")
a = float(input("enter first number :"))

input("enter second number :")
b = float(input("enter second number :"))

average = (a + b)/2

print("average =" ,average)

#4 write a program to input 2 int number ,a and b, print true if a is greater or equal to b. if not print fals.


input("enter first number :")
a = int(input("enter first number :"))

int("enter second number :")
b = int(input("enter second number :"))

print(a >= b)