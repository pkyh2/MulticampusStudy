# range = 1000000
# import math
# num = 1000000

# for i in range(num):
#     cnt = 0
#     if i > 1:
#         for j in range(2, int(math.sqrt(i))+1):
#             if i % j == 0:
#                 cnt += 1
#         if cnt == 0:
#             print(i, end=' ')
# 시간초과

# 에라토스테네스의 체
import math
num = 1000000
def erai(num):
    prime = [True] * num

    m = int(math.sqrt(num))
    for i in range(2, m+1):
        if prime[i] == True:
            for j in range(i+i, num, i):    # i이후의 i의 배수들을 제거
                prime[j] = False
    
    return [i for i in range(2, num) if prime[i] == True]

print(*(erai(num+1)))
