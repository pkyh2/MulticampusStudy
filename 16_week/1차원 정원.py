T = int(input())

for t in range(T):
    N, D = map(int, input().split())
    flower = list(range(1, N+1))
    sprayer = 1 + 2*D
    if N % sprayer == 0:
        print('#{} {}'.format(t+1, N//sprayer))
    else:
        print('#{} {}'.format(t+1, N//sprayer+1))