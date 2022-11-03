#!/usr/bin/env python3

#a. what is boolean in python
b=True
print(type(b))

b1=False
print(type(b1))

b2='True'
print(type(b2))

#b. comparision operators in python
a=10 
b=20
c = a < b

print(c)



#. if conditional in python
if a>b:
    print("a is greater")
else:
    print("b is greater")

# bool True or false means in terms of string/number
if bool(0):
    print("0 is True")
else:
    print("0 is False")
          #any non zero number is treated as True in python
          
          #any non emtpy string is treated as true in python
name=""
if name:
    print("{} is True".format(name))
else:
    print("False")



#c. in keyword
l=[11,2,3]
if l[0]==1 or l[1]==1 or l[2]==1 :
    print("1 exist in our list")
    
if 11 in l:
    print("yes it exists")

#e. indentation error in python
if True:
 print("True")
 print("another stt")


#f. loops : for and while
fnames=['sam','tom','jerry']
for i in fnames:
    print(i)
    
#print number from 1 to 10
for i in  range(1,10,1):
    print(i)
    
#print only even numbers
for i in range(2,11,2):
    print(i)
    
    
    #print table of 4:
for i in range(4,41,4):
    print(i)

i=1
while i <= 10:
    print(i)
    i=i+1