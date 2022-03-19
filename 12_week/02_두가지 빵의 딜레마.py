'''
현미빵 A
단호박 빵 B
은비 C
빵 종류 상관없이 최대한 많은 빵개수?
'''

T = int(input())

for t in range(T):
    a, b, c = map(int, input().split())
    cnt = 0
    if a > b:
        cnt = c // b
    else:
        cnt = c // a
    print('#{} {}'.format(t+1, cnt))