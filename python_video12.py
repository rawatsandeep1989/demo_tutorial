#!/usr/bin/env python3


# file handling : to persist our data
#name=input("Enter a name")
#print(name)


#fh=open("file1.txt",'a') # w is for write , a is append, r is for read
#fh.write(name+"\n")
#fh.close()

# open a file : open()
# read a file : read(),readlines
fh1=open("file1.txt",'r')
print(fh1.readlines())
fh1.close()


# write a file : write()
# close a file : close()

