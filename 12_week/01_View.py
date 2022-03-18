'''
양쪽 조망이 모두 2이상인 세대
'''

for t in range(1):
    dong = int(input())
    floor = list(map(int, input().split()))
    oceanView = 0
    for i in range(len(floor)-4):
        check = floor[i+2]  # 5개 동 중 중간동
        print(check)
        floor5 = floor[i:i+5]
        if check == max(floor5):  # 5개 동 중 중간 동이 가장 높으면
            floor5.remove(check)
            oceanView += check - max(floor5)
    
    print('#{} {}'.format(t+1, oceanView))
