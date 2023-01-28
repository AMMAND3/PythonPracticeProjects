#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    
    mini, maxi = arr[1], arr[1]
    
    
    for i in arr:
        if i < mini:
            mini = i
        if i > maxi:
            maxi = i
    minsum, maxsum, checkmin, checkmax = 0, 0, 0, 0
    for j in arr:
        if j != mini:
            maxsum += j
        if j != maxi:
            minsum += j
        
        if j == mini and checkmax == 1:
            maxsum += j
        if j == maxi and checkmin == 1:
            minsum += j
        if j == mini and checkmax == 0:
            checkmax += 1
        if j == maxi and checkmin == 0:
            checkmin += 1
        
    print(minsum, maxsum)
        
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
