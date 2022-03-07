T = int(input())

for t in range(T):
    a,b,c = map(int, input().split())
    if a==b==c:
        print('#{} {}'.format(t+1, a))
    elif a==b!=c:
        print('#{} {}'.format(t+1, c))
    elif a!=b==c:
        print('#{} {}'.format(t+1, a))
    elif a==c!=b:
        print('#{} {}'.format(t+1, b))
