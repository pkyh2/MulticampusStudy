T = int(input())

for t in range(T):
    N = int(input())
    alZip = [[] for _ in range(20)]     # 1 <= N <= 10 and 1 <= Ki <= 20
    idx = 0
    for n in range(N):
        Ci, Ki = input().split()
        for i in range(int(Ki)):
            alZip[idx].append(Ci)
            if len(alZip[idx]) == 10:
                idx += 1


            # if len(alZip[n]) == 10:
            #     alZip[n+1].append(Ci)

    print('#{}'.format(t+1))
    for i in alZip:
        if i:
            print(''.join(i)) 

