#!/bin/python

import sys


def minimumAbsoluteDifference(n, arr):
    # Complete this function
    minimum_difference = 100000
    sorted_list = sorted(arr, reverse=True)
    for i in xrange(0, len(sorted_list)-1):
    # while i < len(sorted_list):
        diff_val = abs(sorted_list[i] - sorted_list[i+1])
        if diff_val < minimum_difference:
            minimum_difference = diff_val
    return minimum_difference


if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    result = minimumAbsoluteDifference(n, arr)
    print result
