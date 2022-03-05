for t in range(10):
    T = int(input())
    w = input()
    s = input()
    cnt = 0

    for i in range(len(s)-len(w)+1):
        if s[i:i+len(w)] == w:
            cnt += 1
    print('#{} {}'.format(T, cnt))