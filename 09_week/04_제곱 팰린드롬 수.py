T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    nums = list(range(a, b+1))
    for i in nums:
        if i