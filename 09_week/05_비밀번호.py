def pwCheck(list):                  # 1234
    for i in range(1, len(list)):   # 123884
        if list[i-1] == list[i]:
            list.pop(i-1)
            list.pop(i-1)
            # pop 연산 후 list길이가 i보다 작아지면 return
            if i > len(list)-1:
                return pw
            else:
                break

    return pwCheck(list)
    
for t in range(10):
    leng, pw = map(str, input().split())
    pw = list(map(int, pw))    # str는 pop을 못해서 int형으로 변경
    #[1, 2, 3, 4, ...]
    result = pwCheck(pw)

    print('#{}'.format(t+1), end=' ')
    for i in result:
        print(i, end='')
    print()