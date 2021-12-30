# n = int(input())

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 2) + fibonacci(n - 1)

# print(fibonacci(n))
# 시간초과

# n = int(input())

# def fibonacci(n):
#     a1 = 0
#     a2 = 1
#     i = 0

#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1

#     while i < n - 1:
#         temp = a2
#         a2 = a1 + a2
#         a1 = temp
#         i += 1
    
#     return a2

# print(fibonacci(n))
# 29200 72

n = int(input())

def fibonacci2(n):
    arr = [0, 1]
    if n == 0:
        return arr[0]
    elif n == 1:
        return arr[1]
    
    for i in range(2, n + 1):
        arr.append(arr[i - 2]+ arr[i - 1])
    return max(arr)

print(fibonacci2(n))
# 29200 68