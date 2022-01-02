'''
10개의 수를 입력받아 평균값을 출력하는 프로그램을 작성
(소수점 첫째 자리에서 반올림한 정수를 출력)
'''

T = int(input())

for t in range(T):
    numbers = list(map(int, input().split()))
    average = int(round(sum(numbers)/len(numbers), 0))
    print('#{} {}'.format(t+1, average))