'''
N = 2**a * 3**b * 5**c * 7**d * 11**e

N이 주어질때 a, b, c, d, e를 출력하시오.
'''

T = int(input())

def primeFactorization(n, list1):
    if n % 2 == 0:
        list1[0] += 1
        return primeFactorization(n//2, list1)
    elif n % 3 == 0:
        list1[1] += 1
        return primeFactorization(n//3, list1)
    elif n % 5 == 0:
        list1[2] += 1
        return primeFactorization(n//5, list1)
    elif n % 7 == 0:
        list1[3] += 1
        return primeFactorization(n//7, list1)
    elif n % 11 == 0:
        list1[4] += 1
        return primeFactorization(n//11, list1)
    elif n == 1:
        result = []
        for i in list1:
            result.append(str(i))
        return result

for t in range(T):
    N = int(input())
    abcde = [0] * 5
    print('#{} {}'.format(t+1, ' '.join(primeFactorization(N, abcde))))