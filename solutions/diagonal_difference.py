import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    n = len(arr)
    print(f"n equals {n}")
    diagonal_1 = 0
    diagonal_2 = 0
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                diagonal_1 += arr[i][j]
                # print(f"diagonal 1 equals {diagonal_1}")
            if (i == n - j - 1):
                diagonal_2 += arr[i][j]
                print(f"diagonal 2 equals {diagonal_2}")
    return abs(diagonal_1 - diagonal_2)
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
