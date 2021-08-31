#!/bin/python3
import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    caesar_string = ''
    if k >= 26:
        k = k % 26
    for char in s:
        char = ord(char)
        if (char >= 65) and (char <= 90):
            char += k
            if char > 90:
                char -= 26
        if (char >= 97) and (char <= 122):
            char += k
            if char > 122:
                char -= 26
        caesar_string += chr(char)
    return caesar_string
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
