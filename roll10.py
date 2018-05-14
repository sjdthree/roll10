#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 16:56:49 2018

@author: sjd@mit.edu
@github:  sjdthree

https://github.com/sjdthree/roll10/blob/master/README.md
"""

import matplotlib.pyplot as plt
from random import randint
from collections import defaultdict

#global dictionary rd

rd = defaultdict(dict)
# two rolls of 6-sided die lookup table for even distribution of 10-values (no 7 sums)
#  6 * 6 total combinatons = 36, less 6 values that sum to 7, so 30 possible combinations
#first half of lookup matches to 1-5 results, there are 3 combinations for each value
count = 3
for i in range(1,6):
    for j in range(1,7-i):
        #print(i,j)
        rd[(i,j)] = count // 3  # this outputs 1-5, 3 values each
        count+=1

# second half of lookup match 6-10
count = 18
for i in range(6,1,-1):
    for j in range(6,7-i,-1):
        #print(i,j)
        rd[(i,j)] = count // 3  # this outputs 6-10, 3 values each
        count+=1
    
# definitions
        
roll6 = lambda : randint(1,6)

def roll10():
    a=3
    b=4
    while (a+b == 7):  # remove those rolls that sum to 7;
                # leaves 30 combinations; allocate evenly across 10 values
        a = roll6()
        b = roll6()
    #print(a,b)
    return rd[a,b]  #lookup and return 1-10 based on the a & b rolls

#main program
    
if __name__ == '__main__':

    x=list()

#    for j in range(1000000):     #longer test
    for j in range(10000):
        x.append(roll10())
        
    #  plots to check historgram.  all values 1-10 should be evenly distributed
    # i.e. a flat histogram
    plt.hist(x)
    plt.show()
    
    
