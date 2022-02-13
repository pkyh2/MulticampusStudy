T = int(input())

for t in range(T):
    nums = list(map(int, input().split()))
    nums.sort()
    result = int(round(sum(nums[1:-1])/len(nums[1:-1]), 0))
    print('#{} {}'.format(t+1, result))