T = int(input())

for t in range(T):
    rank = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    N, K = map(int, input().split())
    total = []

    for i in range(N):
        ratio = [0.35, 0.45, 0.2]
        score = list(map(int, input().split()))
        for k in range(len(score)):
            ratio[k] = ratio[k]*score[k]

        total.append(sum(ratio))

    result = total[K-1]
    total.sort(reverse=True)
    cnt = 0
    for i in range(0, N, N//10):
        if total[i] >= result:
            cnt += 1
    print('#{} {}'.format(t+1, rank[cnt-1]))