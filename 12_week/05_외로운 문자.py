T = int(input())

for t in range(T):
    string = list(input())
    string.sort()
    stack = [string[0]]
    for i in range(1, len(string)):
        if stack:
            if stack[-1] == string[i]:
                stack.pop()
            else:
                stack.append(string[i])
        else:
            stack.append(string[i])
    if stack:
        print('#{} {}'.format(t+1, ''.join(stack)))
    else:
        print('#{} {}'.format(t+1, "Good"))