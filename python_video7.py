#!/usr/bin/env python3

#a. define a function
# To define a function we use def keyword
# To remove redundant data we use function to define a piece of code once and use it again.
# def <fun_name>():
    
def print_body():
    print("This is body of our function")
    

#print_body()

#b. argument vs parameters
#value passed while calling a function is called as argument
#variable defined during the definition of function is called as parameter

def print_body1(custom_message): # here it is parameter
    print(custom_message)
    
    
#custom_msg= input("enter you msg")
#print_body1(custom_msg) #argument

#c. default parmaters
# to assign a default value to a parameter if its value is not passed.

def total(sub1,sub2,sub3=0):
    total=sub1+sub2+sub3
    print("This is Total marks {}".format(total))
    
#total(10,20,30)
#total(10,20)



sub1=10
sub2=20
sub3=30
#d. lambda function
func_name=lambda sub1,sub2,sub3: sub1+sub2+sub3
print(type(func_name))
total_sum=func_name(10,20,30)
print("Total sum {}".format(total_sum))

