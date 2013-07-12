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
    #Checking included whether we have one Symbol in the command line or not as per the syntax "./sharevalue.py [NASDAQ symbol]
    if len(sys.argv) == 2:
        share_price(sys.argv[1])
    else:
        print "Give only one NASDAQ symbol at a time after command line argument!"
    sys.exit(0)

