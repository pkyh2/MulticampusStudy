T = int(input())

for t in range(T):
    N = int(input())
    numMatrix = [list(map(int, input.split())) for _ in range(N)]
    angle_90 = list(map(list, zip(*numMatrix)))