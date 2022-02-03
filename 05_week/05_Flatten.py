for t in range(10):
    dump = int(input())
    boxHeight = list(map(int, input().split()))
    for i in range(dump):
        maxiIndex = boxHeight.index(max(boxHeight))
        miniIndex = boxHeight.index(min(boxHeight))
        boxHeight[maxiIndex] -= 1
        boxHeight[miniIndex] += 1
    print('#{} {}'.format(t+1, max(boxHeight) - min(boxHeight)))