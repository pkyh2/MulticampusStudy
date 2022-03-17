'''
뿔이 1개 달린 유니콘
뿔이 2개 달린 트윈혼
n개의 뿔과 m마리의 짐승을 보았다.
유니콘과 트윈혼은 각각 몇마리?
'''

T = int(input())
for t in range(T):
    n, m = map(int, input().split())    # n뿔, m마리
    # x 트윈혼, y 유니콘
    x = n - m           # 2x + y = 5 -> x = 5 - 3
    y = m - x           # x + y = 3
    print('#{} {} {}'.format(t+1, y, x))