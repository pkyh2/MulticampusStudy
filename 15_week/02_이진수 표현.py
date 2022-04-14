'''
정수 N, M이 주어질 때, M의 이진수 표현의 마지막 N비트가 모두 1로 켜져 있는지 판별
'''
# T = int(input())

# for t in range(T):
#     N, M = map(int, input().split())
#     bin = list(format(M, 'b'))[-N:] 
#     if '0' in bin:
#         print('#{} {}'.format(t+1, 'OFF'))
#     else:
#         print('#{} {}'.format(t+1, 'ON'))


T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    check = ''
    for _ in range(N):
        if M % 2 == 1:
            M //= 2
            check = "ON"
        else:
            check = "OFF"
    print('#{} {}'.format(t+1, check))
