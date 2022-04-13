T = int(input())

for t in range(T):
    A, B = map(int, input().split())
    print('#{} {}'.format(t+1, (A*A)//(B*B)))