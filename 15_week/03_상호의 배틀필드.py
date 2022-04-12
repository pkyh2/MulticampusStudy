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
    map = [[] for _ in range(H)]
    for i in range(H):
        map[i].append(input())
    commandLen = int(input())
    command = input()

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] in ['^', 'v', '<', '>']:
                tPos = (i, j)
                tank = map[i][j]

    for i in command:
        if i == 'S':
            if tank == '<':
                i = 1
                while True:
                    if map[tPos[0]][tPos[1]-i] == '*': # 벽돌
                        map[tPos[0]][tPos[1]-i] = '.'
                        break
                    elif i < 0:
                        break
                    else:
                        i += 1
                        
            if tank == '^':
                i = len(map)
                while True:
                    if map[tPos[0]-i][tPos[1]] == '*': # 벽돌
                        map[tPos[0]-i][tPos[1]] = '.'
                        break
                    elif i < 0:
                        break
                    else:
                        i += 1


