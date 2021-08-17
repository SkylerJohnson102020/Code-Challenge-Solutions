import math
import os
import random
import re
import sys

def plusMinus(arr):
    positive_ratio = 0.0
    negative_ratio = 0.0
    zero_ratio = 0.0
    
    for num in arr:
        if num == 0:
            zero_ratio += 1.0/len(arr)
        if num > 0:
            positive_ratio += 1.0/len(arr)
        if num < 0:
            negative_ratio += 1.0/len(arr)
        
    print(round(positive_ratio, 6))
    print(round(negative_ratio, 6))
    print(round(zero_ratio, 6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
