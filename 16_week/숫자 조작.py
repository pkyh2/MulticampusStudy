T = int(input())

for t in range(T):
    num = int(input())
    N = list(map(int, str(num)))
    flag = 1
    # 최소값
    if N[0] != max(N):
        minNum = num
        temp = N[0]
        maxIdx = N.index(max(N))
        N[0] = max(N)
        N[maxIdx] = temp
        maxNum = int(''.join(list(map(lambda x:str(x), N))))
    # 최댓값이면
    else:
        maxNum = num
        if min(N) == 0:
            tp = N
            while min(tp) == 0:
                del tp[tp.index(min(N))]
                if len(tp) <= 1:
                    minNum = num
                    print('# {} {} {}'.format(t+1, minNum, maxNum))
                    flag = 0
                    break
            tpMin = min(tp)
        
            temp = N[0]
            minIdx = N.index(tpMin)
            N[0] = tpMin
            N[minIdx] = temp
            minNum = int(''.join(list(map(lambda x:str(x), N))))
        else:
            maxNum = num
            temp = N[0]
            minIdx = N.index(min(N))
            N[0] = min(N)
            N[minIdx] = temp
            minNum = int(''.join(list(map(lambda x:str(x), N))))

    if flag == 1:
        print('# {} {} {}'.format(t+1, minNum, maxNum))
    
# 모르겠다 ㅜㅜ