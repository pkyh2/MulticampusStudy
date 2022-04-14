T = int(input())

for t in range(T):
    num = int(input())
    flag = 0
    for i in range(1, 10):
        if num // i < 10 and (num // i) * i == num:
            print('#{} {}'.format(t+1, 'Yes'))
            flag = 1
            break
    if flag == 0:
        print('#{} {}'.format(t+1, 'No'))