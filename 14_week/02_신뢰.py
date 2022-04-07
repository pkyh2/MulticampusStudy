T = int(input())

def button(robot, pos):
    global posB, posO, time
    if robot == 'B':
        if pos > posB:      # move
            posB += 1
            time += 1
        elif pos == posB:   # click
            time += 1

for t in range(T):
    test = list(map(str, input().split()))
    time = 0
    posB, posO = 1, 1
    for i in range(1, len(test), 2):
        pass