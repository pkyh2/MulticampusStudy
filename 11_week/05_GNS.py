numbers = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
T = int(input())
for t in range(T):
    n, num = map(str, input().split())
    numStr = input().split()
    strToNum = []   # [(0, "ZRO"), (4, "FOR"), ...]
    for i in numStr:
        for key, value in numbers.items():  # 비효율적인 것 같에..
            if i == key:
                strToNum.append((value, key))
    strToNum.sort()
    
    print(n)
    for i in strToNum:
        print(i[1], end=' ')