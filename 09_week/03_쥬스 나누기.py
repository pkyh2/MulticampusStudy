'''
1리터 N명이 나눠 마셔
첫번째 사람은 원하는 만큼 잔에 따를 수 있고 마지막 사람은 맨 처음 잔을 선택할 수 있다.
'''

T = int(input())
for t in range(T):
    N = int(input())
    juice = []
    for i in range(N):
        juice.append('1/{}'.format(N))
    print('#{} {}'.format(t+1, ' '.join(juice)))