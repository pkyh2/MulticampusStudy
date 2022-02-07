T = int(input())

for t in range(T):
    N = int(input())
    moneyCount = {
        50000:0,
        10000:0,
        5000:0,
        1000:0,
        500:0,
        100:0,
        50:0,
        10:0
    }

    for money in moneyCount.keys():
        while True:
            if N // money:
                N -= money
                moneyCount[money] += 1
            else:
                break
    
    print('#{}'.format(t+1))
    print(*list(moneyCount.values()))