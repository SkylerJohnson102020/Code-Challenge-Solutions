#!/bin/python3

import math
import os

def pageCount(n, p):
    book = [num for num in range(n+1)]
    mid = math.floor(len(book) / 2)
    count = 0
    if (p == n) or (mid <= 1):
        return count
    if (p < mid):
        for page in book:
            if page != p:
                count += 1
            if page == p:
                new_count = math.floor(count / 2)
    if (p >= mid):
        for page in reversed(book):
            if page != p:
                count += 1
            if page == p:
                if (count == 1) and (p % 2 == 1):
                    return count
                new_count = math.floor(count / 2)
    return new_count

# Example below has hard coding issues. Trying an approach that does not use loops.

# def pageCount(n, p):
#     mid = math.floor((n + 1) / 2)
#     if (p == n) or (mid <= 1):
#         return 0
#     if (n - p) >= mid:
#         return math.floor(p / 2)
#     if (n - p) < mid:
#         if ((n - p) <= 2):
#             if (n % 2 == 0):
#                 return 1
#             return 0 
#         if p == mid:
#             return math.floor((n - p) / 2)
#         return math.floor((p - mid) / 2)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
