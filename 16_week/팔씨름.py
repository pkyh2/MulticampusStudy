T = int(input())

for t in range(T):
    fight = input()
    lose = 0
    for i in fight:
        if i == 'x':
            lose += 1
    if lose >= 8:
        print('#{} {}'.format(t+1, 'NO'))
    else:
        print('#{} {}'.format(t+1, 'YES'))