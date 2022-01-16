'''
level     
samsung
eye  
'''

T = int(input())
for t in range(T):
    flag = 0
    palindrome = list(input())
    for i in range(len(palindrome)//2):
        if palindrome[i] == palindrome.pop():
            continue
        else:
            print('#{} {}'.format(t+1, 0))
            flag = 1
            break
    if flag == 0:
        print('#{} {}'.format(t+1, 1))