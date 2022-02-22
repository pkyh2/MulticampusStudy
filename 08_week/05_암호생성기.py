'''
8개의 숫자를 입력 받는다.
첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다.
5까지 감소가 1사이클
'''

for i in range(10):
    T = int(input())
    nums = list(map(int, input().split()))
    while nums[len(nums)-1] > 0:
        for j in range(1, 6):
            if nums[0]-j > 0:
                temp = nums.pop(0)-j
                nums.append(temp)
            else:
                nums.pop(0)
                nums.append(0)

                print('#{} {}'.format(T, ' '.join(map(str, nums))))
                break