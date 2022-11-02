#!/usr/bin/env python3

#list

# list is denoted by []
l=[1,2]
print("before appending 3 : {}".format(l))
l.append(3)
print(" after appending 3 : {}".format(l))
l.remove(2)
print("after removing 2 : {}".format(l))


# a list can contain any datatype
l1=[1,2,'sam','a']
print(l1)

#advance operations on list

#slice
print(l1[0])
print(l1[0:2])
# start index in inclusive and end index is exclusive while printing a list.

#split
l3_string="hello python programming"
l3=l3_string.split(' ')
print(type(l3))


#tuple
t=(1,2)
print(type(t))
t1=1,2
print(id(t1))
print(type(t1))

# immutable
t1=t1 + (3,4)
print(id(t1))


#set
s={1,2}
print(type(s))
s.add(3)
print(s)
s.remove(1)
print(s)
        
s1={2,4,5}
s2={3,4,5}

print(s1.difference(s2))
print(s1.intersection(s2))



#dictionaries
d={"name":"sam"}
print(d)

print(d["name"])

d["rollno"]=20
print(d)
d.pop("name")
print(d)
d["rollno"]=31
print(d)