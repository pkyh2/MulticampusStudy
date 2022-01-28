'''
10개의 수를 입력받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성
'''
# 풀이1(for)
T = int(input())
for t in range(T):
    numbers = list(map(int, input().split()))
    sum = 0
    for num in numbers:
        if num % 2 != 0:
            sum += num

    print('#{} {}'.format(t + 1, sum))

# 풀이2(list comprehension)
T = int(input())
for t in range(T):
    numbers = [int(x) for x in input().split() if int(x) % 2 != 0]
    result = sum(numbers)
    print('#{} {}'.format(t+1, result))