'''
수열의 합으로 해당 라인의 처음 수와 끝 수를 구한다.
처음 수의 좌표는 (1, 해당라인의 개수)
'''
def comma(num): # num의 좌표를 구한다.
    sum, i = 0, 1
    while sum < num:    # 몇번째 줄에 있는지 확인
        sum += i
        i += 1

    n = i - 1
    start = 1 + ((n-1)*n)//2        # 7(1,4) 8(2,3) 9 10(4,1)
    end = (n*(n+1))//2
    x = num - start + 1
    y = end - num + 1
    return [x, y]

T = int(input())
for t in range(T):
    p, q = map(int, input().split())
    commaSum = []
    commaSum.append(comma(p))
    commaSum.append(comma(q))
    commaSum.append(commaSum[0][0]+commaSum[1][0])
    commaSum.append(commaSum[0][1]+commaSum[1][1])
    # commaSum =[[2, 3], [3, 3], 5, 6]
    # print(commaSum)

    n = commaSum[2] + commaSum[3]
    end = (n*(n-1))//2
    answer = end - commaSum[3] + 1
    print('#{} {}'.format(t+1, answer))
