T = int(input())

for t in range(T):
    N = int(input())
    pascal = [[0] * N for _ in range(N)]    # N * N 리스트 0으로 초기화

    for y in range(N):
        for x in range(N):
            if x == 0:
                pascal[y][x] = 1
            elif x == y:
                pascal[y][x] = 1
            elif y > x:
                pascal[y][x] = pascal[y-1][x-1] + pascal[y-1][x]    # 2, 1 = pascal[1][0] + pascal[1][1]

    print('#{}'.format(t+1))
    for i in range(N):
        for j in range(N):
            if pascal[i][j] != 0:
                print(pascal[i][j], end=' ')
        print()