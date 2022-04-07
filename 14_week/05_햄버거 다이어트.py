'''
칼로리는 L을 넘지않고, 맛 점수가 가장 높은 조합을 찾아라.
'''
# 조합
from itertools import combinations

T = int(input())

for t in range(T):
    N, L = map(int, input().split())
    combi = {}
    for _ in range(N):
        T, K = map(int, input().split())
        combi[T] = K
    result = set()
    for i in range(1, N+1): # 1부터 N까지의 조합에서
        for j in set(combinations(combi.items(), i)):   # i==3, ((300, 500), (250, 300), (400, 400))
            if sum(map(lambda x: x[1], j)) <= L:
                result.add(sum(map(lambda x: x[0], j)))
    
    print('#{} {}'.format(t+1, max(result)))


T = int(input())

def get_powerset(A):
    A_size = len(A)
    A_pow = []
    for i in range(2**A_size):
        flag = bin(i)[2:].zfill(A_size)
        subset = [(list(A.values())[j], list(A.keys())[j]) for j in range(A_size) if flag[j] == '1']
        if sum(map(lambda x: x[0], subset)) <= L:
            A_pow.append(sum(map(lambda x: x[1], subset)))
    return A_pow

for t in range(T):
    N, L = map(int, input().split())
    combi = {}
    for _ in range(N):
        T, K = map(int, input().split())
        combi[T] = K
    
    print('#{} {}'.format(t+1, max(get_powerset(combi))))