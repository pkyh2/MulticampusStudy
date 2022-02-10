T = int(input())

for t in range(T):
    N, M = map(int, input().split())    # 5, 2 -> 5x5, 2x2
    bugsWorld = [list(map(int, input().split())) for _ in range(N)]
    killBugs = []

    for i in range(N - M + 1):      # 5-2+1 = 4
        for j in range(N - M + 1):
            swing = []
            for k in range(M):
                swing += bugsWorld[i+k][j:j+M]
            killBugs.append(sum(swing))

    print('#{} {}'.format(t+1, max(killBugs)))