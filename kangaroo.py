"""
Source: https://www.hackerrank.com/challenges/kangaroo

Sample input0:
0 3 4 2

Sample output0:
YES


Sample input1:
0 2 5 3

Sample output1:
NO

Sample input2:
45 7 56 2

Sample output2:
NO


"""
#!/bin/python

import sys

def kangaroo(x1, v1, x2, v2):
    '''
    Initial solution, times out for a lot of cases.

    if x1 > x2 and v2 < v1:
        return 'NO'
    elif x1 < x2 and v1 < v2:
        return 'NO'

    k1_pos = x1
    k2_pos = x2
    while k1_pos != k2_pos:
        x1 += v1
        k1_pos = x1
        x2 += v2
        k2_pos = x2
    return 'YES'
    '''
    '''
    ((x2-x1)%(v1-v2)) check is to see if the difference in the speed 
    between the kangaroos can be made up by going faster.
    
    '''
    if v1 > v2 and not ((x2-x1)%(v1-v2)): # Checking if kangaroo1 can catch up with kangaroo2
        return 'YES'
    else:
        return 'NO'


x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
