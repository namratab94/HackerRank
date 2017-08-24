'''
Source: https://www.hackerrank.com/challenges/diagonal-difference

Sample input:
3
11 2 4
4 5 6
10 8 -12

Sample output:
15
'''

#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
# print a
length_of_matrix_diagonal = len(a[0])
principle_diagonal = [a[i][i] for i in xrange(length_of_matrix_diagonal)]
reverse_principle_diagonal = [a[length_of_matrix_diagonal-1-i][i] for i in xrange(length_of_matrix_diagonal-1,-1,-1)]

principle_diagonal_sum = sum(principle_diagonal)
reverse_principle_diagonal_sum = sum(reverse_principle_diagonal)

abs_difference = abs(principle_diagonal_sum - reverse_principle_diagonal_sum)
print abs_difference