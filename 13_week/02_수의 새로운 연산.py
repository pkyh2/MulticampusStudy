'''
수열의 합으로 해당 라인의 처음 수와 끝 수를 구한다.
처음 수의 좌표는 (1, 해당라인의 개수)
'''
def comma(num):
    sum, i = 0, 1
    while sum < num:
        sum += i
        i += 1

    n = i - 1
    start = 1 + ((n-1)*n)//2
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
    # print(commaSum)

    n = commaSum[2] + commaSum[3]
    end = 1+ (n*(n-1))//2
    answer = end - commaSum[3]
    print('#{} {}'.format(t+1, answer))
