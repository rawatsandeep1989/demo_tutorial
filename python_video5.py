#!/usr/bin/env python3

#break : it bring the control at the begining of the next stt just after the loop ( while , for )
l=[1,2,3,4]
for i in l:
    if i == 3:
        break
    else:
        print(i)
print("Hey i am now at line 10")

#continue : it bring the control back to the starting of the loop and stops further execution of stt inside the block.

l1=[1,2,3,4,5]
for i in l1:
    if i == 4:
        continue # from here it will go to start of line 15
    else:
        print(i)




#for with else : the purpose of this is that if our code execute without encountering break else part will be executed
l3=[1,2,3,4,7,8]
for i in l3:
    if i == 8:
        break
else:
    print("hey no break was encountered")

#pass : this is basically a placeholder for future code
print("This part is pass part")
a=11
if a == 10 :
    print(a)
else:
    print("Hey a is equals to {}".format(a))  # this place is left empty so that programmer can decide later what to do.



