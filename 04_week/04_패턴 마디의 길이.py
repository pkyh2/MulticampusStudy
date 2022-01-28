T = int(input())

for t in range(T):
    string = input()
    pattern = str(string[0])    # 'KO'
    for i in range(1, len(string)+1):
        if pattern[0:i] == string[i:i+i]:
            print('#{} {}'.format(t+1, len(pattern)))
            break
        else:
            pattern += string[i]