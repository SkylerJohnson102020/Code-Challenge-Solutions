import os
from collections import Counter

def lonelyinteger(a):
    count_list = Counter(a)
    print(count_list)
    
    for i in count_list:
        if count_list[i] == 1:
            return i
        
# def lonelyinteger(a):
#     value = 0
#     keys = dict.fromkeys(a, value)
#     print(keys)
#     for i in a:
#         if i in keys:
#             keys[i] += 1
#         print(keys)
#     for key, value in keys.items():
#         if value < 2:
#             print(key)
#     return key
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
