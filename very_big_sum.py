'''
Source: https://www.hackerrank.com/challenges/a-very-big-sum

Sample input:
5
1000000001 1000000002 1000000003 1000000004 1000000005

Sample output:
5000000015
'''
#!/bin/python

import sys

def aVeryBigSum(n, ar):
    # Complete this function
    sum_val = 0
    for i in xrange(0, n):
        sum_val += ar[i]
    return sum_val

n = int(raw_input().strip())
ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)
