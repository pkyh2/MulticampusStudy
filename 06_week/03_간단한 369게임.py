N = int(input())

numbers = list(range(1, N+1))

for num in numbers:
    temp = num
    flag = 0
    cnt = ''
    while temp > 0:
        if temp % 10 in [3, 6, 9]:
            flag = 1
            cnt += '-'
            temp //= 10
        else:
            temp //= 10
    
    if flag == 1:
        print(cnt, end=' ')
    else:
        print(num, end=' ')