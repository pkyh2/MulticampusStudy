def coordinate (p, q):
    # 좌표 평면 생성
    plane = [[] for _ in range(142)]
    cnt = 1
    for i in range(142):
        for j in range(i+1):
            plane[i].insert(0, cnt)
            cnt += 1
    
    # 문제 풀이
    comma = []
    for i in range(142):
        for j in range(i+1):
            if plane[i][j] == p:
                comma.append([i, j])
            if plane[i][j] == q:
                comma.append([i, j])
                break
    
    sumComma = (comma[0][0]+comma[0][1], comma[1][0]+comma[1][1])
    print(sumComma)
    return plane[sumComma[0]][sumComma[1]]

T = int(input())
for t in range(T):
    p, q = map(int, input().split())
    print('#{} {}'.format(t+1, coordinate(p, q)))