for t in range(10):
    dump = int(input())
    boxHeight = list(map(int, input().split()))
    for i in range(dump):
        miniIndex = boxHeight.index(min(boxHeight))
        maxiIndex = boxHeight.index(max(boxHeight))
        boxHeight[miniIndex] += 1
        boxHeight[maxiIndex] -= 1
    print('#{} {}'.format(t+1, max(boxHeight) - min(boxHeight)))