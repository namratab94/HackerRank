'''
Source: https://www.hackerrank.com/challenges/time-conversion

Sample input:
07:05:45PM

Sample output:
19:05:45

'''

#!/bin/python

import sys

def timeConversion(s):

    meridian = s[-2]

    time = [int(i) for i in s[:-2].split(':')] # Converting each time unit to integer and obtaining
    # each unit by splitting it using ':'

    hour = time[0]
    minute = time[1]
    second = time[2]
    if meridian == 'P':
        if hour == 12:
            final_time = str(hour) + ':'
        else:
            hour += 12
            final_time = str(hour) + ':'
    else:
        if hour == 12:
            hour -= hour
            final_time = '0' + str(hour) + ':'
        else:
            final_time = '0' + str(hour) + ':'

    if minute < 10:
        minute = '0' + str(minute)

    if second < 10:
        second = '0' + str(second)


    final_time += str(minute) + ':' + str(second)

    return final_time



s = raw_input().strip()
result = timeConversion(s)
print(result)
