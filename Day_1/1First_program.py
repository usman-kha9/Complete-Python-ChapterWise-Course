"""
1First_program.py
Basic examples: printing strings and numbers, variable assignment, and type checks.
Run: python .\1First_program.py
"""

print("hello world") #Output will be hello world
print("my name is usman") #Output will be my name is usman
print("my age is 18") #Output will be my age is 18
print("my name is usman" , "my age is 18") #Output will be my name is usman my age is 18
print(20)              #in case of number we does not use double code
print(20 + 30)


name = "usman" #string data type
age = 18 #integer data type 
price = 20.5 #float data type
print(name) #output will be usman
print("my name is:" ,name) #output will be my name is: usman
print("my age is :", age) #output will be my age is : 18

#how to find out type :
                      # -> we use type function before variable name.

print(type(name)) #output will be <class 'str'>
print(type(age)) #output will be <class 'int'>
print(type(price)) #output will be <class 'float'>