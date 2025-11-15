"""
4Input_in_python.py
Shows how to use input() and how to cast inputs to int/float. Contains examples that read values and print types.
Run: python .\4Input_in_python.py
"""

#INPUT IN PYTHAN PROGRAMMING
                            #-> Input function is used to take input from the user. It is a built-in function in python.
                            #-> The input function always takes input in string format.
                            #-> If we want to take input in other data types like integer or float then we have to type cast the input function.
input("enter your name :")
name = input("enter your name :")
print("welcome" ,name) # The output will be welcome usman if the user input is usman. The input function always takes input in string format.If we do not type cast the input function.if we want to take input in other data types like integer or float then we have to type cast the input function.
print(type(name)) #The output will be <class 'str'> because the input function always takes input in string format.

value = input("enter some value :")
print(type(value) , value) #The output will be <class 'str'> and the value entered by the user because the input function always takes input in string format.

int("5")
value = int(input("enter some value")) # Type casting the input function to integer.
print(type(value), value) #The output will be <class 'int'> and the value entered by the user because we have type casted the input function to integer.

int("5")
value = float(input("enter some val")) # Type casting the input function to float.
print(type(value) , value) #The output will be <class 'float'> and the value entered by the user because we have type casted the input function to float.

name = input("enter your name :")  # Input function to take input from the user.
age = int(input("enter your age :")) # Type casting the input function to integer.
marks = float(input("enter marks :")) # Type casting the input function to float.

print("welcome" , name) # The output will be welcome usman if the user input is usman.
print("age =" , age) # The output will be age = 18 if the user input is 18.
print ("marks =" , marks) # The output will be marks = 85.5 if the user input is 85.5.
print(type(name) , type(age) , type(marks)) # The output will be <class 'str'> <class 'int'> <class 'float'> because we have type casted the input function to integer and float.