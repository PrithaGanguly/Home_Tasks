==========
ShareValue
==========

Problem
-------

Write a program to print the latest share value of a company whose NASDAQ symbol would be provided in the command line.

Code Snippet
------------

::

    #!/usr/bin/env python
    import urllib2
    import sys

    # a function share_price is defined to get the latest share value of a company
    def share_price(nasdaqsym):
    #the link to the finance site is made abd the data is stored in the instance "share_value"
        share_value = urllib2.urlopen('http://download.finance.yahoo.com/d/quotes.csv?s='+nasdaqsym+'&f=l1')

       #The share price is printed
        print "Latest share price of company with NASDAQ symbol "+nasdaqsym+" : " +share_value.read()

    if __name__ == '__main__':
    #Checking included whether we have one Symbol in the command line or not as per the syntax "./sharevalue    .py [NASDAQ symbol]
         if len(sys.argv) == 2:
             share_price(sys.argv[1])
         else:
             print "Give only one NASDAQ symbol at a time after command line argument!"
     sys.exit(0)

Explanation
-----------

For the above stated problem, to obtain the latest share value of a company using the company's **NASDAQ** symbol, the function *urlopen()* of the module **urllib2** has been used. It takes the link of the website *finance.yahoo.com* as input and returns the latest share value(specified by the sybmol f=l1 in the link) of the company which is stored in the instance **share_value**. Then in **'__main__'**, a checking is included which checks whether there is only one input symbol given after the command line input i.e **./sharevalue.py**.

Link to the original code
-------------------------

The Link to the original code is given in `sharevalue.py <https://github.com/PrithaGanguly/Home_Tasks/blob/master/sharevalue/sharevalue.py>`_. 
