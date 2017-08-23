import sys
import itertools
'''
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
'''

if __name__ == '__main__':
    N = int(raw_input())

    data = []
    for n in range(N):
        data_input = raw_input().split()
        command = data_input[0]
        arguments = list(map(int, data_input[1:]))
        if command == 'print':
            print(data)
        else:
            getattr(data, command)(*arguments)