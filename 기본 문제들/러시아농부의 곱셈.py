# 러시아 농부의 곱셈
'''
두 수중 작은 수를 왼쪽에 입력한다.
왼쪽 숫자를 계속 2씩 나눠준다. 나머지는 버린다.(//연산)
오른쪽 숫자는 곱하기 2씩해준다.
왼쪽 숫자가 1이 될 때까지 반복하고
그 숫자들 중에서 왼쪽 숫자가 짝수면 오른쪽 숫자와 함께 제거한다.
나머지 숫자들의 합을 구한다.
'''

left, right = map(int, input().split())
pair = []
while left:
    leftRight = [left, right]
    pair.append(leftRight)
    left //= 2
    right *= 2
print(pair)
result = 0
for i in pair:
    if i[0] % 2 == 1:
        result += sum(i)

print(result)