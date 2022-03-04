T = int(input())

for t in range(T):
    word = input()
    row = 5 + (len(word)-1)*4
    deco = [['.'] * row for _ in range(5)]
    
    for i in range(5):
        for j in range(row):
            if i == 0 or i == 4:
                if j == 2 or j % 4 == 2:
                    deco[i][j] = '#'
            elif i == 1 or i == 3:
                if j % 2 == 1:
                    deco[i][j] = '#'
            else:
                if j % 4 == 0:
                    deco[i][j] = '#'
                elif j == 2 or j % 4 == 2:
                    deco[i][j] = word[j//4]

    for i in deco:
        print(''.join(i))