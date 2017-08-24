'''
Source: https://www.hackerrank.com/challenges/compare-the-triplets
'''

#!/bin/python

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function

    alice_scores = 0
    bob_scores = 0

    alice_scores, bob_scores = score_comparer(a0, b0, alice_scores, bob_scores)
    alice_scores, bob_scores = score_comparer(a1, b1, alice_scores, bob_scores)
    alice_scores, bob_scores = score_comparer(a2, b2, alice_scores, bob_scores)

    return alice_scores, bob_scores


def score_comparer(a, b, alice_scores, bob_scores):

    if a > b:
        alice_scores += 1
    elif b > a:
        bob_scores += 1

    return alice_scores, bob_scores


a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]

result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))
