for t in range(10):
    T = int(input())
    w = input()         # 찾을 문자열
    s = input()         # 전체 문자열
    cnt = 0

    for i in range(len(s)-len(w)+1):    # abcding   i에서 마지막
        if s[i:i+len(w)] == w:
            cnt += 1
    print('#{} {}'.format(T, cnt))