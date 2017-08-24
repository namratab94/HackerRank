'''
Source: https://www.hackerrank.com/challenges/staircase

Sample input:
6

Sample output:
     #
    ##
   ###
  ####
 #####
######
'''
#!/bin/python

import sys


n = int(raw_input().strip())


def line_creator(space_count, n):
    hash_count = n - space_count
    line = ''
    for i in range(space_count):
        line += ' '
    for i in range(hash_count):
        line += '#'
    line += '\n'
    return line

line = ''
for i in range(n-1, -1, -1):
    line += line_creator(i, n)

print(line)
