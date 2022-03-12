'''
뿔이 1개 달린 유니콘
뿔이 2개 달린 트윈혼
n개의 뿔과 m마리의 짐승을 보았다.
유니콘과 트윈혼은 각각 몇마리?
'''

T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    # x 트윈혼, y 유니콘
    x = n - m
    y = m - x
    print('#{} {} {}'.format(t+1, y, x))