def deadlock(col):
    global cnt

    check = []
    for i in col:
        if i != 0:
            check.append(i)
    
    for i in range(len(check)-1):
        if check[i] == 1 and check[i+1] == 2:
            cnt += 1

for t in range(10):
    N = int(input())
    magnet = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        vertical = []
        for j in range(N):
            vertical.append(magnet[j][i])
        deadlock(vertical)
    print('#{} {}'.format(t+1, cnt))