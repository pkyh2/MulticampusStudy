T = int(input())

for t in range(T):
    N = int(input())
    alZip = [[] for _ in range(20)]     # 1 <= N <= 10 and 1 <= Ki <= 20  총 20줄
    idx = 0
    for n in range(N):
        Ci, Ki = input().split()
        for i in range(int(Ki)):
            alZip[idx].append(Ci)       # [[AAA..], [], ...]
            if len(alZip[idx]) == 10:
                idx += 1

    print('#{}'.format(t+1))
    for i in alZip:
        if i:
            print(''.join(i))