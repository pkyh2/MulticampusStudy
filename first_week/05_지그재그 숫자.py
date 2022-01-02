'''
1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자
'''

T = int(input())

for t in range(T):
    N = int(input())
    zigzagNum = 0
    for i in range(1, N+1):
        if i % 2 == 1:
            zigzagNum += i
        else:
            zigzagNum -= i

    print('#{} {}'.format(t+1, zigzagNum))