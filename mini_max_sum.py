'''
Source: https://www.hackerrank.com/challenges/mini-max-sum

Sample input:
1 2 3 4 5

Sample output:
10 14
'''
#!/bin/python

import sys

arr = map(int, raw_input().strip().split(' '))

array_sum = sum(arr)

min_value = (array_sum-(max(arr)))
max_value = (array_sum-(min(arr)))

print(min_value, max_value)
