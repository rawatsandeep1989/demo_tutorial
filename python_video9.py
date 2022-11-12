#!/usr/bin/env python3

#super,self
class A:  #parent or base class 
    def __init__(self):
        print("init func of A")
    def print(self): #self denotes the instance on which this method was called.
        print("hello world")
        
        
        
class B(A): #child class or derived class
    def __init__(self):
        print("init func of B")
        super().__init__() # super keyword is used to call the funciton of the parent class
        

b_obj=B()


# types of method in python
# instance method : any method which takes instance as a parameter is called as instance method
# class method : 

class P:
    @classmethod
    def print_msg(cls): #we pass class name as the parameter to this function
        print("hello world")


P.print_msg()

# static method :
class X:
    @staticmethod
    def print_msg1(): #the methods which donot take any parameter is called as static method in python
        print("hello i am static method")
        
x_obj=X()
x_obj.print_msg1()