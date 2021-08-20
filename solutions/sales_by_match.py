import math
import os
from collections import Counter

def sockMerchant(n, ar):
    sock_dict = Counter(ar)
    sock_values = sock_dict.values()
    pair_counter = 0
    for pairs in sock_values:
        if pairs >= 2:
            total_pairs = math.floor(pairs / 2)
            pair_counter += total_pairs
    return pair_counter
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
