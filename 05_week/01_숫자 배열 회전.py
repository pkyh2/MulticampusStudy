T = int(input())

for t in range(T):
    N = int(input())
    numMatrix = [input().replace(' ', '') for _ in range(N)]

    angle_270 = []
    angle_90 = []
    angle_180 = []

    for i in range(N):
        str_90 = ''
        str_270 = ''
        for j in range(N):
            str_90 += numMatrix[N-1-j][i]
            str_270 += numMatrix[j][N-1-i]
        angle_90.append(str_90)
        angle_270.append(str_270)
        
    for i in range(N-1, -1, -1):
        angle_180.append(numMatrix[i][::-1])

    print('#{}'.format(t+1))
    for i in range(N):
        print('{} {} {}'.format(angle_90[i], angle_180[i], angle_270[i]))