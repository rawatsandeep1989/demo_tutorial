#!/usr/bin/env python3

#a. class
class Student:
    def __init__(self,name,sub1,sub2,sub3):
        self.name=name
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3

    def print_total_marks(self):
        print("{} has got total marks {} ".format(self.name,self.sub1+self.sub2+self.sub3))
    



#b. methods
#c. property
#d. object
stud1=Student("sam",10,20,30)
print(stud1.__class__)
stud1.print_total_marks()