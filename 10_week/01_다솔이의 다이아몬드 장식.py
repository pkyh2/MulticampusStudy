T = int(input())

for t in range(T):
    word = input()
    col = 5 + (len(word)-1)*4
    deco = [['.'] * col for _ in range(5)]  # 5x5 "."
    
    for i in range(5):
        for j in range(col):
            if i == 0 or i == 4:            # 1, 5줄
                if j == 2 or j % 4 == 2:
                    deco[i][j] = '#'
            elif i == 1 or i == 3:          # 2, 4줄
                if j % 2 == 1:
                    deco[i][j] = '#'
            else:                           # 가운데 줄
                if j % 4 == 0:
                    deco[i][j] = '#'
                elif j == 2 or j % 4 == 2:
                    deco[i][j] = word[j//4]

    for i in deco:
        print(''.join(i))