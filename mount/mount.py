#!/usr/bin/env python
f = open("/proc/mounts")#opens file /proc/mounts
s = f.readlines()# reads the file line by line
for x in s[1:]:# for loop which ignores the first line of the file and begins from the second line of the file
    b = x.split(" ")#splits the file line by line according to spaces
    del b[-2]#deletes the  second last zero from the file
    del b[-1]#deletes the last zero from the file
    b.insert(2,"type ")# the string "type" is inserted in index 2
    b.insert(1,"on")# the string "on" is inserted in index 1
    b.insert(5,"(")# the opening bracket "(" is inserted in the 5th index
    b.insert(7,")")# the closing bracket ")" is inserted in the 7th index
    str = " ".join(b)# the splitted string is joined using the join() function
    print str #the required output is printed; for loop ends
f.close()# file is closed
