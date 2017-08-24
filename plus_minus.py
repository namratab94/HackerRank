'''
Source: https://www.hackerrank.com/challenges/plus-minus

Sample input:
6
-4 3 -9 0 4 1

Sample output:
0.500000
0.333333
0.166667
'''

#!/bin/python

from __future__ import division
import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
total_entries = len(arr)

pos_count = 0
zero_count = 0
neg_count = 0

for each_term in arr:
    if each_term > 0:
        pos_count += 1
    elif each_term < 0:
        neg_count += 1
    else:
        zero_count += 1

pos_score = pos_count / total_entries
zero_score = zero_count / total_entries
neg_score = neg_count / total_entries

print '%.6f' % pos_score
print '%.6f' % neg_score
print '%.6f' % zero_score