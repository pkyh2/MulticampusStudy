T = int(input())

for t in range(T):
    A, B = map(int, input().split())
    if A % B == 0:
        print('#{} {}'.format(t+1, (A*A)//B))