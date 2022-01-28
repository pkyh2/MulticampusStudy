import math
T = int(input())

for t in range(T):
    N = int(input())
    farm = [list(input()) for _ in range(N)]
    revenue = 0

    # 처음부터 중간까지
    for y in range(N//2+1): # 0에서 중간index 까지
        for x in range(1 + y*2):    # 1, 3, 5, 7, 9
            revenue += int(farm[y][x+(N//2)-y])    

    # 맨 아래 줄에서 중간 전까지
    for y in range(N-1, N//2, -1):      # 4, 2, -1
        for x in range(2*N-2*y-1):      # 2*5 - 2*4 - 1 = 1
            revenue += int(farm[y][x + y-(N//2)])   # [0+ 4 - 2]

    print('#{} {}'.format(t+1, revenue))