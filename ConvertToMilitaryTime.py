#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    
    #assert len(s) == 10
    #s[8:10]
    hours = s[0:2]
    minutes = s[3:5]
    seconds = s[6:8]
    m = s[8:10]
    newtime = ""
    
    if (m == ("AM")):
        if (int(hours) == 12):
            newhours = "00"
        if (int(hours) > 12):
            newhours = str(int(hours) - 12)
        if (int(hours) < 12):
            newhours = hours
        newtime += newhours + ":" + minutes + ":" + seconds
        return newtime
    
    elif (m == ("PM")):
        if (int(hours) == 12):
            newhours = hours
        if (int(hours) < 12):
            newhours = str(int(hours) + 12)
        newtime += newhours + ":" + minutes + ":" + seconds
        return newtime
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
