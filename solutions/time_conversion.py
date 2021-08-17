import math
import os
import random
import re
import sys

def timeConversion(s):
    string = s.split(':')        
    if s[-2:] == 'PM':
        if s[:2] != '12':
            string[0] = str(int(string[0])+12)
            
    if s[-2:] == 'AM':
        if s[:2] == '12':
            string[0] = '00'
                    
    new_string = ':'.join(string)
    return str(new_string[:-2])
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
