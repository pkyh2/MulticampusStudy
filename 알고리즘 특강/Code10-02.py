# 팩토리얼
n = int(input())

def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * factorial(num-1)
print(factorial(n))

# 별출력
def countingStar(num):
    if num > 0:
        countingStar(num-1)
        print('*'*num)

countingStar(n)

# 구구단
def gugu(dan, num):
    print('{} x {} = {}'.format(dan, num, dan * num))
    if num < 9:
        gugu(dan, num+1)


for dan in range(2, 10): # 2 ~ 9단
    print("##%d##" % dan)
    gugu(dan, 1)