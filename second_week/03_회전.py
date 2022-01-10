'''
N개의 숫자로 이루어진 수열에서 맨앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 맨 앞의 숫자를 출력하시오.
'''

# 풀이1(rotate)
from collections import deque

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    de = deque(list(map(int, input().split())))
    for _ in range(M):
        de.rotate(-1)
    print('#{} {}'.format(t+1, de[0]))