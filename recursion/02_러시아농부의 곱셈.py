def russianFarmer(rightSum, left, right):
    if left % 2 == 1:
        rightSum += right
    left //= 2
    right *= 2
    if left == 1:
        return rightSum + right
    return russianFarmer(rightSum, left, right)

left, right = map(int, input().split())
print(russianFarmer(0, left, right))
