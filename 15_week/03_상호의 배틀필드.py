'''
문자	의미
.	평지(전차가 들어갈 수 있다.)
*	벽돌로 만들어진 벽
#	강철로 만들어진 벽
-	물(전차는 들어갈 수 없다.)
^	위쪽을 바라보는 전차(아래는 평지이다.)
v	아래쪽을 바라보는 전차(아래는 평지이다.)
<	왼쪽을 바라보는 전차(아래는 평지이다.)
>	오른쪽을 바라보는 전차(아래는 평지이다.)

문자	동작
U	Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
D	Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
L	Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
R	Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
S	Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.
'''

T = int(input())

for t in range(T):
    H, W = map(int, input().split())
    _map = []*H
    for i in range(H):
        # 맵 입력
        _map.append(list(input()))
    commandLen = int(input())
    command = input()

    # 명령어 실행
    for cmd in command:
        # 탱크 위치 찾기
        for i in range(len(_map)):
            for j in range(len(_map[i])):
                if _map[i][j] in ['^', 'v', '<', '>']:
                    tPos = (i, j)
                    tank = _map[i][j]

        # 미사일 발사
        if cmd == 'S':
            if tank == '<':
                i = 1

                while True:
                    # x축 인덱스가
                    if tPos[1] - i >= 0:
                        # _map[tPos[0]][tPos[1]] 탱크위치
                        if _map[tPos[0]][tPos[1]-i] == '*': # 벽돌
                            _map[tPos[0]][tPos[1]-i] = '.'
                            break
                        elif _map[tPos[0]][tPos[1]-i] == '#':  # 강철
                            break
                    else:
                        break
                    i += 1
                        
            elif tank == '^':
                i = 1
                while True:
                    if tPos[0] - i >= 0:
                        if _map[tPos[0]-i][tPos[1]] == '*': # 벽돌
                            _map[tPos[0]-i][tPos[1]] = '.'
                            break
                        elif _map[tPos[0]-i][tPos[1]] == '#':  # 강철
                            break
                    else:
                        break
                    i += 1

            elif tank == 'v':
                i = 1
                while True:
                    if tPos[0] + i < H:
                        if _map[tPos[0]+i][tPos[1]] == '*': # 벽돌
                            _map[tPos[0]+i][tPos[1]] = '.'
                            break
                        elif _map[tPos[0]+i][tPos[1]] == '#':  # 강철
                            break
                    else:
                        break
                    i += 1

            elif tank == '>':
                i = 1
                while True:
                    if tPos[1] + i < W:
                        if _map[tPos[0]][tPos[1]+i] == '*': # 벽돌
                            _map[tPos[0]][tPos[1]+i] = '.'
                            break
                        elif _map[tPos[0]][tPos[1]+i] == '#':  # 강철
                            break
                    else:
                        break
                    i += 1

        elif cmd == 'U':
            _map[tPos[0]][tPos[1]] = '^'
            if tPos[0]-1 >= 0:
                if _map[tPos[0]-1][tPos[1]] == '.':
                    _map[tPos[0]-1][tPos[1]] = '^'
                    _map[tPos[0]][tPos[1]] = '.'
                else:
                    continue
        
        elif cmd == 'D':
            _map[tPos[0]][tPos[1]] = 'v'
            if tPos[0]+1 < H:
                if _map[tPos[0]+1][tPos[1]] == '.':
                    _map[tPos[0]+1][tPos[1]] = 'v'
                    _map[tPos[0]][tPos[1]] = '.'
                else:
                    continue

        elif cmd == 'L':
            _map[tPos[0]][tPos[1]] = '<'
            if tPos[1]-1 >= 0:
                if _map[tPos[0]][tPos[1]-1] == '.':
                    _map[tPos[0]][tPos[1]-1] = '<'
                    _map[tPos[0]][tPos[1]] = '.'
                else:
                    continue

        elif cmd == 'R':
            _map[tPos[0]][tPos[1]] = '>'
            if tPos[1]+1 < W:
                if _map[tPos[0]][tPos[1]+1] == '.':
                    _map[tPos[0]][tPos[1]+1] = '>'
                    _map[tPos[0]][tPos[1]] = '.'
                else:
                    continue

    print('#{}'.format(t+1), end=' ')
    for i in _map:
        for j in i:
            print(j, end='')
        print()