#"""
# 2Data_type.py
# Explains core Python data types with examples: str, int, float, bool, NoneType.
# Run: python .\2Data_type.py
#"""

#DATA TYPES:
           # -> data types are the types of data which we use in programming language like python to store different type of data.
           # -> there are 5 main data types in python.
#1> STRING
        #=> string is of any word or sentence or alphanumeric value which we use in double or single or triple quotes.
name1="usman"
name2='usman'
name3='''usman'''

print(name1)   # usman
print(name2)   # usman
print(name3)   # usman

#2>INTEGER
         #=>   Integer means whole numbers without decimal point like 1,2,3,4,5,6,7,8,9 etc.
age = 18
print(type(age)) #output will be <class 'int'> and 18 will be shown in the output terminal

#3 FLOAT
      #=> Float means numbers with decimal point like 1.5 , 2.5 , 3.5 etc.
price = 20.5
print(type(price))  #output will be <class 'float'> and 20.5 will be shown in the output terminal

#4 BOOLEN
       #=> Boolen means true or false value. It just tell us that the statement is true or false.
age=18
old= False
print(type(old)) #output will be <class 'bool'> and False will be shown in the output terminal, because the age is not old.

is_adult= True
print(type(is_adult)) #output will be <class 'bool'> and True will be shown in the output terminal, because the age is adult.

#5NONE TYPE
         #=> None type means no value or null value.
         #-> None type is used when we want to clear the value of a variable or we want to assign no value to a variable.
         #-> None type is also used when we want to return nothing from a function.
a= None
print(type(a)) #output will be <class 'NoneType'> and None will be shown in the output terminal.
a = 5

print(a) #output will be 5 because here we assign 5 to a variable a. And in programing language we called it as variable reassigning or type casting.



#Practice Examples:
#PRINT SUM
a= 10
b= 3
sum = a+b
print(sum)
    #or
a= 10
b= 3
print(a + b)


#PRINT DIFFERENCE
a= 10
b= 3
DIFFERENCE= a-b
print(DIFFERENCE)
     #or
a= 10
b= 3
print(a-b)

#PRINT DIVISION
a=10
b=3
DIVISION=a/b
print(DIVISION)
