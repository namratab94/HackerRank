'''
Sample input:
2
1 2

Sample output:
3713081631934410656
'''

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    print hash(tuple(integer_list))
    # print hash((1, 2))
