#!/usr/bin/env python3

'''
This program is about defining string
it explain bla bla bla.
'''
"""
This is same as above.
This is again a multiline comment.
"""

#this is single line comment

name = "linuxgeeks"
name1= 'linuxgeek1'
name2=""" name : jose
empcode : 2300
"""
name3 = '''name : santosh
empcode : 4500
'''

print(name)
print(name1)
print(name2)
print(name3)

# multiline string is helpful to pass multiline comment string.
''' 
this is how we pass multiline string in python
'''
"""
This is another way
"""

#perform type conversion in python
age=90
print(type(age))

print("my age is " + str(age))

age="6"
print("my age in months is :"+ str((int(age)*12)))


#perform string printing
name= "kareena"
age = input("Enter the age: ")
print(type(age))
print("{} age is {} months old".format(name,age))

print("{0} age is {1} months old".format(age,name))

print("{name} is {age} months old".format(name=name,age=age))


print(f"{name} is {age} months old")

#taking input from user

empcode=input("Enter you emp code")
print(type(empcode))
empcode =int(empcode) +12
print("your emp code empcode = empcode is {}".format(empcode))
print(type(empcode))
