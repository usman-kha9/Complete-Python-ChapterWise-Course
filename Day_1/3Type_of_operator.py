#"""
# 3Type_of_operator.py
# Demonstrates arithmetic, comparison, assignment, and logical operators with examples.
# Run: python .\3Type_of_operator.py
#"""

#TYPE OF OPERATORS
                 # -> Operators are the symbols which are used to perform operations on variables and values.
                 # -> There are 4 types of operators in python.
#1ARITMETIC OPERATOR
                  # -> Aritmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, division etc.
a= 10
b= 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #% means modelo which means reminder of the two values
print(a ** b) # ** means power
print(a // b) # // means floor division which means the value will be rounded off to

#2RENATIONAL OPERATOR
                   # Renational operators are used to compare two values.
                   #Renational operator means equal or not equal,less or greater than, less or equal, greater or equal.
a = 10
b = 3
print(a==b) #fals
print(a!=b) #true
print(a>=b) #true
print(a<=b) #fals
print(a> b) #true
print(a< b) #fals

#3ASSIGNMENTAL OPERATORS
                    # -> Assignmental operators are used to assign values to variables.
                    # -> There are 7 types of assignmental operators in python.
#1=                 
num = 10
num = num +10 #means 10+10 = 20
       #or
#2 +=
num += 10
print(num)
print("num :",num)


#3 -=
num = 10
num =10 -10 #means 10-10=0
print(num)
  #or
num-=10 #means 10-10=0
print("num :" , num)


#4 *=
num = 10
num *=5 #* means multiplication of 5 * 10 =50
print("num :", num)


#5 /=
num = 10
num /=5 #/ means division 10/5=2
print("num :" , num)


#6 %=
num =10
num %=5 #%means reminder 10%5=0
print("num :", num)


#7 **=
num =10
num **= 5 #** means power 10**5=100000
print("num :", num)

#4LOGICAL OPERATORS 
                    # -> Logical operators are used to combine two or more conditions.
                    # -> There are 3 types of logical operators in python.
#1 Not operator
print(not False) #true
print(not True) #Fals

a = 50
b = 30
print(not False)
print(not(a>b)) #It will print false because a is greater than b but we use not operator before the condition so the output will be false.
print(not(a<b)) #It will print true because a is greater than b and we use not operator before the condition so the output will be true.

#2 AND OPERATOS
val1 =True
val2= True
print("and operator :" , val1 and val2) #It will print true because in and operator both values are true then the output will be true and vorse versa

#3 OR OPERATOR

val1 =True
val2 =False
print("OR operator:", val1 or val2) #It will print true because in or operator if one value is true then the output will be true
