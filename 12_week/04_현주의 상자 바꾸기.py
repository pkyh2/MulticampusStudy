'''
1번부터 N번까지 N개의 상자를 가지고 있다.
처음에는 모두 0
'''

T = int(input())
for t in range(T):
    n, q = map(int, input().split())
    box = [0]*n
    for i in range(1, q+1):
        l, r = map(int, input().split())
        for j in range(l-1, r):
            box[j] = i
    
    print('#{}'.format(t+1), *box)