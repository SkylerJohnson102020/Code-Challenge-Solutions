import os
import string

def pangrams(s):
    alpha_dict = dict.fromkeys(string.ascii_lowercase, 0)
    clean_string = s.replace(' ', '').lower()
    for char in clean_string:
        if char in alpha_dict:
            alpha_dict[char] += 1
    values = alpha_dict.values()
    for i in values:
        if i != 0:
            continue
        if i == 0:
            return 'not pangram'
    return 'pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
