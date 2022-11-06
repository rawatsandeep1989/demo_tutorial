#!/usr/bin/env python3


#list comprehension : To create a new list based on existing list
l=[1,2,5,6,7,8]
l_double=[x*2 for x in l]
print(l_double)

l_even=[y for y in l if y%2 ==0 ]
print(l_even)

# zip function : it is used to combine two list into a list of tuples
names=['sam','tom','jerry','aman']
roll_nos=[1,4,6,7,8]
new_list=list(zip(roll_nos,names))
print(new_list)

#enumerate: creates a list and adds number to it
print("This output is of enumerate section")
names1=['sam','tom','jerry','aman']
new_list1=list(enumerate(names1,start=1))
print(new_list1)

#slicing
l_numbers=[1,2,3,4,5]
#          0 1 2 3 4
#          -5  -4  -3  -2  -1
print(l_numbers[0:4])
print(l_numbers[-5:-3])
print(l_numbers[-5:3])
print(l_numbers[:3])
print(l_numbers[3:])