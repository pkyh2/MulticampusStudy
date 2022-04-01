from itertools import combinations

T = int(input())

for t in range(T):
    game = list(map(int, input().split()))
    sumList = set()
    for i in list(combinations(game, 3)):
        sumList.add(sum(i))
    sumList = list(sumList)
    sumList.sort()
    print('#{} {}'.format(t+1, sumList[-5]))