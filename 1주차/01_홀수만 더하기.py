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
    '''
    input()을 받고 공백을 기준으로 split하여 ["1 2 3 4"] -> ["1", "2", "3", "4"]
    나온 x를 int(x) 로 변환해준다. [1,2,3,4]
    '''
    result = sum(numbers)
    print('#{} {}'.format(t+1, result))