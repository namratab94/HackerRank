#!/bin/python

import sys

'''
n = int(raw_input().strip())
calories = map(int, raw_input().strip().split(' '))
'''
n = 3
calories = [1, 3, 2, 1]
# your code goes here

def miles_counter(n, calories):
    sorted_calories =sorted(calories, reverse=True)
    num_of_miles_to_walk = 0
    for i in xrange(0, len(sorted_calories)):
        num_of_miles_to_walk += (sorted_calories[i] * pow(2, i))

    return num_of_miles_to_walk

num_of_miles = miles_counter(n, calories)
print num_of_miles
# raw_input()
# print(sum(c * 2 ** j for (j, c) in enumerate(sorted(map(int, calories), reverse=True))))