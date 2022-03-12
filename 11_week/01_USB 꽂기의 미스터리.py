'''
가장 처음 USB를 꽂을 때의 확률 p(제대로), 처음 제대로 안 꽂을 확률(1-p)
만약 올바른 면으로 USB를 꽂을 확률 q
'''
T = int(input())
for t in range(T):
    p, q = map(float, input().split())
    s1 = 1*(1-p)*q
    s2 = 1*p*(1-q)*q
    if s1<s2:
        print('#{} {}'.format(t+1, 'YES'))
    else:
        print('#{} {}'.format(t+1, 'NO'))