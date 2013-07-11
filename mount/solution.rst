=====
Mount
=====

Problem
-------

Write a file which gives the same output as while typing mount command in the terminal.

Code Snippet
------------

::

 1. #!/usr/bin/env python
 2. f = open("/proc/mounts")#opens file /proc/mounts
 3. s = f.readlines()# reads the file line by line
 4. for x in s[1:]:# for loop which ignores the first line of the file and begins from the second line of the file
 5.     b = x.split(" ")#splits the file line by line according to spaces
 6.     del b[-2]#deletes the  second last zero from the file
 7.     del b[-1]#deletes the last zero from the file
 8.     b.insert(2,"type ")# the string "type" is inserted in index 2
 9.     b.insert(1,"on")# the string "on" is inserted in index 1
 10.    b.insert(5,"(")# the opening bracket "(" is inserted in the 5th index
 11.    b.insert(7,")")# the closing bracket ")" is inserted in the 7th index
 12.    str = " ".join(b)# the splitted string is joined using the join() functi    on
 13.    print str #the required output is printed; for loop ends
 14. f.close()# file is closed

Explanation of the code
-----------------------

For the required problem, the python code along with sufficient comments is given above. The file **/proc/mounts** is opened using the **open()** function and is read line by line using the **readlines()** function. Then using a *for loop* the required changes are made so that the output of this program matches exactly with the output of the mount command in the terminal. The necessary insertions and deletions whatever done is mentioned alongside the code in form of comments.

The actual link of the code is given in, ` mount.py <https://github.com/PrithaGanguly/Home_Tasks/blob/master/mount/mount.py/>`_. 

