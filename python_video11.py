#!/usr/bin/env python3



#a. Error
a=10
if a == 10:
    print(a)

#b. Exception
b=10
if b == 10:
    print(b)


#c. try
try:
    c=b/0
    print(f"value of c is {c}")
except Exception as e:
    print("Exception was raised duering execution")
    print(e)
else: # this block is executed only when the code doesn't through any exception.
    print("c is printed")
finally: #this block is used to execute a piece of code in both situations i.e if exception is raised or not raised.
    print("hey i have got executed")
#else

#f. finally


#g. raise
x=10.0
if type(x) is not int:
    raise TypeError("Hey x is not int type")
    