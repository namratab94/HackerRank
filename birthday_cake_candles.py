'''
Source: https://www.hackerrank.com/challenges/birthday-cake-candles

Sample input:
4
3 2 1 3

Sample output:
2
'''
#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    tallest_candle_height = max(ar)
    num_of_tallest_candles = ar.count(tallest_candle_height)
    return num_of_tallest_candles



n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
