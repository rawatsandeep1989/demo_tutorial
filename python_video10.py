#!/usr/bin/env python3


#Inheritance
class Person:  #base class  or parent class
    def __init__(self,name,id):
        self.name=name
        self.id=id
        print("init of person")


class Working_person(Person):  #derived class or child class
    def __init__(self,name,id,salary):
        super().__init__(name,id)
        self.salary=salary
        print("init of working person")
        
        
wp=Working_person("sam",12,12000)

    
#single level inheritance

#multiple inheritance

class A: 
    def print_msg2(self):
        print("msg2 is printed")

class B:
    def print_msg1(self):
        print("msg1 is printed")
    
class C(B,A):
    pass


c_obj=C()
c_obj.print_msg1()
c_obj.print_msg2()




#Types of inheritance : single , multiple,multilevel, hybrid
#Derived vs base class or main class vs sub class === done
#Diamond problem ??



class W:
    def print_msg0(self):
        print("msg0 was printed")
class X(W):
    def print_msg1(self):          # print_msg0 and print_msg1
        print("msg1 was printed")
    
class Y(W):
    def print_msg2(self):           #print_msg2 and print_msg0
        print("msg2 was printed")
    
class Z(Y,X):                       #print_msg0, print_msg0, print_msg1 and print_msg2
    def print_msg3(self):
        print("msg3 was printed")   


z_obj=Z()
z_obj.print_msg0()

