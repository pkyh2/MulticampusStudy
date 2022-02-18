T = int(input())

for t in range(T):
    word = input()

    canSee = ''
    for i in word:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            canSee += i

    print('#{} {}'.format(t+1, canSee))
# 레벨3 맞나..