'''
두 개의 숫자열 중 작은 숫자열을 큰 숫자열 길이안에서 움직이면서
마주보는 숫자들을 곱한뒤 더했을 때 최댓값을 구하라.
'''

# 풀이1
# len_A < len_B일때
# len_A > len_B일때
T = int(input())

for t in range(T):
    len_A, len_B = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if len_A < len_B:
        sumList = []
        for i in range(len_B - len_A + 1):
            sumAB = 0
            for j in range(len_A):
                sumAB += A[j] * B[i+j]
            sumList.append(sumAB)
        print('#{} {}'.format(t+1, max(sumList)))
    elif len_A > len_B:
        sumList = []
        for i in range(len_A - len_B + 1):
            sumAB = 0
            for j in range(len_B):
                sumAB += B[j] * A[i+j]
            sumList.append(sumAB)
        print('#{} {}'.format(t+1, max(sumList)))
    else:
        sumAB = 0
        for i in range(len_A):
                sumAB += A[i] * B[i]
        print('#{} {}'.format(t+1, sumAB))

        
