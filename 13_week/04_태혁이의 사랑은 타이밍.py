T = int(input())

for t in range(T):
    D, H, M = map(int, input().split())
    
    # 1D = 1440M 1H = 60M
    llll = 11*1440 + 11*60 + 11
    sadStory = D*1440 + H*60 + M

    if llll > sadStory:
        print('#{} {}'.format(t+1, -1))
    else:
        print('#{} {}'.format(t+1, sadStory - llll))     